import requests

def get_keywords(model, pdf_text):
    prompt = f"""
Extract exactly 3 highly relevant and specific keywords or short phrases from the following PDF content:

{pdf_text[:15000]}
"""
    response = model.generate_content(prompt)
    return [kw.strip("•-123. ") for kw in response.text.split("\n") if kw.strip()][:3]

def fetch_image_for_keyword(keyword, serpapi_key):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_images",
        "q": keyword,
        "api_key": serpapi_key
    }
    try:
        res = requests.get(url, params=params).json()
        return res['images_results'][0]['original']
    except Exception:
        return None
