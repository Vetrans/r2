import { Cell, Pie, PieChart, ResponsiveContainer } from "recharts";

const TONE_COLORS = {
    "stamp-strong": "#2E6E49",
    "stamp-moderate": "#B8801F",
    "stamp-partial": "#C2790E",
    "stamp-low": "#B23A2E",
};

function getStampTone(score) {
    if (score >= 80) return "stamp-strong";
    if (score >= 60) return "stamp-moderate";
    if (score >= 40) return "stamp-partial";
    return "stamp-low";
}

function MatchScoreGauge({ score, verdict, scoreBreakdown }) {
    const remainingScore = Math.max(0, 100 - score);
    const stampTone = getStampTone(score);

    const gaugeData = [
        { name: "Match score", value: score },
        { name: "Remaining", value: remainingScore },
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
                <div className={`verdict-stamp ${stampTone}`}>
                    <span>{verdict}</span>
                </div>
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
                            <Cell fill={TONE_COLORS[stampTone]} />
                            <Cell fill="#E4E6EC" />
                        </Pie>
                    </PieChart>
                </ResponsiveContainer>

                <div className="gauge-label">
                    <strong>{score}%</strong>
                    <span>Match score</span>
                </div>
            </div>

            <div className="score-breakdown">
                {breakdownItems.map(([label, value]) => (
                    <div className="breakdown-row" key={label}>
                        <div className="breakdown-label">
                            <span>{label}</span>
                            <strong>{value}%</strong>
                        </div>
                        <div className="progress-track">
                            <div
                                className="progress-fill"
                                style={{ width: `${value}%` }}
                            />
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
}

export default MatchScoreGauge;