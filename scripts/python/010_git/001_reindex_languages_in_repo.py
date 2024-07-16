import os

import requests

github_token = os.environ.get("GITHUB_API_KEY")


def get_repo_languages(user, repo, token):
    url = f"https://api.github.com/repos/{user}/{repo}/languages"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Error: API request unsuccessful")
    languages = response.json()

    return languages


def main():
    user = "AleksNeStu"  # Replace with GitHub username
    repo = "AI-POC"  # Replace with repository name
    languages = get_repo_languages(user, repo, github_token)
    print(languages)

if __name__ == "__main__":
    #TODO: Find post command to reindex
    main()