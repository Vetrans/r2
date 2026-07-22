import re
from datetime import datetime
from typing import List, Optional
from app.services.jd_parser import extract_education, extract_skills

def _month_number(month_name: str) -> int:
    month_name = month_name[:3].lower()

    month = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    return months.get(month_name, 1)

def _calculate_data_range_experience(text:str) -> float:
    current_date = datetime.now()
    total_months = 0

    *pattern = re.compile(
        r"",
        r"",
        r"",
        r"",
        r"",
        r"",
        r"",
        r"",
        r"",
        r"",
        re.IGNORECASE,
    )

    for match in pattern.finditer(text):
        start_month_name, start_year, onging, end_month_name