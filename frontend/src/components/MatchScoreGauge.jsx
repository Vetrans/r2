import {Cell, Pie, PieChart, ResponsiveContainer } from "recharts";

function MatchScoreGauge({ score, verdict, scoreBreakdown }){
    const remainingScore = Math.max(0, 100 - score);

    const gaugeData = [
        {name: "Match score", value: score},
        {name: "Remaining", value: remainingScore},
    ];

    const breakdownItems = [
        ["Skills", scoreBreakdown.skill_match_score],
        ["Relevance", scoreBreakdown.relevance_score],
        ["Experience", scoreBreakdown.experience_score],
        ["Education", scoreBreakdown.education_score],
    ];

    return (
        <section className="result-card score-card">
            <div>
                <p className="eyebrow"> Overall Application </p>
                <h2>{verdict}</h2>
                <p className="muted-text">
                    A transparent estimate based on skills, relevance, experience and education.
                </p>
            </div>

            <div className="gauge-wrapper">
                <ResponsiveContainer width="100%" height={230}>
                    <PieChart>
                        <Pie 
                            data={gaugeData}
                            dataKey="value"
                            cx="50%"
                            cy="50%"
                            innerRadius={72}
                            outerRadius={95}
                            startAngle={90}
                            endAngle={-270}
                            stroke="none"
                            >
                                <Cell fill="#5b5ce2"/>
                                <Cell fill="#e8e9f3"/>
                        </Pie>
                    </PieChart>
                </ResponsiveContainer>

                <div className="gague-label">
                    <strong>{score}%</strong>
                    <span>Match score</span>
                </div>
            </div>

            <div className="score-breakdown">
                {breakdownItems.map(([Label, value])=> (
                    <div className="breakdown-row" key={label}>
                        <div className="breakdown-label">
                            <span>{label}</span>
                            <strong>{value}%</strong>
                        </div>
                        <div className="progress-track">
                            <div className="progress-fil" style={{width: '${value}%'}} />
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
}

export default MatchScoreGauge;