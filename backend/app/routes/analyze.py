from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from app.models.schemas import AnalysisResponse
from app.services.jd_parser import parse_job_description
from app.services.matcher import analyze_match
from app.services.pdf_extractor import extract_text_from_pdf
from app.services.resume_parser import parse_resume
from app.services.suggestions import generate_suggestions

router = APIRouter(prefix="/api", tags=["analysis"])


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(
    job_description: str = Form(...),
    resume: UploadFile = File(...),
):
    cleaned_jd = job_description.strip()

    if len(cleaned_jd) < 30:
        raise HTTPException(
            status_code=400,
            detail="Please provide a more detailed job description.",
        )

    resume_text = await extract_text_from_pdf(resume)

    jd_data = parse_job_description(cleaned_jd)
    resume_data = parse_resume(resume_text)

    analysis = analyze_match(
        jd_text=cleaned_jd,
        resume_text=resume_text,
        jd_data=jd_data,
        resume_data=resume_data,
    )

    suggestions = generate_suggestions(analysis)
    analysis.update(suggestions)
    analysis["resume_text_preview"] = resume_text[:500].replace("\n", " ")

    return analysis