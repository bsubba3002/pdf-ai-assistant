import google.generativeai as genai

def ask_question(model, pdf_text, user_question):
    prompt = f"""
You are an expert assistant. Read the following PDF content and answer the user's question **only** using relevant info from it.

PDF Content:
{pdf_text[:15000]}

User Question:
{user_question}
"""
    response = model.generate_content(prompt)
    return response.text
