# 📄 Resume Analyzer AI

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green.svg)
![Google Gemini](https://img.shields.io/badge/LLM-Gemini%202.5-blueviolet.svg)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

Deployed App Link:
https://atsresume-analyzer.streamlit.app/

---

## 📌 Overview

AI-powered ATS resume analyzer that compares resumes with job descriptions and provides match scoring and improvement suggestions.

---

![Homepage](images/homepage.png)

---

## 🚀 Features
- 📄 Resume PDF parsing
- 📚 Job description analysis
- 🔎 ATS match scoring
- 💡 Skill gap detection
- 📦 AI-powered feedback using Gemini
- 💬 Clean Streamlit UI

---
## Tech Stack

| Component        | Technology |
|----------------|-----------|
| Frontend       | Streamlit |
| LLM            | Google Gemini (`gemini-2.5-flash`) |
| Embeddings     | `gemini-embedding-001` |
| Framework      | LangChain |
| Vector DB      | FAISS |
| PDF Processing  | PyMuPDF (`fitz`) |
| Keyword Extraction  | NLP |
| Language       | Python |

---

## System Architecture
![Architecture](images/Architecture.png) 

---

## 📦 Installation

```bash
git clone <repo>
cd resume-analyzer-ai
pip install -r requirements.txt
streamlit run app.py
```

🔑 API Key Setup
You need a Google Gemini API Key.
Get it from:
👉 https://ai.google.dev/
No need for .env file — the app accepts it directly via Streamlit sidebar.

![API Required](images/api_required.png)

---

▶️ Run the Deployed App (Link):

https://atsresume-analyzer.streamlit.app/
---

## 💡 How to Use
1. Enter your Gemini API Key in the sidebar
2. Upload Resume in PDF format
3. Enter/Paste the Job Desciption
4. Click “Analyze Resume”
5. Wait for processing to complete
6. ATS style match score is displayed
7. Missing keywords and improvement sugestions are also displayed

📚 Example Use Cases
- Job Application Optimization
- ATS Resume Scoring
- Skill Gap Identification
- Resume Improvement Suggestions

![Chat Example](images/chat_example.png)

---

🚀 Future Improvements
- 💾 Add PDF report download
- 📌 Add multi-resume comparison
- 📊  Add job recommendation system
- 💾 Add database storage

---

## 👨‍💻 Author
Muhammad Ali Waris Khan
- AI / ML Enthusiast | Building RAG Systems & LLM Applications

---
