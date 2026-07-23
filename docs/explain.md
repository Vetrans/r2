# ClearCall — Transparent Resume Analysis Through Explainable AI

> **"A score is only useful if people understand how it was calculated."**

---

# Project Overview

**ClearCall** is an explainable resume analysis platform that compares a candidate's resume against a job description and produces a detailed, transparent evaluation instead of a single opaque match percentage.

Most Applicant Tracking Systems (ATS) and automated hiring tools provide little or no explanation for their decisions. Candidates often receive rejection emails without knowing what skills were missing, whether they lacked sufficient experience, or if their resume simply failed to match the language used in the job description.

ClearCall was built to solve this transparency problem.

Instead of functioning as another black-box scoring system, ClearCall breaks every decision into understandable components. Every score shown to the user can be traced back to an explicit calculation, allowing users to understand not only **what** the result is, but also **why** they received it.

The application accepts only two inputs:

- A job description
- A resume (PDF)

From these two inputs, the system extracts structured information, compares both documents using deterministic algorithms, calculates weighted scores, generates human-readable explanations, and finally suggests concrete improvements that can increase the candidate's chances of matching similar roles in the future.

No user accounts are required, no resumes are permanently stored, and every analysis is performed independently for maximum privacy and simplicity.

---

# The Problem

Recruitment has become increasingly automated.

Today, companies receive hundreds or even thousands of applications for a single position. To manage this scale, organizations rely on Applicant Tracking Systems (ATS), keyword filters, and automated ranking algorithms to shortlist candidates before any human recruiter reviews their resumes.

While this significantly reduces manual effort, it introduces a major problem:

**Candidates rarely understand why they were rejected.**

Typical hiring platforms return outcomes such as:

- Application Rejected
- Not Selected
- Profile Doesn't Match
- Better Candidates Found

These responses provide almost no actionable information.

As a result, applicants are left wondering:

- Was my resume missing important skills?
- Did I fail because of insufficient experience?
- Was my education below the requirement?
- Did my resume formatting prevent proper parsing?
- Did my resume simply not resemble the job description closely enough?

Without clear explanations, improving future applications becomes largely a matter of guesswork.

This lack of transparency affects not only job seekers but also students entering the workforce for the first time. Many students have never seen how their resumes compare against real job descriptions and therefore struggle to identify which technical skills or experiences they should develop before applying.

The original project challenge summarized this issue in one simple sentence:

> **"Systems should explain themselves."**

That principle became the foundation of ClearCall.

---

# Our Solution

ClearCall transforms resume evaluation from a hidden scoring process into a fully explainable analysis.

Instead of presenting only a single percentage match, the platform produces a complete report that answers the questions candidates actually care about.

For every analysis, the system provides:

- Overall resume match score
- Individual score breakdowns
- Matched skills
- Missing skills
- Experience comparison
- Education comparison
- Human-readable rejection reasons
- Resume improvement suggestions
- Upskilling recommendations

Each section is generated from explicit calculations rather than hidden machine learning predictions.

This allows users to verify every result themselves.

For example, if the system reports a low skills score, users can immediately see which required skills were missing.

If the experience score is low, the report explains exactly how many years were required, how many were detected, and where the gap exists.

Rather than saying:

> "Your resume scored 58%."

ClearCall says:

> "Your resume scored 58% because only 6 of the 10 required skills were detected, your experience is approximately one year below the requirement, and your resume shares limited topical similarity with the job description."

This difference is what makes the platform explainable.

---

# Core Objectives

From the beginning of development, the project focused on five primary goals.

## 1. Transparency

Every score should be understandable.

Every calculation should be reproducible.

Every recommendation should have a visible reason.

Nothing should appear as unexplained magic.

---

## 2. Privacy

Many resume analysis platforms permanently store uploaded resumes.

ClearCall intentionally avoids this.

Every uploaded PDF is processed entirely in memory.

After the response is generated, no resume content is written to a database or stored on the server.

There are:

- No user accounts
- No login system
- No saved reports
- No permanent storage

Each request is completely independent.

---

## 3. Explainability

Instead of relying heavily on opaque AI models, ClearCall favors deterministic algorithms wherever possible.

Examples include:

- Regular expressions
- Keyword matching
- Rule-based comparisons
- Documented scoring formulas
- Fixed weighting system

This approach ensures that every decision can be inspected and verified.

---

## 4. Actionable Feedback

Finding problems is only half the job.

Users also need guidance on how to improve.

For every weakness identified, ClearCall generates practical recommendations such as:

- Learn missing technologies
- Add measurable project experience
- Improve resume structure
- Highlight relevant achievements
- Better align resume wording with the job description

