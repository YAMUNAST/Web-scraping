import requests
from bs4 import BeautifulSoup

# URL of Stack Overflow's latest questions
url = "https://stackoverflow.com/questions"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send request to the website
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all question elements
questions = soup.find_all("div", class_="s-post-summary")

# Loop through the first 10 questions and extract details
for i, question in enumerate(questions[:10]):
    title = question.find("h3").text.strip()  # Extract question title
    link = "https://stackoverflow.com" + question.find("a")["href"]  # Extract question link

    print(f"{i+1}. {title}")
    print(f"   Link: {link}")
    print("-" * 80)
