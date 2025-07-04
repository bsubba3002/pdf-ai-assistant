def ask_question(model, pdf_text, user_question):
    prompt = f"""
You are an expert assistant. Read the following PDF content and answer the user's question using only relevant information from it.

PDF Content:
{pdf_text[:15000]}

Question:
{user_question}
"""
    response = model.generate_content(prompt)
    return response.text.strip()
