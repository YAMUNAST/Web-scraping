import requests
from bs4 import BeautifulSoup

# CoinMarketCap URL
url = "https://coinmarketcap.com/"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send request to the website
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all rows in the table (excluding the header)
crypto_rows = soup.find_all("tr")

print("Top 10 Cryptocurrencies:")
print("-" * 80)

for i, row in enumerate(crypto_rows[1:11]):  # Skip the header row
    try:
        columns = row.find_all("td")
        name = columns[2].find("p").text.strip()  # Name of the crypto
        price = columns[3].find("span").text.strip()  # Price of the crypto
        
        print(f"{i+1}. {name}: {price}")
        print("-" * 80)
    except (AttributeError, IndexError):
        continue  # Skip rows that don't match the expected structure
