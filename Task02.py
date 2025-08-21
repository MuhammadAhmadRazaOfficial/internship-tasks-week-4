import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        print("Here's a joke for you:\n")
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
    else:
        print(f"Failed to fetch joke. Status code: {response.status_code}")

# Run the function
fetch_joke()
