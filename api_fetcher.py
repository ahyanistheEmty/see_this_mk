import requests

def fetch_random_joke():
    """Fetches a random joke from a public API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"

if __name__ == "__main__":
    print("Fetching a random joke for you...\n")
    print(fetch_random_joke())
