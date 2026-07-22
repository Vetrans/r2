import { useRef } from "react";

function UploadForm({
    jobDescription,
    onJobDescriptionChange,
    resumeFile,
    onResumeFileChange,
    onSubmit,
    loading,
}) {
    const fileInputRef = useRef(null);

    function handleFileChange(event) {
        const selectedFile = event.target.files?.[0];

        if (!selectedFile) {
            return;
        }

        if (selectedFile.type !== "application/pdf") {
            alert("Please select a PDF resume");
            event.target.value = "";
            return;
        }

        onResumeFileChange(selectedFile);
    }

    function removeFile() {
        onResumeFileChange(null);

        if (fileInputRef.current) {
            fileInputRef.current.value = "";
        }
    }

    return (
        <form className="upload-form" onSubmit={onSubmit}>
            <div className="form-group">
                <label htmlFor="job-description">Job Description</label>
                <textarea
                    id="job-description"
                    value={jobDescription}
                    onChange={(event) => onJobDescriptionChange(event.target.value)}
                    placeholder="Paste the complete job description here..."
                    rows="11"
                    disabled={loading}
                    required
                />
            </div>

            <div className="form-group">
                <label htmlFor="resume"> Resume PDF </label>

                <label className="file-upload" htmlFor="resume">
                    <span className="upload-icon">↑</span>
                    <span>
                        <strong>Choose your resume PDF</strong>
                        <small>Only text based PDF files are supported</small>
                    </span>
                </label>

                <input
                    ref={fileInputRef}
                    id="resume"
                    type="file"
                    accept=".pdf,application/pdf"
                    onChange={handleFileChange}
                    disabled={loading}
                    required={!resumeFile}
                />

                {resumeFile && (
                    <div className="selected-file">
                        <span>{resumeFile.name}</span>
                        <button type="button" onClick={removeFile} disabled={loading}>
                            Remove
                        </button>
                    </div>
                )}
            </div>

            <button className="primary-button" type="submit" disabled={loading}>
                {loading ? "Analyzing..." : "Analyze My Resume"}
            </button>
        </form>
    );
}

export default UploadForm;