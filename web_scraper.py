import requests
from bs4 import BeautifulSoup
import json


def scrape_headlines():
    url = "https://quotes.toscrape.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes_data = []

        for item in soup.select(".quote"):
            quote = item.select_one(".text")
            author = item.select_one(".author")

            if quote and author:
                quotes_data.append({
                    "quote": quote.get_text(strip=True),
                    "author": author.get_text(strip=True)
                })

        if not quotes_data:
            print("No quotes found.")
            return

        # Save to JSON
        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(quotes_data, file, indent=4, ensure_ascii=False)

        # Save to text file
        with open("quotes.txt", "w", encoding="utf-8") as file:
            for item in quotes_data:
                file.write(f"Quote: {item['quote']}\n")
                file.write(f"Author: {item['author']}\n\n")

        print("Scraping completed successfully!")
        print(f"Total quotes collected: {len(quotes_data)}")
        print("Files created: quotes.json and quotes.txt")

        print("\nSample results:")
        for item in quotes_data[:3]:
            print(f"\nQuote: {item['quote']}")
            print(f"Author: {item['author']}")

    except requests.exceptions.RequestException as error:
        print("Website connection failed:", error)


if __name__ == "__main__":
    scrape_headlines()