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
    match_score