import fitz

def extract_resume_text(pdf_file):

    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text() + "\n"

    return text.strip()
