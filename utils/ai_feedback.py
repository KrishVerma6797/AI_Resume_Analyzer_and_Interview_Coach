import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def gen_feedback(resume_text,jd_text):
    prompt = f"""
    Analyze this resume against the job description in very concise form in pointers.

    Give:

    1. ATS Feedback
    2. Strengths
    3. Weaknesses
    4. Missing Skills
    5. Resume Improvement Suggestions
    6. Interview Preparation Tips

    Resume:
    {resume_text}

    Job Description:
    {jd_text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating feedback: {str(e)}"
