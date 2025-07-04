import fitz  # PyMuPDF
import io

def extract_text_from_upload(uploaded_file):
    if not uploaded_file or not uploaded_file.value:
        return None
    file_info = uploaded_file.value[0]
    stream = io.BytesIO(file_info['content'])
    doc = fitz.open(stream=stream, filetype="pdf")
    return "\n".join(page.get_text() for page in doc)
