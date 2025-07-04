import google.generativeai as genai

def summarize_pdf(model, pdf_text):
    prompt = f"Please summarize the following PDF content:\n\n{pdf_text[:15000]}"
    response = model.generate_content(prompt)
    return response.text
