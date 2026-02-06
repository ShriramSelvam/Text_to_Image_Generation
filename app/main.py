from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import uuid
import sqlite3
import torch
from datetime import datetime
from diffusers import StableDiffusionPipeline

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
GENERATED_DIR = os.path.join(BASE_DIR, "generated_images")
DB_PATH = os.path.join(BASE_DIR, "history.db")

os.makedirs(GENERATED_DIR, exist_ok=True)

# ---------------- DB ----------------
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# Base table (SAFE + BACKWARD COMPATIBLE)
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT,
    negative_prompt TEXT,
    seed INTEGER,
    size INTEGER,
    filename TEXT,
    created_at TEXT
)
""")
conn.commit()

# ---------------- AUTO SYNC FILESYSTEM → DB ----------------
def sync_images():
    cursor.execute("SELECT filename FROM history WHERE filename IS NOT NULL")
    existing = {row[0] for row in cursor.fetchall()}

    for file in os.listdir(GENERATED_DIR):
        if file.endswith(".png") and file not in existing:
            cursor.execute("""
                INSERT INTO history
                (prompt, negative_prompt, seed, size, filename, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                "[Imported image – metadata unavailable]",
                "",
                None,
                None,
                file,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))

    conn.commit()

sync_images()

# ---------------- APP ----------------
app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/generated", StaticFiles(directory=GENERATED_DIR), name="generated")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

# ---------------- MODEL ----------------
print("🚀 Loading Stable Diffusion model (CPU)...")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32,
    safety_checker=None
).to("cpu")

print("✅ Model loaded successfully.")

# ---------------- ROUTES ----------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def generate_image(payload: dict):
    prompt = payload.get("prompt", "").strip()
    negative_prompt = payload.get("negative_prompt", "")
    seed = int(payload.get("seed", 123456))
    size = int(payload.get("size", 512))

    if not prompt:
        return JSONResponse({"error": "Prompt is required"}, status_code=400)

    generator = torch.Generator("cpu").manual_seed(seed)

    print("🖼️ Generating image...")

    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        height=size,
        width=size,
        num_inference_steps=30,
        generator=generator
    ).images[0]

    filename = f"{uuid.uuid4()}.png"
    image.save(os.path.join(GENERATED_DIR, filename))

    cursor.execute("""
        INSERT INTO history
        (prompt, negative_prompt, seed, size, filename, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        prompt,
        negative_prompt,
        seed,
        size,
        filename,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    return {"image_url": f"/generated/{filename}"}


@app.get("/history")
async def get_history():
    cursor.execute("""
        SELECT prompt, negative_prompt, seed, size, filename, created_at
        FROM history
        WHERE filename IS NOT NULL
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    return [
        {
            "prompt": r[0],
            "negative_prompt": r[1],
            "seed": r[2],
            "size": r[3],
            "image_url": f"/generated/{r[4]}",
            "created_at": r[5]
        }
        for r in rows
    ]
