import re
from datetime import datetime
from typing import List, Optional

from app.services.jd_parser import extract_education, extract_skills


def _month_number(month_name: str) -> int:
    month_name = month_name[:3].lower()

    months = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    }

    return months.get(month_name, 1)


def _calculate_date_range_experience(text: str) -> float:
    current_date = datetime.now()
    total_months = 0

    pattern = re.compile(
        r"(?:(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|"
        r"jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|"
        r"oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?\s*)?"
        r"(\d{4})\s*"
        r"(?:-|–|to)\s*"
        r"(?:(present|current)|"
        r"(?:(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|"
        r"jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|"
        r"oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\.?\s*)?"
        r"(\d{4}))",
        re.IGNORECASE,
    )

    for match in pattern.finditer(text):
        start_month_name, start_year, ongoing, end_month_name, end_year = match.groups()

        start_year = int(start_year)
        start_month = _month_number(start_month_name) if start_month_name else 1

        if ongoing:
            end_year = current_date.year
            end_month = current_date.month
        else:
            end_year = int(end_year)
            end_month = _month_number(end_month_name) if end_month_name else 12

        if end_year >= start_year:
            months = (end_year - start_year) * 12 + (end_month - start_month) + 1
            total_months += max(months, 0)

    return round(total_months / 12, 1)


def extract_actual_experience(text: str) -> Optional[float]:
    normalized_text = text.lower()

    explicit_matches = re.findall(
        r"(\d+(?:\.\d+)?)\s*(?:\+|plus)?\s*(?:years?|yrs?)\s+(?:of\s+)?experience",
        normalized_text,
    )

    explicit_years = [float(value) for value in explicit_matches]
    date_range_years = _calculate_date_range_experience(text)

    if explicit_years or date_range_years > 0:
        return round(max(explicit_years + [date_range_years]), 1)

    return None


def parse_resume(resume_text: str) -> dict:
    return {
        "skills": extract_skills(resume_text),
        "actual_experience_years": extract_actual_experience(resume_text),
        "education": extract_education(resume_text),
    }