# 🚀 ClearCall

> **Know why your resume might get rejected before you apply.**

**ClearCall** is an explainable resume analysis tool that compares your resume against a job description and provides a transparent breakdown of your compatibility with the role.

Instead of giving a mysterious "match score," ClearCall explains **how the score was calculated**, identifies missing qualifications, highlights potential rejection reasons, and suggests actionable improvements to increase your chances of getting shortlisted.

---

# ✨ Features

* 📄 Extracts text from PDF resumes
* 🎯 Compares resumes against job descriptions
* 📊 Generates an explainable match score
* ✅ Identifies matched and missing skills
* 💼 Detects experience gaps
* 🎓 Checks education requirements
* ⚠️ Explains why an application may be rejected
* 💡 Provides resume improvement suggestions
* 📚 Recommends skills to learn for better alignment

---

# 🤔 Why ClearCall?

Many companies use Applicant Tracking Systems (ATS) to filter resumes before they ever reach a recruiter. These systems often reject applications without giving applicants any explanation.

ClearCall makes this process transparent by showing:

* What matches the job requirements
* What is missing
* Why your resume scored the way it did
* What you can improve before applying

Every result is backed by clear, inspectable rules—no black-box decisions.

---

# ⚙️ How It Works

```text
                 Job Description
                        +
                   Resume (PDF)
                        │
                        ▼
        ┌──────────────────────────────┐
        │ Extract Resume Text          │
        │ Parse Resume & Job Details   │
        │ Compare Skills & Experience  │
        │ Calculate Match Score        │
        │ Generate Explanations        │
        └──────────────────────────────┘
                        │
                        ▼
        Match Score
        Skill Analysis
        Experience Gap
        Education Check
        Rejection Reasons
        Improvement Plan
```

---

# 🛠 Tech Stack

## Frontend

* React 19
* Vite
* Axios
* Recharts

## Backend

* FastAPI
* Uvicorn
* pdfplumber
* scikit-learn
* Pydantic

## Database

ClearCall is **stateless** and does not require a database. Every analysis is performed in real time using the uploaded resume and provided job description.

---

# 📁 Project Structure

```text
ClearCall
│
├── backend
│   ├── app
│   │   ├── data
│   │   │   └── skills_list.json
│   │   ├── models
│   │   │   └── schemas.py
│   │   ├── routes
│   │   │   └── analyze.py
│   │   ├── services
│   │   │   ├── jd_parser.py
│   │   │   ├── resume_parser.py
│   │   │   ├── pdf_extractor.py
│   │   │   ├── matcher.py
│   │   │   └── suggestions.py
│   │   ├── config.py
│   │   └── main.py
│   ├── requirements.txt
│   └── run.py
│
└── frontend
    ├── src
    │   ├── api
    │   ├── components
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── index.css
    ├── package.json
    ├── index.html
    └── .env
```

---

# 📋 Prerequisites

Install the following before running the project.

* Python **3.11+**
* Node.js **18+**
* npm
* Git

Verify your installation:

```bash
python --version
node --version
npm --version
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

---

## 2. Backend Setup

Navigate to the backend directory.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

(Optional) Create a `.env` file inside `backend/`.

```env
FRONTEND_URL=http://localhost:5173
```

Run the backend.

```bash
python run.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

Health check:

```
GET /
```

```json
{
  "message": "ClearCall API running.",
  "status": "healthy"
}
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

Open a new terminal.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Create a `.env` file.

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Run the frontend.

```bash
npm run dev
```

Open the URL shown by Vite (usually):

```
http://localhost:5173
```

---

# 💻 Using ClearCall

1. Paste a complete job description (minimum 30 characters).
2. Upload a **text-based PDF** resume.
3. Click **Analyze My Resume**.
4. Review the generated report.

The report includes:

* Match score
* Skills matched
* Missing skills
* Experience analysis
* Education analysis
* Resume relevance
* Rejection reasons
* Resume improvement suggestions
* Upskilling recommendations

---

# 🌍 Environment Variables

| File            | Variable            | Default                 |
| --------------- | ------------------- | ----------------------- |
| `backend/.env`  | `FRONTEND_URL`      | `http://localhost:5173` |
| `frontend/.env` | `VITE_API_BASE_URL` | `http://127.0.0.1:8000` |

The project works with default values, so these files are optional unless you're using different ports or deploying the application.

---

# 📡 API

## POST `/api/analyze`

### Request

Multipart form data.

| Field             | Type | Description                                  |
| ----------------- | ---- | -------------------------------------------- |
| `job_description` | Text | Full job description (minimum 30 characters) |
| `resume`          | PDF  | Text-based resume                            |

---

### Successful Response

```json
{
  "match_score": 34.8,
  "verdict": "Low match",
  "score_breakdown": {
    "skill_match_score": 11.1,
    "relevance_score": 16.0,
    "experience_score": 100.0,
    "education_score": 100.0
  },
  "matched_skills": [
    "communication",
    "git",
    "github",
    "python"
  ],
  "missing_skills": [
    "agile",
    "aws",
    "api development"
  ],
  "experience": {},
  "education": {},
  "rejection_reasons": [],
  "resume_fixes": [],
  "upskilling_suggestions": [],
  "resume_text_preview": ""
}
```

---

### Error Responses (400)

Returned when:

* Job description contains fewer than 30 characters.
* Uploaded file is not a PDF.
* PDF contains no extractable text.
* Uploaded PDF is image-based or scanned.

---

# 🩺 Troubleshooting

### Backend connection failed

Ensure the backend is running.

```bash
python run.py
```

Also verify that `VITE_API_BASE_URL` matches your backend URL.

---

### No readable text found

Your resume is likely a scanned PDF.

Export the resume directly from Word, Google Docs, or another editor instead of scanning a printed copy.

---

### CORS errors

Verify that the frontend URL is included in the backend's allowed origins.

If necessary, set:

```env
FRONTEND_URL=http://localhost:5173
```

---

### Dependency installation fails

Ensure that:

* Python 3.11 or newer is installed.
* Your virtual environment is activated.
* Dependencies are installed using:

```bash
pip install -r requirements.txt
```

---

# 🎯 Future Improvements

* AI-powered resume rewriting
* ATS compatibility scoring
* Resume keyword optimization
* Cover letter generation
* Multiple resume comparison
* Job recommendation engine
* User authentication
* Resume history and analytics

---

# 📄 License

This project was created as part of an **Explainable Systems** engineering project for educational and demonstration purposes.