The objective is improvement rather than simply evaluation.

---

## 5. Simplicity

The system intentionally avoids unnecessary complexity.

Instead of dozens of services, multiple databases, and hidden processing pipelines, the architecture consists of only two major components:

- React Frontend
- FastAPI Backend

This keeps deployment straightforward while making the entire project easier to understand and maintain.

---

# Key Features

## Explainable Resume Matching

Unlike traditional ATS platforms, ClearCall shows exactly how the final score is produced.

The report includes:

- Skills score
- Resume relevance score
- Experience score
- Education score
- Final weighted score

Each value is independently calculated and displayed.

---

## Automatic PDF Processing

Users simply upload their resume in PDF format.

The backend extracts all readable text directly from the document without requiring manual copy-pasting.

Processing occurs entirely in memory, ensuring user privacy.

---

## Skill Extraction

Both the resume and job description pass through the same extraction engine.

A curated vocabulary of technical and professional skills is searched using case-insensitive word-boundary matching.

Examples include:

- Python
- Java
- React
- Docker
- Kubernetes
- TensorFlow
- SQL
- Git
- AWS
- Azure
- Leadership
- Communication
- Agile
- Machine Learning

Using the same extraction logic for both documents guarantees fair comparison.

---

## Experience Detection

The platform identifies professional experience using two independent methods.

First, it searches for explicit statements such as:

- "3 years of experience"
- "5+ years"
- "Minimum 2 years"

If those are not available, it estimates experience by detecting employment date ranges like:

```
Jan 2021 – Present

March 2019 – August 2021

2018 – 2020
```

These date ranges are converted into total months of experience before being transformed into years.

---

## Education Comparison

Education requirements are extracted from both documents using multiple regular expression patterns.

Supported education levels include:

- Diploma
- Associate Degree
- Bachelor's Degree
- Master's Degree
- PhD

The system compares the highest education level found in each document and calculates a proportional score.

---

## Resume Relevance Analysis

Skills alone do not capture the complete similarity between two documents.

Two resumes may mention the same technologies while describing entirely different domains.

To address this, ClearCall computes overall document similarity using TF-IDF vectorization and cosine similarity.

This captures broader contextual overlap including:

- Domain terminology
- Project descriptions
- Technical vocabulary
- Professional language

The resulting relevance score complements keyword matching without replacing it.

---

## Human-Readable Explanations

Numbers alone are difficult to interpret.

Instead of forcing users to infer the meaning of scores, ClearCall converts analysis results into plain language.

Examples include:

- Four required skills were not found.
- Experience is approximately two years below the job requirement.
- Required education could not be detected.
- Resume wording has limited similarity with the job description.

These explanations connect numerical scores with understandable reasons.

---

## Personalized Improvement Plan

Every detected weakness is transformed into an actionable recommendation.

Suggestions are divided into two categories:

### Resume Improvements

Changes users can make immediately, such as:

- Add missing skills that genuinely reflect your experience.
- Improve the skills section.
- Clarify employment history.
- Include education details.
- Rewrite the professional summary.

### Upskilling Recommendations

Long-term improvements including:

- Learn missing technologies.
- Build portfolio projects.
- Complete relevant certifications.
- Gain practical experience through internships or open-source contributions.

By separating document improvements from career development, the platform helps users distinguish between presentation issues and actual skill gaps.

---

# Planned Features vs. Final Implementation

The original project proposal included several planned capabilities.

During development, priorities shifted toward building a robust explainability pipeline before expanding feature coverage.

The following table summarizes the implementation status.

| Feature                        | Status             |
| ------------------------------ | ------------------ |
| PDF Text Extraction            | ✅ Implemented     |
| Skill Extraction               | ✅ Implemented     |
| Experience Detection           | ✅ Implemented     |
| Education Detection            | ✅ Implemented     |
| Resume vs Job Comparison       | ✅ Implemented     |
| Weighted Match Score           | ✅ Implemented     |
| Explainable Rejection Reasons  | ✅ Implemented     |
| Resume Improvement Suggestions | ✅ Implemented     |
| Upskilling Recommendations     | ✅ Implemented     |
| Certificate Extraction         | ❌ Not Implemented |
| Dedicated Project Extraction   | ❌ Not Implemented |
| Cloud Deployment               | ⏳ Planned         |

Although certificate and project extraction were not implemented as standalone modules, the TF-IDF relevance engine partially compensates by recognizing broader topical similarity across entire documents rather than relying solely on explicit keyword detection.

The completed system therefore fully delivers the project's central objective: transforming opaque resume evaluation into a transparent, explainable process where every result can be understood, verified, and acted upon.

---

