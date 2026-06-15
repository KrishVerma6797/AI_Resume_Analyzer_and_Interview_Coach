import streamlit as st
import pdfplumber as pp

from utils.skills_extractor import extract_skills
from utils.ats_score import (
    ats_score,
    keyword_match,
    missing_skills,
    suggestions
)
from utils.semantic_match import semantic_match
from utils.interview_ques import get_ques
from utils.ai_feedback import gen_feedback


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("📌 Project Info")

    st.write(
        "AI Resume Analyzer & Interview Coach"
    )

    st.write("### Features")

    st.write("✅ ATS Score")
    st.write("✅ JD Match")
    st.write("✅ Semantic Match")
    st.write("✅ Missing Skills")
    st.write("✅ Interview Questions")
    st.write("✅ AI Feedback")

# ---------------- TITLE ---------------- #

st.title("🚀 AI Resume Analyzer & Interview Coach")

st.markdown(
    """
    Upload your resume, compare it with a Job Description,
    and get AI-powered feedback and interview preparation.
    """
)

# ---------------- JD INPUT ---------------- #

jd_description = st.text_area(
    "📋 Paste Job Description",
    height=200
)

jd_skills = extract_skills(jd_description)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📄 Upload Resume PDF",
    type=["pdf"]
)

# ---------------- MAIN LOGIC ---------------- #

if uploaded_file is not None:

    text = ""

    with pp.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    # ---------------- SKILL EXTRACTION ---------------- #

    skills = extract_skills(text)

    ats = ats_score(skills, text)

    jd_match_score = keyword_match(
        jd_skills,
        skills
    )

    missed_skills = missing_skills(
        jd_skills,
        skills
    )

    resume_suggestions = suggestions(
        skills,
        text
    )

    # ---------------- SEMANTIC MATCH ---------------- #

    se_match = 0

    if jd_description:

        se_match = semantic_match(
            text,
            jd_description
        )

    # ---------------- SCORE CARDS ---------------- #

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{ats}/100"
        )

    with col2:
        st.metric(
            "JD Match",
            f"{jd_match_score:.2f}%"
        )

    with col3:
        st.metric(
            "Semantic Match",
            f"{se_match:.2f}%"
        )

    st.progress(min(int(ats), 100))

    # ---------------- TABS ---------------- #

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 Analysis",
            "🛠 Skills",
            "🎯 Interview Questions",
            "🤖 AI Feedback"
        ]
    )

    # ---------------- ANALYSIS TAB ---------------- #

    with tab1:

        with st.expander(
            "📄 View Extracted Resume Text"
        ):

            st.text_area(
                "",
                value=text,
                height=350
            )

    # ---------------- SKILLS TAB ---------------- #

    with tab2:

        st.subheader("Detected Skills")

        col1, col2 = st.columns(2)

        for i, skill in enumerate(skills):

            if i % 2 == 0:
                col1.success(skill.title())
            else:
                col2.success(skill.title())

        st.subheader("Missing Skills")

        if len(missed_skills) == 0:

            st.success(
                "No missing skills detected."
            )

        else:

            for skill in missed_skills:
                st.error(skill.title())
        
        st.subheader("Resume Suggestions")

        for s in resume_suggestions:
            st.warning(s)

    # ---------------- INTERVIEW TAB ---------------- #

    with tab3:

        interview_questions = get_ques(
            skills
        )

        if len(interview_questions) == 0:

            st.info(
                "No interview questions available."
            )

        else:

            for ques in interview_questions:
                st.info(ques)

    # ---------------- AI FEEDBACK TAB ---------------- #

    with tab4:

        st.write(
            "Generate AI-powered feedback using Gemini."
        )

        if st.button(
            "🚀 Generate AI Feedback"
        ):

            if not jd_description:

                st.warning(
                    "Please enter a Job Description first."
                )

            else:

                with st.spinner(
                    "Analyzing Resume..."
                ):

                    feedback = gen_feedback(
                        text,
                        jd_description
                    )

                st.markdown(feedback)
