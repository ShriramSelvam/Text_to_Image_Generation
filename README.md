# 🖼️ Text-to-Image Generator (Stable Diffusion)

A full-stack **AI Text-to-Image Generation** web application built using **FastAPI**, **Stable Diffusion**, and **SQLite**.  
The app supports prompt history, reproducible image generation, and image downloads through a clean web interface.

This project demonstrates **end-to-end AI system integration**, backend persistence, and frontend UX handling — designed as an **internship-level production prototype**.

---

## 🚀 Features

### Core
- ✅ Text-to-image generation using **Stable Diffusion v1.5**
- ✅ **CPU-only inference** (no GPU required)
- ✅ FastAPI backend
- ✅ Responsive HTML / CSS / JavaScript frontend

### Advanced Controls
- 🎯 **Negative prompt** support
- 🎲 **Seed control** for reproducible images
- 📐 Image size selector (**512×512 / 768×768**)
- ⏳ Loading spinner with progress feedback

### Persistence & UX
- 🖼️ Prompt history gallery
- 🗂️ SQLite database persistence
- 📁 Filesystem-backed image storage
- ⬇️ Download generated images
- 🔄 Auto-load previous generations

---

## 🧠 Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend     | FastAPI |
| AI Model    | Stable Diffusion (Hugging Face Diffusers) |
| Frontend    | HTML, CSS, JavaScript |
| Database    | SQLite |
| Image Store | Local filesystem |
| Runtime     | Python 3.10+ |

---

## 📁 Project Structure
```
text_to_image/
│
├── app/
│ └── main.py
│
├── static/
│ ├── style.css
│ └── script.js
│
├── templates/
│ └── index.html
│
├── generated_images/
│ └── *.png
│
├── history.db
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShriramSelvam/Text_to_Image_Generation.git
cd Text_to_Image_Generation
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```bash
python -m uvicorn app.main:app --reload
```
### 5️⃣ Open in Browser
```bash
http://127.0.0.1:8000
```

⚠️ Note: First launch will be slow because the Stable Diffusion model loads on CPU.

## ✨ Example Usage

## Prompt
```
A futuristic cyberpunk city at night, neon lights, ultra detailed, cinematic
```
### Negative Prompt
```
blurry, low quality, distorted, extra limbs
```
### Seed
```
123456
```
### Image Size
```
512
```

## 🙋‍♂️ Author
Shriram Selvam
