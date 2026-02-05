import requests
from bs4 import BeautifulSoup
import pandas as pd

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

tables = content_div.find_all("table")

for table in tables:
    rows = table.find_all("tr")
    data_rows = [r for r in rows if r.find_all("td")]
    if len(data_rows) >= 3:
        target_table = table
        break

header_cells = rows[0].find_all("th")
if header_cells:
    headers_list = [cell.get_text(" ", strip=True) for cell in header_cells]
else:
    #if no <th> create headers
    max_cols = max(len(r.find_all(["td", "th"])) for r in rows)
    headers_list = [f"col{i+1}" for i in range(max_cols)]

table_data = []

for r in rows[1:]:  #skip header row if present
    cells = r.find_all(["td", "th"])
    row_data = [c.get_text(" ", strip=True) for c in cells]
    #pad missing columns
    while len(row_data) < len(headers_list):
        row_data.append("")
    table_data.append(row_data)

df = pd.DataFrame(table_data, columns=headers_list)
df.to_csv("wiki_table.csv", index=False, encoding="utf-8")