# System Architecture

ClearCall follows a simple two-tier architecture designed around separation of responsibilities.

Rather than mixing interface code with analysis logic, the application clearly divides presentation from computation.

```text
                    User
                      │
                      │
                      ▼
        Upload Resume + Job Description
                      │
                      ▼
             React Frontend (Vite)
                      │
         HTTP Multipart/Form Request
                      │
                      ▼
            FastAPI Backend (Python)
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 PDF Extraction   Job Parser     Resume Parser
      │               │                │
      └──────────────► Matcher Engine ◄┘
                      │
                      ▼
          Suggestions Generator
                      │
                      ▼
               JSON Response
                      │
                      ▼
          Interactive React Report
```

The frontend never performs resume analysis.

Its responsibility is limited to collecting user input, sending the request, and presenting the returned report.

All parsing, comparison, scoring, explanation generation, and recommendation logic resides entirely within the backend.

This architectural separation ensures consistency, simplifies maintenance, and guarantees that every calculation originates from a single source of truth.

# Complete Request Flow

Every resume analysis performed by ClearCall follows the same deterministic pipeline.

No hidden background processing occurs, and no previous analyses influence future results.

Each request starts with only two inputs:

- A job description entered by the user.
- A resume uploaded as a PDF.

From these inputs, the backend performs a sequence of independent processing steps before returning a structured JSON response.

The complete flow is illustrated below.

```text
Resume.pdf
        │
        ▼
Extract PDF Text
        │
        ▼
Parse Resume
        │
        ▼
Extract Skills
Extract Education
Extract Experience
        │
        │
Job Description
        │
        ▼
Parse Job Description
        │
        ▼
Extract Skills
Extract Education
Extract Required Experience
        │
        ▼
        Matcher Engine
        │
        ▼
Calculate Individual Scores
        │
        ▼
Generate Final Match Score
        │
        ▼
Generate Rejection Reasons
        │
        ▼
Generate Resume Suggestions
        │
        ▼
Return Analysis Response
```

Each stage has a clearly defined purpose, making the entire pipeline easy to inspect, debug, and extend.

---

# Backend Architecture

The backend is responsible for every analytical task performed by ClearCall.

It is built using **FastAPI**, exposing a single REST endpoint that accepts a resume and job description before returning a fully structured report.

Unlike many resume analysis platforms, the backend is completely stateless.

Every request begins with no prior knowledge and ends without storing any user data.

This design provides several advantages:

- Better user privacy
- Simpler deployment
- Predictable behavior
- Easier debugging
- Easier scalability

Since nothing is stored permanently, refreshing the application simply starts a new analysis.

---

# Backend Workflow

The backend can be divided into six major processing stages.

1. API Entry Point
2. PDF Extraction
3. Resume Parsing
4. Job Description Parsing
5. Matching Engine
6. Suggestion Generation

Each stage performs one specific task before passing structured data to the next stage.

---

# API Entry Point

The FastAPI application exposes a single primary endpoint.

```
POST /api/analyze
```

The endpoint accepts multipart form data containing:

| Field           | Type     |
| --------------- | -------- |
| resume          | PDF File |
| job_description | Text     |

Before any processing begins, the backend performs basic validation.

Validation checks include:

- Resume file exists
- Resume is a PDF
- Job description is not empty
- Job description exceeds the minimum required length

Invalid requests immediately return descriptive HTTP error responses.

This ensures users understand exactly why their request failed instead of receiving generic server errors.

---

# PDF Processing

After validation, the uploaded resume is passed to the PDF extraction service.

The system uses **pdfplumber** to read text directly from each page.

Unlike OCR-based systems, ClearCall reads the embedded text layer inside the PDF.

The process follows these steps:

1. Open uploaded PDF in memory.
2. Read every page.
3. Extract readable text.
4. Merge pages together.
5. Return a single text document.

Nothing is written to disk during this process.

This protects user privacy while improving processing speed.

---

## Why OCR Is Not Used

Many resumes are exported directly from word processors.

These PDFs already contain selectable text, making OCR unnecessary.

Using OCR would introduce:

- Longer processing time
- Additional dependencies
- Lower accuracy
- Harder debugging

Instead, ClearCall deliberately supports text-based PDFs only.

If a scanned image resume is uploaded, the backend clearly informs the user that no readable text could be extracted.

This behavior is intentional rather than being treated as an unexpected error.

---

# Resume Parsing

Once plain text has been extracted, the resume parser begins converting unstructured text into structured information.

The parser focuses on three categories:

- Skills
- Experience
- Education

Rather than attempting to understand every sentence semantically, the parser uses deterministic extraction rules that are transparent and easy to inspect.

