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

st.sidebar.title("⚙ Settings")

GOOGLE_API_KEY = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password",
    help="Your API key is never stored."
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
This AI tool analyzes resumes against
job descriptions using ATS-style scoring
and Gemini AI feedback.
"""
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

    # CHECK API KEY
    if not GOOGLE_API_KEY:

        st.warning(
            "Please enter your Gemini API Key in the sidebar."
        )

    # CHECK RESUME
    elif not resume_file:

        st.warning(
            "Please upload a resume PDF."
        )

    # CHECK JOB DESCRIPTION
    elif not job_description.strip():

        st.warning(
            "Please paste a job description."
        )

    else:
        try:

            with st.spinner("Analyzing Resume..."):

                # Extract resume text
                resume_text = extract_resume_text(
                    resume_file
                )
        
                # Clean job description
                jd_text = clean_job_description(
                    job_description
                )
        
                # Calculate ATS score
                score, matched, missing = calculate_match_score(
                    resume_text,
                    jd_text
                )
        
                # Generate AI feedback
                feedback = generate_feedback(
                    resume_text,
                    jd_text,
                    score,
                    missing
                )

        except Exception as e:

            st.error(
                f"An error occurred: {str(e)}"
            )
        
            st.stop()


        # =====================
        # OUTPUT UI
        # =====================

        # =====================
        # MATCH SCORE
        # =====================
        
        st.subheader("📊 ATS Match Score")
        
        if score >= 75:
        
            st.success(
                f"✅ ATS Match Score: {score}%"
            )
        
        elif score >= 50:
        
            st.warning(
                f"⚠ ATS Match Score: {score}%"
            )
        
        else:
        
            st.error(
                f"❌ ATS Match Score: {score}%"
            )
        
        
        # =====================
        # MATCHED SKILLS
        # =====================
        
        st.subheader("✅ Matching Skills")
        
        if matched:
        
            st.write(
                ", ".join(matched[:20])
            )
        
        else:
        
            st.info(
                "No strong matching skills found."
            )
        
        
        # =====================
        # MISSING SKILLS
        # =====================
        
        st.subheader("❌ Missing Skills")
        
        if missing:
        
            st.write(
                ", ".join(missing[:20])
            )
        
        else:
        
            st.success(
                "No major missing skills detected."
            )
        
        
        # =====================
        # AI FEEDBACK
        # =====================
        
        st.subheader("🧠 AI Resume Feedback")
        
        st.write(feedback)
