import os
import requests

def get_repository_files(username, repository, branch, access_token):
    url = f"https://api.github.com/repos/{username}/{repository}/contents/?ref={branch}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json()
        for file in files:
            print(file["name"])
    else:
        print(f"Failed to retrieve files. Status code: {response.status_code}")
        print(response.text)

# Assuming you have set the PAT_TOKEN as a secret in your GitHub repository
username = "Anilathmacloudeqs"
repository = "demotest"
branch = "main"
access_token = os.environ.get("PAT_TOKEN")

if access_token is None:
    print("Access token not found. Make sure to set PAT_TOKEN as a secret.")
else:
    get_repository_files(username, repository, branch, access_token)
