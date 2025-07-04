# app.py

import streamlit as st
import fitz  # PyMuPDF
import io
import os
import google.generativeai as genai
from agents.question_agent import ask_question
from agents.summary_agent import summarize_pdf
from agents.image_agent import get_keywords, fetch_image_for_keyword

# API keys (use secrets on Streamlit Cloud)
GEMINI_API_KEY = os.getenv("AIzaSyCwJcrR_XU5ARZCw-rFq5p6PcMx_pZfGdc")
SERPAPI_KEY = os.getenv("f32926f616dd68e37b414049b6fd7c603bc3cfce761b3f577fe8e7de9a89c7e5")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="📄 PDF AI Assistant")
st.title("📄 PDF AI Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    # Extract PDF text
    stream = io.BytesIO(uploaded_file.read())
    doc = fitz.open(stream=stream, filetype="pdf")
    pdf_text = "\n".join(page.get_text() for page in doc)
    st.success("✅ PDF loaded successfully.")

    if st.button("📘 Summarize PDF"):
        with st.spinner("Summarizing..."):
            summary = summarize_pdf(model, pdf_text)
            st.markdown("### 📘 Summary")
            st.markdown(summary)

    question = st.text_input("Ask a question about the PDF")
    if st.button("💡 Get Answer"):
        if question.strip():
            with st.spinner("Thinking..."):
                answer = ask_question(model, pdf_text, question)
                st.markdown("### ✅ Answer")
                st.markdown(answer)
        else:
            st.warning("Please enter a question.")

    if st.button("🖼️ Show Keywords & Images"):
        with st.spinner("Extracting keywords and fetching images..."):
            keywords = get_keywords(model, pdf_text)
            for kw in keywords:
                st.markdown(f"**🔑 {kw}**")
                image_url = fetch_image_for_keyword(kw, SERPAPI_KEY)
                if image_url:
                    st.image(image_url, width=300)
                else:
                    st.warning("No image found.")
