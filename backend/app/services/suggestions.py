def generate_suggestions(analysis: dict) -> dict:
    resume_fixes = []
    upskilling_suggestions = []

    missing_skills = analysis["missing_skills"]
    experience = analysis["experience"]
    education = analysis["education"]
    relevance_score = analysis["score_breakdown"]["relevance_score"]

    if missing_skills:
        skills_to_add = ", ".join(missing_skills[:5])
        resume_fixes.append(
            f"Add relevant, truthful evidence of these skills where you have used them: {skills_to_add}."
        )
        resume_fixes.append(
            "Create a dedicated Skills section near the top of your resume using wording that matches the job description."
        )

        for skill in missing_skills[:5]:
            upskilling_suggestions.append(
                f"Build a small practical project or complete a focused course in {skill}."
            )

    if experience["status"] == "Below requirement":
        resume_fixes.append(
            "Make your work history easier to scan: include dates, job titles, measurable achievements, and relevant projects."
        )
        upskilling_suggestions.append(
            "Gain relevant hands-on experience through internships, freelance projects, open-source work, or portfolio projects."
        )

    if experience["status"] == "Experience not clearly found on resume":
        resume_fixes.append(
            "Add a short professional summary that clearly states your total relevant experience in years."
        )

    if education["status"] == "Education not clearly found on resume":
        resume_fixes.append(
            "Add an Education section with your degree, institution, graduation year, and relevant coursework or certifications."
        )

    if education["status"] == "Below requirement":
        upskilling_suggestions.append(
            "Consider a relevant certification, diploma, or degree pathway that closes the education requirement gap."
        )

    if relevance_score < 35:
        resume_fixes.append(
            "Rewrite your professional summary and recent project bullets to use the role's most relevant keywords naturally."
        )

    if not resume_fixes:
        resume_fixes.append(
            "Tailor your summary and project bullets to the exact responsibilities and terminology used in this job description."
        )

    if not upskilling_suggestions:
        upskilling_suggestions.append(
            "Deepen your strongest job-relevant skills with one portfolio project that demonstrates measurable impact."
        )

    return {
        "resume_fixes": resume_fixes[:5],
        "upskilling_suggestions": upskilling_suggestions[:5],
    }