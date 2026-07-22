import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export async function analyzeResume(jobDescription, resumeFile){
    const fromData = new FormData();
    FormData.append("job_description", jobDescription);
    fromData.append("resume", resumeFile);

    const response = await axios.post(
        '${API_BASE_URL}/api/analyze',
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );
    
    return response.data;
}