import os
import requests
import base64

def update_or_create_file(username, repository, main_branch, release_branch, access_token, filename, new_content):
    # Assuming you have set the PAT_TOKEN as a secret in your GitHub repository
    if access_token is None:
        print("Access token not found. Make sure to set PAT_TOKEN as a secret.")
        return

    url_main = f"https://api.github.com/repos/{username}/{repository}/contents/{filename}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Process the main branch
    branch = main_branch
    response = requests.get(url_main, params={"ref": branch}, headers=headers)
    if response.status_code == 200:
        # File exists, get the current SHA and content
        current_sha = response.json()["sha"]
        current_content = base64.b64decode(response.json()["content"]).decode()

        # Check if the content is different
        if current_content != new_content:
            # Update the existing file
            data = {
                "message": f"Update {filename}",
                "content": base64.b64encode(new_content.encode()).decode(),
                "sha": current_sha,
                "branch": branch,
            }
            response = requests.put(url_main, headers=headers, json=data)
            print(response.text)
        else:
            print(f"The content of {filename} in {branch} is already up to date.")
    else:
        # File does not exist, create a new file
        data = {
            "message": f"Add {filename}",
            "content": base64.b64encode(new_content.encode()).decode(),
            "branch": branch,
        }
        response = requests.put(url_main, headers=headers, json=data)
        print(response.text)

    # Process the release branch
    branch = release_branch
    response = requests.get(url_main, params={"ref": branch}, headers=headers)
    if response.status_code == 200:
        # File exists, get the current SHA and content
        current_sha = response.json()["sha"]
        current_content = base64.b64decode(response.json()["content"]).decode()

        # Check if the content is different
        if current_content != new_content:
            # Update the existing file
            data = {
                "message": f"Update {filename}",
                "content": base64.b64encode(new_content.encode()).decode(),
                "sha": current_sha,
                "branch": branch,
            }
            response = requests.put(url_main, headers=headers, json=data)
            print(response.text)
        else:
            print(f"The content of {filename} in {branch} is already up to date.")
    else:
        # File does not exist, create a new file
        data = {
            "message": f"Add {filename}",
            "content": base64.b64encode(new_content.encode()).decode(),
            "branch": branch,
        }
        response = requests.put(url_main, headers=headers, json=data)
        print(response.text)

update_or_create_file("Anilathmacloudeqs", "demotest", "main", "release", os.environ.get("PAT_TOKEN"), "hello.py", "Your new file content here")