The resulting structured object resembles:

```text
Resume

Skills:
Python
Docker
SQL
React

Experience:
3 Years

Education:
Bachelor's Degree
```

This structured representation is then passed to the matching engine.

---

# Job Description Parsing

The job description undergoes nearly identical processing.

The parser extracts:

- Required skills
- Required education
- Required experience

Using the same extraction logic for both documents ensures consistency.

For example, if "Docker" is recognized inside the resume, it will also be recognized inside the job description because both rely on the same extraction engine.

This eliminates discrepancies that could occur if two independent extraction methods were used.

---

# Skill Extraction

Skill extraction is one of the most important components of the system.

Instead of relying on a language model to guess technologies, ClearCall uses a curated vocabulary stored inside a JSON file.

The vocabulary currently contains approximately **230 technical and professional skills**.

Examples include:

Programming Languages

- Python
- Java
- C++
- JavaScript
- Go
- Rust

Frameworks

- React
- Angular
- Vue
- FastAPI
- Django
- Spring Boot

Cloud Platforms

- AWS
- Azure
- Google Cloud

Data Science

- TensorFlow
- PyTorch
- Pandas
- NumPy
- Scikit-Learn

Databases

- PostgreSQL
- MongoDB
- MySQL
- Redis

DevOps

- Docker
- Kubernetes
- Jenkins
- GitHub Actions

Professional Skills

- Leadership
- Agile
- Scrum
- Communication
- Stakeholder Management

Each skill is searched using case-insensitive regular expressions with strict word boundaries.

For example,

Searching for:

```
Go
```

will match

```
Go
```

but will not incorrectly match

```
Algorithm
```

Similarly,

```
R
```

does not match every word containing the letter "r."

This greatly reduces false positives while keeping extraction deterministic.

After scanning completes:

- Duplicate skills are removed.
- Skills are alphabetically sorted.
- Results become part of the structured profile.

---

# Why Rule-Based Extraction?

Many modern resume analyzers rely heavily on large language models.

Although powerful, these models often introduce uncertainty.

The same resume may produce different outputs across multiple runs.

ClearCall intentionally avoids that behavior.

Every extracted skill originates from a visible vocabulary.

Every match comes from a documented regular expression.

Every result can therefore be verified manually.

This design directly supports the project's explainability goal.

---

# Education Extraction

Education extraction follows a similar strategy.

Instead of looking for only one wording, multiple variations are recognized for every education level.

Examples include:

Bachelor's Degree

- Bachelor of Technology
- Bachelor of Engineering
- B.Tech
- B.E.
- Bachelor's
- Bachelor of Science

Master's Degree

- Master of Science
- MBA
- MCA
- M.Tech
- Master's

Doctorate

- PhD
- Ph.D.
- Doctorate

Associate Degree

- Associate Degree

Diploma

- Diploma

Because many resumes use abbreviations, supporting multiple patterns significantly improves detection accuracy.

The parser records every education level found.

Later, during comparison, only the highest detected level is used.

For example,

Resume

- Bachelor's Degree
- Master's Degree

Highest level:

Master's Degree

The same logic applies to the job description.

---

# Experience Detection

Experience is extracted differently from skills and education because years of experience may be written in several formats.

To improve robustness, ClearCall combines two independent detection strategies.

The higher value becomes the final detected experience.

---

## Method 1 — Explicit Experience Statements

The parser first searches for phrases such as:

```
3 years of experience

5+ years

Minimum 2 years

At least 4 years

7 years experience
```

These patterns are extracted directly using regular expressions.

This method is highly accurate whenever resumes explicitly mention total experience.

---

## Method 2 — Employment Date Ranges

Not every resume includes a sentence stating total years of experience.

Instead, candidates often list employment history.

Example:

```text
Software Engineer

January 2020 – Present

Backend Developer

March 2018 – December 2019
```

The parser detects these date ranges automatically.

Each employment period is converted into months.

All detected periods are added together.

Finally, total months are converted into years.

If one job runs from

January 2020

to

January 2023

the parser calculates:

```
36 months

≈ 3 years
```

If multiple employment periods exist, they are accumulated to estimate total professional experience.

When "Present" or "Current" appears, today's date is used as the ending point.

This approach allows the parser to estimate experience even when resumes never explicitly mention total years.

---

# Combining Both Methods

After both extraction strategies complete, the backend compares their outputs.

Example:

Explicit Statement

```
2 Years
```

Date Range Calculation

```
3.4 Years
```

Final Experience

```
3.4 Years
```

The larger value is selected because explicit summaries on resumes are sometimes outdated while employment history continues beyond that statement.

