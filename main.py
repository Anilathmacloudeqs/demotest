import os
import requests
import base64

def update_or_create_file(username, repository, branch, access_token, filename, content):
    url = f"https://api.github.com/repos/{username}/{repository}/contents/{filename}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Check if the file exists
    response = requests.get(url, params={"ref": branch}, headers=headers)
    if response.status_code == 200:
        # File exists, get the current SHA and content
        current_sha = response.json()["sha"]
        current_content = base64.b64decode(response.json()["content"]).decode()

        # Check if the content is different
        if current_content != content:
            # Update the existing file
            data = {
                "message": f"Update {filename}",
                "content": base64.b64encode(content.encode()).decode(),
                "sha": current_sha,
                "branch": branch,
            }
            response = requests.put(url, headers=headers, json=data)
            print(response.text)
        else:
            print(f"The content of {filename} is already up to date.")
    else:
        # File does not exist, create a new file
        data = {
            "message": f"Add {filename}",
            "content": base64.b64encode(content.encode()).decode(),
            "branch": branch,
        }
        response = requests.put(url, headers=headers, json=data)
        print(response.text)

# Assuming you have set the PAT_TOKEN as a secret in your GitHub repository
username = "Anilathmacloudeqs"
repository = "demotest"
branch = "main"
access_token = os.environ.get("PAT_TOKEN")
filename = "hello.py"

if access_token is None:
    print("Access token not found. Make sure to set PAT_TOKEN as a secret.")
else:
    # Check if the file exists in the release branch and update or create accordingly
    update_or_create_file(username, repository, "release", access_token, filename, "Your new file content here")
