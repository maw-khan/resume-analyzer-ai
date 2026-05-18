import os
from langchain_google_genai import ChatGoogleGenerativeAI

def generate_feedback(resume_text, jd_text, score, missing_keywords):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3
    )

    prompt = f"""
You are an expert ATS resume reviewer.

TASK:
Analyze this resume vs job description.

OUTPUT:
1. Short summary of match quality
2. 5 improvement suggestions
3. Keyword optimization tips
4. Formatting advice for ATS systems

DATA:

MATCH SCORE: {score}

MISSING KEYWORDS:
{list(missing_keywords)}

RESUME:
{resume_text[:2000]}

JOB DESCRIPTION:
{jd_text[:2000]}
"""

    response = llm.invoke(prompt)

    return response.content
