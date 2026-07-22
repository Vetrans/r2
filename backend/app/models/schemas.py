from typing import List, Optional
from pydantic import BaseModel, Field

class ExperienceDetails(BaseModel):
    required_years: Optional[float] = None
    actual_years: Optional[float] = None
    gap_years: Optional[float] = None
    status: str

class EducationDetails(BaseModel):
    required: List[str] = Field(default_factory=list)
    actual: List[str] = Field(default_factory=list)
    status: str

class ScoreBreakdown(BaseModel):
    skill_match_score: float
    relevance_score: float
    experience_score: float
    education_score: float

class AnalysisResponse(BaseModel):
    match_score: float
    verdict: str
    score_breakdown: ScoreBreakdown

    matched_skills: List[str] = Field(default_factory=list)
    missing_skills: List[str] = Field(default_factory=list)

    experience: ExperienceDetails
    education: EducationDetails

    rejection_reasons: List[str] = Field(default_factory=list)
    resume_fixes: List[str] = Field(default_factory=list)
    upskilling_suggestions: List[str] = Field(default_factory=list)

    resume_text_preview: str