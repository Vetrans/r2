function ImprovementPlan({ resumeFixes, upskillingSuggestions }) {
    return (
        <section className="result-card improvement-card">
            <p className="eyebrow">Your action plan</p>
            <h2>Improve the application before you apply</h2>

            <div className="plan-grid">
                <div className="plan-coloumn">
                    <h3>Resume fixes</h3>
                    <ul>
                        {resumeFixes.map((fix) => (
                            <li key={fix}">{fix}</li>
                        )
                            )}
                    </ul>
                </div>

                <div className="plan-coloumn">
                            <h3>Upskilling suggestions</h3>
                            <ul>
                                {upskillingSuggestions.map((suggestion) =>(
                                    <li key={suggestion}>{suggestion}</li>
                                ))}
                            </ul>
                </div>
            </div>
        </section> 
    );
}

export default ImprovementPlan;