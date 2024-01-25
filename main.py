import os
import requests
import base64

username = "Anilathmacloudeqs"
repository = "demotest"
branch = "main"
access_token = os.environ.get("PAT_TOKEN")  # Replace with your Personal Access Token

def get_files_in_branch(username, repository, branch, access_token):
    url = f'https://api.github.com/repos/{username}/{repository}/contents?ref={branch}'
    headers = {'Authorization': f'token {access_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json()
        return [file['name'] for file in files if file['type'] == 'file']
    else:
        print(f"Error: {response.status_code}")
        return []

files_in_branch = get_files_in_branch(username, repository, branch, access_token)

print(f"Files in the '{branch}' branch of '{username}/{repository}':")
print(f"Files in the '{branch}' branch of '{username}/{repository}':")
print(', '.join(files_in_branch))

