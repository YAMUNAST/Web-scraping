import requests
from bs4 import BeautifulSoup

# BBC News URL
url = "https://www.bbc.com/news"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send request to the BBC News website
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all news headline elements
headlines = soup.find_all("h3")  # BBC often uses <h3> for headlines

# Print the top 10 headlines
print("BBC News Headlines:")
print("-" * 80)

for i, headline in enumerate(headlines[:10]):  # Get top 10 headlines
    print(f"{i+1}. {headline.text.strip()}")
    print("-" * 80)