If neither method detects any usable information, experience is recorded as **Not Detected** instead of assuming zero years.

This distinction is important.

Zero years means:

> The candidate has no experience.

Not Detected means:

> The parser could not confidently determine experience from the resume.

Returning "Not Detected" prevents misleading conclusions and allows the frontend to display a more accurate explanation.

---

At this point, both the resume and the job description have been transformed from raw text into structured information.

The next stage is the **Matcher Engine**, where these extracted attributes are compared, individual scores are calculated, and the final explainable match score is produced.

# Matcher Engine

The Matcher Engine is the core of ClearCall.

Everything extracted from the resume and job description eventually flows into this component.

Its responsibility is not only to determine how well a resume matches a job description, but also to explain every part of that decision.

Rather than producing a single opaque percentage, the matcher independently evaluates multiple aspects of the candidate's profile before combining them into a weighted final score.

The comparison process consists of four major stages:

1. Skills Comparison
2. Resume Relevance
3. Experience Comparison
4. Education Comparison

Each stage produces its own score, explanation, and supporting information.

These individual scores are then combined into the final match score.

---

# Skills Comparison

Skills are the strongest indicator of compatibility between a candidate and a role.

For that reason, they receive the highest weight in the final scoring formula.

The comparison process is intentionally simple and transparent.

After parsing completes, the backend has two skill sets:

**Job Description Skills**

```text
Python
FastAPI
Docker
SQL
Git
```

**Resume Skills**

```text
Python
SQL
Git
React
```

The matcher performs two set operations.

Matched skills:

```text
Job Skills ∩ Resume Skills
```

Result:

```text
Python
SQL
Git
```

Missing skills:

```text
Job Skills − Resume Skills
```

Result:

```text
FastAPI
Docker
```

The skill score is calculated using a straightforward formula.

```text
Skill Score =
(Number of Matched Skills ÷ Number of Required Skills) × 100
```

Using the example above:

```text
Matched Skills = 3

Required Skills = 5

Skill Score = (3 ÷ 5) × 100 = 60%
```

If the job description contains no recognizable skills, the backend assigns a score of **100%** because there are no explicit skill requirements to evaluate.

This avoids unfairly penalizing candidates when the job description itself lacks structured technical information.

---

# Resume Relevance

Skills alone do not fully describe whether a candidate fits a role.

Consider these two resumes.

Resume A:

- Python
- SQL
- Git

Resume B:

- Python
- SQL
- Git
- Machine Learning
- TensorFlow
- Computer Vision

Suppose the job description is for a Backend Developer.

Although Resume B contains more technical skills, its primary focus is Machine Learning rather than backend engineering.

Simply counting keywords would incorrectly suggest that Resume B is the better match.

To address this limitation, ClearCall computes overall document similarity.

---

## TF-IDF Vectorization

The backend converts both documents into TF-IDF vectors.

TF-IDF (Term Frequency–Inverse Document Frequency) measures how important each word is within a document while reducing the influence of common words.

Words such as:

- the
- and
- with
- for

are ignored because they provide little useful information.

Instead, the algorithm focuses on meaningful technical vocabulary.

Examples include:

- Kubernetes
- REST API
- Microservices
- NLP
- TensorFlow
- PostgreSQL

Each document becomes a numerical vector representing the importance of its terms.

---

## Cosine Similarity

Once both vectors have been created, cosine similarity is calculated.

The similarity value ranges between:

```text
0.0 → Completely different

1.0 → Nearly identical
```

The backend converts this value into a percentage.

Example:

```text
Cosine Similarity = 0.82

Relevance Score = 82%
```

Unlike the skill comparison, TF-IDF captures broader contextual similarity.

It recognizes overlap in:

- Domain language
- Technical terminology
- Project descriptions
- Professional wording
- General subject matter

This allows resumes that naturally describe similar work to receive higher relevance scores even when they do not share every exact keyword.

---

# Experience Comparison

Experience comparison evaluates whether the candidate meets the years of experience requested by the employer.

The matcher compares:

- Required experience (Job Description)
- Detected experience (Resume)

Four scenarios are possible.

---

## Scenario 1

No experience requirement exists.

Example:

```text
Job Description

Experience:
Not Specified
```

Result:

```text
Experience Score = 100%

Status

No experience requirement specified.
```

The candidate should not lose marks because the employer never defined a requirement.

---

## Scenario 2

Experience requirement exists, but the resume does not clearly indicate experience.

Example:

Job Description

```text
3 Years Required
```

Resume

```text
Experience Not Detected
```

Result:

```text
Experience Score = 0%
```

Reason:

> Experience could not be clearly identified from the resume.

