import requests
from bs4 import BeautifulSoup

# ESPN Cricinfo URL
url = "https://www.espncricinfo.com/live-cricket-score"

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send request to ESPN Cricinfo
response = requests.get(url, headers=headers)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all match score elements
matches = soup.find_all("div", class_="ds-px-4 ds-py-3")  # Class may change, inspect and update

print("🏏 Live Cricket Matches:")
print("-" * 80)

for i, match in enumerate(matches[:5]):  # Fetch top 5 matches
    try:
        team_names = match.find_all("p", class_="ds-text-tight-m")  # Team names
        scores = match.find_all("strong")  # Scores
        match_status = match.find("span", class_="ds-text-tight-xs").text.strip()  # Status

        team1 = team_names[0].text.strip() if len(team_names) > 0 else "Unknown"
        team2 = team_names[1].text.strip() if len(team_names) > 1 else "Unknown"
        score1 = scores[0].text.strip() if len(scores) > 0 else "N/A"
        score2 = scores[1].text.strip() if len(scores) > 1 else "N/A"

        print(f"🏏 {team1} ({score1}) vs {team2} ({score2})")
        print(f"📢 {match_status}")
        print("-" * 80)

    except AttributeError:
        continue  # Skip if there's missing data
