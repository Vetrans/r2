Engineer-01: "System SHould Explain themselves"

Problem Statement -> Modern software is becoming too complex to understand.

Goal

Build a system that makes its own behavior, decisions, or failures easy to understand.



Main Problem to Work on: 
    Job Application rejection based on resume
    Student not getting shortlisted based on resume

THE IDEA ->
The platform would tell what improvements are too be made in resume and as well as what should we do in terms of upskilling to get up to the mark

it would tell the user what would get them rejected

INPUT FLOW:-
    User gives ->
                    JD
                    RESUME
    Backend Process:-
    Step 1:-
       1. Extract text from resume PDF (pdfplumber)
       2. Extract skills
       3. Extract Years of experience
       4. Extract Education
       5. Extract Certificates
       6. Extract Projects/keywords relevant to domain
    Step 2:-
       1. Parse the JD text
       2. Same Extraction logic for required skills, experience level, education
    Step 3:-
       1. Comapre Resume vs JD (Core Engine)
    Step 4:-
       1. generate explanation output
    Step 5:-
       1. Frontend Visualizes Match score
       2. Matched vs Missing Skills
       3. Reasons for Rejection

Why am i Building this:-
    People can understand what and where they are going wrong and where they can improve 

