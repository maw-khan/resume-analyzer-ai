import streamlit as st
import os
from dotenv import load_dotenv

from utils.resume_parser import extract_resume_text
from utils.jd_parser import clean_job_description
from utils.scorer import calculate_match_score
from utils.feedback_generator import generate_feedback


# =====================
# CONFIG
# =====================

st.set_page_config(
    page_title="Resume Analyzer AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.markdown("Upload resume and job description to get ATS analysis")


# =====================
# ENV
# =====================

load_dotenv()

GOOGLE_API_KEY = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password"
)

if GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# =====================
# INPUTS
# =====================

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)


# =====================
# PROCESS BUTTON
# =====================

if st.button("Analyze Resume"):

    if not resume_file or not job_description:
        st.warning("Please upload resume and job description")

    else:

        with st.spinner("Analyzing..."):

            # Extract resume
            resume_text = extract_resume_text(resume_file)

            # Clean JD
            jd_text = clean_job_description(job_description)

            # Score
            score, matched, missing = calculate_match_score(
                resume_text,
                jd_text
            )

            # AI feedback
            feedback = generate_feedback(
                resume_text,
                jd_text,
                score,
                missing
            )


        # =====================
        # OUTPUT UI
        # =====================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📊 Match Score")
            st.metric("ATS Score", f"{score}%")

            st.subheader("✅ Matched Skills")
            st.write(list(matched))

            st.subheader("❌ Missing Skills")
            st.write(list(missing))


        with col2:

            st.subheader("🧠 AI Feedback")
            st.write(feedback)
