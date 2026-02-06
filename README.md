🖼️ Text-to-Image Generator (Stable Diffusion)



A full-stack AI Text-to-Image Generation web application built using FastAPI, Stable Diffusion, and SQLite, supporting prompt history, reproducibility, and image downloads.



This project demonstrates end-to-end AI system integration, backend persistence, and frontend UX handling — designed as an internship-level production prototype.



🚀 Features

Core



✅ Text-to-image generation using Stable Diffusion v1.5



✅ CPU-only inference (no GPU required)



✅ FastAPI backend



✅ Responsive HTML/CSS/JS frontend



Advanced Controls



🎯 Negative prompt support



🎲 Seed control (reproducible images)



📐 Image size selector (512×512 / 768×768)



⏳ Loading spinner + progress feedback



Persistence \& UX



🖼️ Prompt history gallery



🗂️ SQLite database persistence



📁 Filesystem-backed image storage



⬇️ Download generated images



🔄 Auto-load previous generations



🧠 Tech Stack

Layer	Technology

Backend	FastAPI

AI Model	Stable Diffusion (diffusers)

Frontend	HTML, CSS, JavaScript

Database	SQLite

Image Storage	Local filesystem

Runtime	Python 3.10+

📁 Project Structure

text\_to\_image/

│

├── app/

│   └── main.py

│

├── static/

│   ├── style.css

│   └── script.js

│

├── templates/

│   └── index.html

│

├── generated\_images/

│   └── \*.png

│

├── history.db

├── requirements.txt

└── README.md



⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/your-username/text-to-image.git

cd text-to-image



2️⃣ Create Virtual Environment

python -m venv venv

venv\\Scripts\\activate   # Windows



3️⃣ Install Dependencies

pip install -r requirements.txt



4️⃣ Run the Application

python -m uvicorn app.main:app --reload



5️⃣ Open in Browser

http://127.0.0.1:8000





⚠️ First launch will be slow (Stable Diffusion model loads on CPU).



✨ Example Prompts



Prompt



A futuristic cyberpunk city at night, neon lights, ultra detailed, cinematic





Negative Prompt



blurry, low quality, distorted, extra limbs





Seed



123456





Size



512





🖼️ Image upscaling🙋‍♂️ Author  
Shriram Selvam

