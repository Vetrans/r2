import json
import re
from pathlib import Path
from typing import List, Optional

SKILLS_FILE = Path(__file__).resolve().parent.parent / "data" / "skills_list.json"

EDUCATION PATTERNS = {
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

    patterns = [

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