This encourages candidates to improve how employment history is presented.

---

## Scenario 3

Candidate satisfies the requirement.

Example:

```text
Required

3 Years

Detected

5 Years
```

Result:

```text
Experience Score = 100%
```

Status:

> Meets experience requirement.

No deductions are applied.

---

## Scenario 4

Candidate falls below the requirement.

Example:

```text
Required

5 Years

Detected

3 Years
```

The score becomes proportional.

Formula:

```text
Experience Score =
(Detected Experience ÷ Required Experience) × 100
```

Calculation:

```text
3 ÷ 5 × 100

= 60%
```

The report also calculates the gap.

```text
Gap

2 Years
```

This information is later reused when generating rejection reasons and resume improvement suggestions.

---

# Education Comparison

Education comparison follows the same philosophy.

Instead of checking for identical wording, the backend compares education levels using a simple hierarchy.

| Level             | Rank |
| ----------------- | ---: |
| Diploma           |    1 |
| Associate Degree  |    2 |
| Bachelor's Degree |    3 |
| Master's Degree   |    4 |
| PhD               |    5 |

The parser first determines the highest education level detected in both documents.

Example:

Resume

- Bachelor's Degree
- Master's Degree

Highest Level:

Master's Degree

Job Description

- Bachelor's Degree

Highest Level:

Bachelor's Degree

Since the resume exceeds the requirement, the candidate receives full marks.

If the candidate falls below the required education level, a proportional score is calculated.

Example:

Required:

Master's Degree

Detected:

Bachelor's Degree

Calculation:

```text
3 ÷ 4 × 100

= 75%
```

This approach rewards candidates who come close to meeting educational expectations while still distinguishing between different qualification levels.

If no education requirement exists inside the job description, the education score defaults to **100%**.

---

# Final Weighted Score

After calculating the four independent scores, the matcher combines them into one overall match score.

Each category contributes a fixed percentage.

| Component        | Weight | Purpose                                       |
| ---------------- | -----: | --------------------------------------------- |
| Skills           |    45% | Measures direct technical compatibility       |
| Resume Relevance |    30% | Measures overall similarity between documents |
| Experience       |    15% | Measures professional experience requirements |
| Education        |    10% | Measures educational qualification            |

The final score is calculated using the following formula.

```text
Final Score

=

(Skill Score × 0.45)

+

(Relevance Score × 0.30)

+

(Experience Score × 0.15)

+

(Education Score × 0.10)
```

Example:

| Component  | Score |
| ---------- | ----: |
| Skills     |    70 |
| Relevance  |    82 |
| Experience |   100 |
| Education  |   100 |

Calculation:

```text
(70 × 0.45)

+

(82 × 0.30)

+

(100 × 0.15)

+

(100 × 0.10)

=

81.1%
```

Rounded Result:

```text
81%
```

This weighted system ensures that technical skills have the greatest influence while still considering broader compatibility, experience, and educational background.

---

# Match Verdict

Numerical scores are useful but not always intuitive.

To make the report easier to understand, ClearCall converts the final percentage into a human-readable verdict.

| Score Range | Verdict        |
| ----------- | -------------- |
| 80–100      | Strong Match   |
| 60–79       | Moderate Match |
| 40–59       | Partial Match  |
| Below 40    | Low Match      |

This verdict appears prominently within the final report and is represented visually using a colored audit stamp.

The verdict does not replace the numerical score—it complements it.

---

# Rejection Reasons

One of the defining features of ClearCall is that it never returns a score without an explanation.

After the final score has been calculated, the matcher analyzes every comparison result and generates a list of human-readable reasons describing what reduced the score.

Possible explanations include:

- Missing required technical skills.
- Experience below the required level.
- Required education not detected.
- Resume wording has low similarity with the job description.
- Experience could not be clearly identified.
- Education details are missing or unclear.

For example, instead of displaying only:

```text
Match Score

58%
```

The report explains:

```text
Reasons

• Four required skills were not found.

• Experience is approximately two years below the requirement.

• Resume wording shares limited similarity with the job description.
```

These explanations are generated directly from the comparison results rather than written manually.

If every comparison succeeds and no significant weaknesses are detected, the backend still returns a helpful message encouraging candidates to tailor their resume for each application.

This guarantees that the report always contains meaningful feedback rather than leaving the explanation section empty.

---

# Suggestions Engine

Identifying weaknesses is valuable, but users also need practical guidance.

The Suggestions Engine transforms detected problems into actionable recommendations.

Unlike rejection reasons, which explain **why** the score was reduced, suggestions explain **how** to improve future results.

Suggestions are divided into two categories:

1. Resume Improvements
2. Upskilling Recommendations

