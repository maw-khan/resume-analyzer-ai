import re

def extract_keywords(text):

    text = text.lower()

    words = re.findall(r'\b[a-zA-Z]{3,}\b', text)

    return set(words)


def calculate_match_score(resume_text, jd_text):

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    if not jd_keywords:
        return 0, set(), set()

    matched = resume_keywords.intersection(jd_keywords)

    missing = jd_keywords - resume_keywords

    score = (len(matched) / len(jd_keywords)) * 100

    return round(score, 2), matched, missing
