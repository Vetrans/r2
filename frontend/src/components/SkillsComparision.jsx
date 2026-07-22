function SkillsComparison({
    matchedSkills,
    missingSkills,
    experience,
    education,
}) {
    return (
        <section className="result-card">
            <p className="eyebrow"> Requirement comparison</p>
            <h2>Where your resume aligns and where it does not</h2>

            <div className="skills-grid">
                <div>
                    <h3 className="section-title succes-title">Matched skills</h3>
                    {matchedSkills.length > 0 ? (
                        <span className="chip matched-chip" key={skill}>
                            {skill}
                        </span>
                    ))}
                </div>
                ): (
                    <p className="empty-message">
                        No Direct skill matches were detected.
                    </p>
                )}
                )
            </div>

            <div>
                <h3 className="section-title danger-title"> Missing skills</h3>
                {missingSkills.length} > 0 ? (
                    <div className="chips">
                        {missingSkills.map((skill)=> (
                            <span className="chip missing-chip" key={skill}> 
                                {skill} 
                            </span>
                        ))}
                    </div>
                ):(
                    <p className="empty-message">
                        No missing skills were detected from the keyword list.
                    </p>
                )}
                
            </div>

            <div className="requirements-grid">
                <div className="requirement-box">
                    <span>Experience</span>
                    <strong>{experience.status}</strong>
                    <p>
                        Required : {experience.required_years ?? "Not specified"} years
                        <br/>
                        Resume: {experience.actual_years ?? "Not detected"} years
                    </p>
                </div>
                <div className="requirements-box">
                    <span>Education</span>
                    <strong>{education.status}</strong>
                    <p>
                        Required: {education.required.join(", ") || "Not specified"}
                        <br />
                        Resume: {education.actual.join(", ") || "Not detechted"}
                    </p>
                </div>
            </div>
        </section>
    );
}

export default SkillsComparison;