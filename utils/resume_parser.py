import fitz


def extract_resume_text(pdf_file):

    try:

        doc = fitz.open(
            stream=pdf_file.read(),
            filetype="pdf"
        )

        text = ""

        for page in doc:

            text += page.get_text() + "\n"

        if not text.strip():

            raise ValueError(
                "No readable text found in PDF."
            )

        return text.strip()

    except Exception as e:

        raise Exception(
            f"Failed to process PDF: {str(e)}"
        )