This distinction helps users separate presentation issues from genuine skill gaps.

# Resume Improvement Suggestions

Resume improvements focus on changes that users can make directly to their resume without necessarily learning new skills.

These recommendations improve how existing qualifications are presented rather than changing the candidate's technical background.

Examples include:

- Add a dedicated technical skills section.
- Mention missing technologies if they genuinely reflect your experience.
- Include measurable project outcomes.
- Clarify employment history using consistent date formats.
- Add education details if they are missing.
- Rewrite the professional summary to better align with the job description.

For example, if the parser cannot detect work experience because employment dates are inconsistent, the recommendation might be:

> Clearly format your employment history using standard date ranges (e.g., Jan 2022 – Present) so experience can be identified more accurately.

Similarly, if required skills exist in projects but are not explicitly mentioned inside the skills section, the system encourages users to highlight them more clearly.

These improvements can often increase resume readability without requiring additional qualifications.

---

# Upskilling Recommendations

Some weaknesses cannot be solved simply by editing the resume.

If the comparison engine identifies genuine gaps between the candidate and the target role, ClearCall recommends longer-term improvements.

Examples include:

- Learn missing programming languages.
- Complete a course covering required technologies.
- Build portfolio projects demonstrating missing skills.
- Gain practical experience through internships.
- Contribute to open-source projects.
- Pursue relevant certifications.
- Improve domain-specific knowledge.

For example, if Docker and Kubernetes are required but missing, the system may recommend:

- Build a containerized application using Docker.
- Learn Kubernetes deployment fundamentals.
- Deploy a sample project to a cloud platform.

Recommendations are intentionally concise and limited in number to avoid overwhelming the user.

Instead of generating dozens of suggestions, ClearCall prioritizes the most impactful improvements.

---

# Response Structure

After all processing stages complete, the backend assembles a structured response.

Every response follows the same schema, ensuring the frontend always receives predictable data.

A simplified representation is shown below.

```text
Analysis Response

├── Match Score
├── Verdict
├── Score Breakdown
│   ├── Skills
│   ├── Relevance
│   ├── Experience
│   └── Education
├── Matched Skills
├── Missing Skills
├── Experience Details
├── Education Details
├── Rejection Reasons
├── Resume Improvements
├── Upskilling Suggestions
└── Resume Preview
```

Using a predefined schema provides several benefits:

- Consistent frontend rendering
- Easier debugging
- Automatic response validation
- Simplified future feature additions

FastAPI validates every outgoing response before sending it to the frontend, ensuring that malformed data cannot accidentally reach the user interface.

---

# Frontend Architecture

The frontend is built using **React** with **Vite**.

Its primary responsibility is presentation rather than analysis.

Every calculation, comparison, and recommendation originates from the backend.

The frontend simply:

1. Collects user input.
2. Sends the analysis request.
3. Displays the returned report.

Separating presentation from business logic makes the application easier to maintain while ensuring that all analytical decisions originate from one authoritative source.

---

# User Interface Flow

The application follows a straightforward single-page workflow.

```text
Open Application
        │
        ▼
Paste Job Description
        │
        ▼
Upload Resume PDF
        │
        ▼
Click Analyze
        │
        ▼
Loading Screen
        │
        ▼
Analysis Report
```

There are no multi-step forms, registration pages, or account dashboards.

The entire interaction is designed to remain simple and focused.

---

# Upload Form

The upload form serves as the entry point into the application.

Users provide:

- Job description
- Resume PDF

Before the request reaches the backend, the frontend performs lightweight validation.

Validation checks include:

- Resume selected
- PDF uploaded
- Job description length
- Empty input detection

Immediate validation improves user experience by preventing unnecessary API requests.

---

# API Layer

Communication between the frontend and backend occurs through a single API function.

The frontend constructs a multipart request containing:

```text
resume

job_description
```

This request is sent to the backend using Axios.

The backend processes the request before returning a structured JSON response.

The frontend never attempts to interpret or modify backend calculations.

Instead, it renders exactly what the backend returns.

This separation ensures that all analytical logic remains centralized.

---

# Loading State

Resume analysis requires several processing stages.

During this time, the frontend displays a loading component instead of leaving the page unresponsive.

This provides users with immediate feedback that processing is underway.

The loading interface disappears automatically when the response arrives.

---

# Results Dashboard

After analysis completes, the dashboard displays multiple independent report sections.

Each component corresponds to a specific part of the backend response.

These components contain presentation logic only.

They do not perform calculations.

---

## Match Score Card

The first section users see is the overall score.

It contains:

- Final match percentage
- Visual score gauge
- Match verdict
- Individual score breakdown

