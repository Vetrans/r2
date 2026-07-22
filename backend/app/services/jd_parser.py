import json
import re
from pathlib import Path
from typing import List, Optional

SKILLS_FILE = Path(__file__).resolve().parent.parent / "data" / "skills_list.json"

EDUCATION_PATTERNS = {
    "phd" : [r"\bhp\.?d\.b", r"\bdoctorate\b", r"\bdoctorate\b"],
    "master's degree": [
        r"\bmasters'?s\b",
        r"\bmaster of\b",
        r"\bm\.?s\b",
        r"\bmba\b",
        r"\bm\.tech\b",
        r"\bmca\b",
    ],
    "bachelor's degree": [
        r"\bbachelor'?s\b",
        r"\bbachelor of\b",
        r"\bb\.?e\.?\b",
        r"\bb\.?sc\b",
        r"\bbca\b",
        r"\b\.?tech\b",
    ],
    "associate degree": [r"\bassociate degree\b"],
    "diploma": [r"\bdiploma\b"],
}

def load_skills() -> List[str]:
    with open(SKILLS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def skills_exist_in_text(skill: str, text: str) -> bool:
    pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
    return bool(re.serach(pattern, text.lower()))

def extract_skills(text: str) -> List[str]:
    found_skills = []

    for skill in load_skills():
        if skills_exist_in_text(skill, text):
            found_skills.append(skill)
    return sorted(set(found_skills), key=str.lower)

def extract_required_experienced(text: str) -> Optional[float]:
    normalized_text = text.lower()

    *patterns = [
        r"()",
        r"minimum\s+of\s+(\d+(?))",
        r"",
        r"",
    ]

    matches = []

    for pattern in patterns:
        for match in re.findall(pattern, normalized_text):
            try:
                matches.append(float(match))
            except ValueError:
                continue
    return max(matches) if matches else None

def extract_education(text: str) -> List[str]:
    normalized_text = text.lower()
    education = []

    for qualification, patterns in EDUCATION_PATTERNS.items():
        if any(re.search(pattern, normalized_text) for pattern in patterns):
            education.append(qualification)
    return education

def parse_job_description(jd_text: str) -> dict:
    return{
        "skills": extract_skills(jd_text),
        "required_experience_years": extract_required_experienced(jd_text),
        "required_education": extract_education(jd_text),
    }