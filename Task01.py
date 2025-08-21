import requests

def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        print(f"\nPublic Repositories of {username}:")
        for repo in repos:
            print(f"- {repo['name']}")
    else:
        print(f"Failed to fetch repos for {username}. Status code: {response.status_code}")

fetch_github_repos("MuhammadAhmadRazaOfficial")
