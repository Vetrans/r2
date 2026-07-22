function RejectionReasons({reasons}) {
    return (
        <section>
            <p className="eyebrow">Explainable decision</p>
            <h2>Why this application may be rejected</h2>

            <ol className="reason-list">
                {reasons.map((reason, index)=> (
                    <li key={reason}>
                        <span className="reason-number">{index + 1}</span>
                        <p>{reason}</p>
                    </li>
                ))}
            </ol>
        </section>
    );
}

export default RejectionReasons;