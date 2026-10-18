import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

print("API key loaded:", bool(API_KEY))

def fetch_news():

    if not API_KEY:
        print("NEWS_API_KEY missing. Check your .env file.")
        return []

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "apiKey": API_KEY,
        "pageSize": 5
    }

    try:
        response = requests.get(url,params=params, timeout=10)
        print("Status code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]
            return articles
        
        else:
            print("News fetch failed:", response.text)
            return []
        
    except requests.exceptions.Timeout:
        print("Request time out. Please try again.")
        return[]

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return []

    except ValueError as e:
        print(f"Invalid JSON response: {e}")
        return []

articles = fetch_news()

print(f"Total article fetched: {len(articles)}")



def display_news(articles):
    if not articles:
        print("No news articles available.")
        return

    for article in articles:
        title = article.get("title") or "Title not available"
        source = article.get("source", {}).get("name") or "Unknown source"
        published_at = article.get("publishedAt") or "Date not available"
        description = article.get("description") or "Description not available"

        print(f"\n📰 {title}")
        print(f"Source: {source}")
        print(f"Published At: {published_at}")
        print(f"Description: {description}")
        print("-" * 60)

display_news(articles)