The score gauge provides an immediate overview while the breakdown explains how that score was constructed.

---

## Skills Comparison

The skills section displays two groups.

Matched Skills

```text
✓ Python

✓ SQL

✓ Git
```

Missing Skills

```text
✗ Docker

✗ Kubernetes

✗ FastAPI
```

Presenting both groups side by side allows users to quickly identify strengths and weaknesses.

---

## Experience Summary

The report compares:

- Required experience
- Detected experience
- Comparison result

Example:

```text
Required

3 Years

Detected

5 Years

Status

Requirement Met
```

or

```text
Required

5 Years

Detected

3 Years

Gap

2 Years
```

This information directly mirrors the backend calculations.

---

## Education Summary

Education comparison presents:

- Required education
- Detected education
- Match status

Examples include:

- Requirement Met
- Below Requirement
- Not Detected
- Not Specified

Keeping these categories explicit prevents users from misunderstanding the result.

---

## Rejection Reasons

Instead of displaying technical metrics, this section translates comparison results into natural language.

Example:

```text
Reasons

• Three required technologies are missing.

• Experience is below the requested level.

• Resume wording differs significantly from the job description.
```

This is often the most valuable section for candidates because it directly explains why their score decreased.

---

## Improvement Plan

The improvement plan is divided into two columns.

### Resume Improvements

Immediate document changes.

### Upskilling Suggestions

Long-term professional development.

Separating these categories helps candidates prioritize their next steps.

---

# Visual Design Philosophy

The interface was intentionally designed to resemble a professional audit report rather than a modern social media application.

The design language emphasizes clarity, trust, and transparency.

Key design characteristics include:

- Paper-inspired background
- High-contrast typography
- Minimal visual clutter
- Consistent spacing
- Structured information hierarchy

The goal is to encourage users to read and understand the report instead of merely glancing at a single percentage.

---

# Color System

Colors communicate meaning throughout the application.

| Color  | Meaning        |
| ------ | -------------- |
| Green  | Strong Match   |
| Amber  | Moderate Match |
| Orange | Partial Match  |
| Red    | Low Match      |

These colors are reused consistently across:

- Verdict badge
- Match gauge
- Skill indicators
- Report highlights

Using a consistent semantic color system improves readability while reducing cognitive load.

---

# Typography

Different typefaces serve different purposes.

- **Fraunces** is used for major headings.
- **Inter** is used for body text.
- **IBM Plex Mono** is used for labels, numerical values, and technical information.

Assigning distinct roles to typography improves visual hierarchy without requiring excessive styling.

---

# Why ClearCall Is Different

Many resume analysis tools focus solely on prediction.

They answer the question:

> "How likely is this resume to pass?"

ClearCall answers a different question:

> "Why did this resume receive this score?"

That distinction influences every design decision made throughout the project.

Instead of optimizing for hidden prediction accuracy alone, the system prioritizes explainability.

Every major component follows deterministic rules.

Every score has a documented formula.

Every recommendation originates from a specific comparison result.

Every explanation can be traced back to the extracted data.

This makes ClearCall not only an evaluation tool but also a learning tool.

Rather than simply judging candidates, it helps them understand how hiring requirements align with their current qualifications and what concrete steps they can take to improve future applications.

---

# Technology Stack

## Frontend

- React 19
- Vite
- Axios
- Recharts
- Plain CSS
- Google Fonts

## Backend

- FastAPI
- Uvicorn
- Pydantic
- pdfplumber
- scikit-learn
- python-multipart
- python-dotenv

## Algorithms

- Regular Expressions
- TF-IDF Vectorization
- Cosine Similarity
- Rule-Based Parsing
- Weighted Scoring

## Data Storage

None.

The application is intentionally stateless.

No databases, user accounts, or persistent storage are used.

This design keeps deployment simple while preserving user privacy.

---

# End-to-End Summary

From the moment a user uploads a resume until the final report appears, every stage of ClearCall follows a transparent and deterministic workflow.

The system extracts readable text from the uploaded PDF, identifies skills, education, and experience from both the resume and the job description, compares each category independently, computes weighted scores using documented formulas, generates human-readable explanations, and finally produces personalized suggestions for improvement.

At no point does the platform rely on hidden decision-making or unexplained predictions.

Every result shown to the user can be traced back to a specific extraction rule, comparison method, or scoring calculation.

This commitment to transparency is the defining principle of ClearCall.

Rather than replacing human judgment, ClearCall provides an understandable framework for evaluating resume compatibility—helping candidates identify skill gaps, improve resume quality, and better prepare for future opportunities while ensuring that every automated decision remains visible, explainable, and actionable.
