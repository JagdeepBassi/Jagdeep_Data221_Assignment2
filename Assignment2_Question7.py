import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

#to avoid error
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

#print title
title = soup.title.string
print("Page Title:")
print(title)

#print first paragraph with more than 50 characters
content_div = soup.find("div", id="mw-content-text")

for p in content_div.find_all("p"):
    text = p.get_text(" ", strip=True)
    if len(text) >= 50:
        print("\nFirst valid paragraph:")
        print(text)
        break