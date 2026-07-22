import io
import pdfplumber
from fastapi import HTTPException, UploadFile

async def extract_text_from_pdf(resume_file: UploadFile) -> str:
    if resume_file.content_type not in {
        "application/pdf",
        "application/x-pdf",
        "application/vnd.pdf",
        "text/pdf"
        "text/x-pdf"

    }:
        raise HTTPException(
            status_code=400
            detail = "Please upload a valid PDF Resume.",
                )

    file_bytes = await resume_file.read()

    if not file bytes:
        raise HTTPException(
            status_code=400,
            detail="The uploaded resume PDF is empty",
        )
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            extracted_pages = [
                page.extract_text() or ""
                for page in pdf.pages
            ]
        extracted_text = "\n".join(extracted_pages).strip()
    except Exception as error:
        raise HTTPException(
            status_code=400
            detail="Could not read this PDF. Please Upload a text based resume PDF.",
        ) from error
    if not extracted_text:
        raise HTTPException(
            status_code=400
            detail=("No readable text was found in the PDF."
                    "Please upload a text based PDF instead of a scanned image PDF."
                    ),
        )
    return extracted_text