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

content_div = soup.find("div", id="mw-content-text")

exclude_words = {"references", "external links", "see also", "notes"}

headings = []

#loop through h2, remove [edit]
for h2 in content_div.find_all("h2"):
    headline = h2.get_text(" ", strip=True)
    headline = headline.replace("[edit]", "").strip()

    #skip excluded words
    if headline.lower() in exclude_words:
        continue

    if headline:
        headings.append(headline)

#save to file
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")