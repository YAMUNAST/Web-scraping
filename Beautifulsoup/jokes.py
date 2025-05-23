import requests

url = "https://icanhazdadjoke.com/search"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

params = {
    "limit": 10  # Fetch 10 jokes
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    jokes = response.json().get("results", [])
    for i, joke in enumerate(jokes, start=1):
        print(f"Joke {i}: {joke['joke']}")
        print("-" * 80)
else:
    print("Failed to fetch jokes!")
