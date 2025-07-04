import requests

def get_keywords(model, pdf_text):
    prompt = f"""
Based on the following PDF content, extract ONLY 3 highly specific and relevant keywords or short phrases 
that best represent the core topics or subjects discussed. Avoid generic words like 'the', 'and', 'introduction', etc.

PDF Text:
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
    except Exception as e:
        print(f"Error fetching image for '{keyword}':", e)
        return None
