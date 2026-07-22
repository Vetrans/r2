function Loader() {
    return (
        <div className="loader-container" aria-live="polite">
            <div className="spinner" />
            <h2>Compiling your case file</h2>
            <p>
                Cross-referencing your resume against the role's requirements and
                drafting an explainable verdict.
            </p>
        </div>
    );
}

export default Loader;