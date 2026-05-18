import re


# =========================
# STOPWORDS
# =========================

STOPWORDS = {
    "the", "and", "for", "with", "you",
    "are", "this", "that", "have", "has",
    "from", "your", "will", "using", "use",
    "into", "their", "about", "such", "well",
    "they", "them", "our", "who", "was",
    "were", "been", "being", "also", "can",
    "all", "any", "job", "role", "work",
    "year", "years", "team", "detail",
    "apply", "related", "including"
}


# =========================
# EXTRACT KEYWORDS
# =========================

def extract_keywords(text):

    text = text.lower()

    words = re.findall(r'\b[a-zA-Z][a-zA-Z+#.-]{2,}\b', text)

    keywords = {
        word for word in words
        if word not in STOPWORDS
    }

    return keywords


# =========================
# MATCH SCORE
# =========================

def calculate_match_score(resume_text, jd_text):

    resume_keywords = extract_keywords(
        resume_text
    )

    jd_keywords = extract_keywords(
        jd_text
    )

    if not jd_keywords:

        return 0, [], []

    matched = sorted(
        list(
            resume_keywords.intersection(
                jd_keywords
            )
        )
    )

    missing = sorted(
        list(
            jd_keywords - resume_keywords
        )
    )

    score = (
        len(matched) / len(jd_keywords)
    ) * 100

    return round(score, 2), matched, missing
