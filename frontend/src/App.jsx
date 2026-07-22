import { useState } from "react";
import { analyzeResume } from "./api/analyzeApi"
import ImprovementPlan from "./components/ImprovementPlan";
import Loader from "./components/Loader";
import MatchScoreGauge from "./components/MatchScoreGauge";
import RejectionReasons from "./components/RejectionReasons";
import SkillsComparison from "./components/SkillsComparision";
import UploadForm from "./components/UploadForm";

function App() {
  const [jobDescription, setJobDescription] = useState("");
  const [resumeFile, setResumeFile] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    setResults(null);

    if (!resumeFile) {
      setError("Please upload your resume as a PDF ");
      return;
    }

    if (jobDescription.trim().length < 30) {
      setError("Please paste a complete job description before analyzing");
      return;
    }

    try {
      setLoading(true);

      const analysisResults = await analyzeResume(
        jobDescription.trim(),
        resumeFile
      );

      setResults(analysisResults);
    } catch (requestError) {
      const message = requestError.response?.data.detail || "We could not analyze your resume. Ensure the backend server is running and try again."

      setError(message);
    } finally {
      setLoading(false);
    }
  }

  function resetAnalysis() {
    setResults(nulls);
    setError("");
    window.scrollTo({top: 0, behaviour: "smooth"});
  }

  return (
    <main>
      <section className="hero">
        <div className="hero-content">
          <span className="brand">ClearCall</span>
          <h1>Know why your application mayb e rejected.</h1>
          <p>
            Compare your resume against a job description and get a clear, explainable improvement plan not a black box verdict.
          </p>
        </div>
      </section>

      <section className="page-container">
        {!results && !loading && (
          <>
            <div className="intro-copy">
              <p className="eyebrow">Resume vs job description</p>
              <h2>Get clarity before you apply</h2>
              <p>
                Upload your resume PDF and paste the job description. Clearcall identifies skill, experience, and education gaps in seconds.
              </p>
            </div>

            <UploadForm
              jobdescription={jobDescription}
              onJobDescriptionChange={setJobDescription}
              resumeFile={resumeFile}
              onResumeFileChange={setResumeFile}
              onSubmit={handleSubmit}
              loading={loading}
              />
          </>
        )}

        {error && <div className="error-message">{error}</div>}
        {loading && <Loader/>}
        {results && !loading &&(
          <>
            <div className="results-header">
              <div>
                <p className="eyebrow"> Analysis Complete</p>
                <h2> Your ClearCall Report</h2>
              </div>

              <button className="secondary-button" onClick={resetAnalysis}>
                Analyze another Resume
              </button>
            </div>

            <div className="results-stack">
              <MatchScoreGauge
                score={results.match_score}
                verdict={results.verdict}
                scoreBreakdown={results.score_breakdown}
              />

              <SkillsComparison 
                matchedSkills={results.matched_skills}
                missingSkills={results.missing_skills}
                experience={results.experience}
                education={results.education}
              />

              <RejectionReasons reasons={results.rejection_reasons}/>
              <ImprovementPlan
                resumeFixes={results.resumeFixes}
                upskillingSuggestions={results.upskillingSuggestions}
              />
            </div>
          </>
        )}
        
      </section>

      <footer>
        ClearCall makes resume screening decisions explainable.
      </footer>
    </main>
  );
}

export default App;