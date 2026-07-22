from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


EDUCATION_LEVELS = {
    "diploma": 1,
    "associate degree": 2,
    "bachelor's degree": 3,
    "master's degree": 4,
    "phd": 5,
}


def _round_score(score: float) -> float:
    return round(max(0, min(100, score)), 1)


def calculate_relevance_score(jd_text: str, resume_text: str) -> float:
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        matrix = vectorizer.fit_transform([jd_text, resume_text])
        similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        return _round_score(similarity * 100)
    except ValueError:
        return 0.0


def compare_experience(required_years, actual_years) -> dict:
    if required_years is None:
        return {
            "required_years": None,
            "actual_years": actual_years,
            "gap_years": 0,
            "status": "Not specified in job description",
            "score": 100.0,
        }

    if actual_years is None:
        return {
            "required_years": required_years,
            "actual_years": 0,
            "gap_years": required_years,
            "status": "Experience not clearly found on resume",
            "score": 0.0,
        }

    gap = round(max(required_years - actual_years, 0), 1)

    if gap == 0:
        status = "Meets requirement"
        score = 100.0
    else:
        status = "Below requirement"
        score = _round_score((actual_years / required_years) * 100)

    return {
        "required_years": required_years,
        "actual_years": actual_years,
        "gap_years": gap,
        "status": status,
        "score": score,
    }


def compare_education(required_education: List[str], actual_education: List[str]) -> dict:
    if not required_education:
        return {
            "required": [],
            "actual": actual_education,
            "status": "Not specified in job description",
            "score": 100.0,
        }

    if not actual_education:
        return {
            "required": required_education,
            "actual": [],
            "status": "Education not clearly found on resume",
            "score": 0.0,
        }

    highest_required = max(EDUCATION_LEVELS[item] for item in required_education)
    highest_actual = max(EDUCATION_LEVELS[item] for item in actual_education)

    if highest_actual >= highest_required:
        status = "Meets requirement"
        score = 100.0
    else:
        status = "Below requirement"
        score = _round_score((highest_actual / highest_required) * 100)

    return {
        "required": required_education,
        "actual": actual_education,
        "status": status,
        "score": score,
    }


def determine_verdict(score: float) -> str:
    if score >= 80:
        return "Strong match"
    if score >= 60:
        return "Moderate match"
    if score >= 40:
        return "Partial match"
    return "Low match"


def analyze_match(jd_text: str, resume_text: str, jd_data: dict, resume_data: dict) -> dict:
    jd_skills = set(jd_data["skills"])
    resume_skills = set(resume_data["skills"])

    matched_skills = sorted(jd_skills.intersection(resume_skills), key=str.lower)
    missing_skills = sorted(jd_skills.difference(resume_skills), key=str.lower)

    skill_match_score = (
        _round_score((len(matched_skills) / len(jd_skills)) * 100)
        if jd_skills
        else 100.0
    )

    relevance_score = calculate_relevance_score(jd_text, resume_text)

    experience = compare_experience(
        jd_data["required_experience_years"],
        resume_data["actual_experience_years"],
    )

    education = compare_education(
        jd_data["required_education"],
        resume_data["education"],
    )

    final_score = _round_score(
        (skill_match_score * 0.45)
        + (relevance_score * 0.30)
        + (experience["score"] * 0.15)
        + (education["score"] * 0.10)
    )

    rejection_reasons = []

    if missing_skills:
        skill_list = ", ".join(missing_skills[:5])
        rejection_reasons.append(
            f"Your resume does not clearly mention {len(missing_skills)} job-required skill(s): {skill_list}."
        )

    if experience["status"] == "Below requirement":
        rejection_reasons.append(
            f"The role requests {experience['required_years']} years of experience, "
            f"while your resume shows about {experience['actual_years']} years."
        )
    elif experience["status"] == "Experience not clearly found on resume":
        rejection_reasons.append(
            "The job requires experience, but your total years of experience are not clearly stated on the resume."
        )

    if education["status"] == "Below requirement":
        rejection_reasons.append(
            "Your listed education appears below the qualification requested in the job description."
        )
    elif education["status"] == "Education not clearly found on resume":
        rejection_reasons.append(
            "The job requires education details, but a matching qualification was not clearly found on the resume."
        )

    if relevance_score < 35:
        rejection_reasons.append(
            "The overall wording and keywords in your resume have low relevance to this job description."
        )

    if not rejection_reasons:
        rejection_reasons.append(
            "No major requirement gaps were identified. Tailor your resume wording to mirror the job description before applying."
        )

    return {
        "match_score": final_score,
        "verdict": determine_verdict(final_score),
        "score_breakdown": {
            "skill_match_score": skill_match_score,
            "relevance_score": relevance_score,
            "experience_score": experience["score"],
            "education_score": education["score"],
        },
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "experience": {
            key: value for key, value in experience.items() if key != "score"
        },
        "education": {
            key: value for key, value in education.items() if key != "score"
        },
        "rejection_reasons": rejection_reasons[:4],
    }