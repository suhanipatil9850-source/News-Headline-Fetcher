import os
import requests

API_KEY = os.environ.get("NEWSAPI_KEY", "YOUR_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_headlines(limit=5):
    if not API_KEY or API_KEY == "YOUR_API_KEY":
        return [], "Set NEWSAPI_KEY or replace YOUR_API_KEY in k.py."

    params = {"country": "in", "apiKey": API_KEY}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()

    if response.status_code != 200:
        return [], data.get("message", "Unable to fetch headlines")

    headlines = [article.get("title") for article in data.get("articles", [])[:limit]]
    return headlines, None


if __name__ == "__main__":
    headlines, error = fetch_headlines()

    if error:
        print("Error:", error)
    else:
        print("\n📰 Top Headlines:\n")
        for title in headlines:
            print("•", title)
