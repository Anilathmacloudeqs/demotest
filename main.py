import requests
import base64
import os
import sys
print('stating')

def push_file_to_branch(username, repository, source_branch, destination_branch, file_path, commit_message):
    source_api_url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}?ref={source_branch}'
    destination_api_url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}?ref={destination_branch}'

    access_token = os.environ.get('PAT_TOKEN')  # Use get to handle potential absence
    if not access_token:
        print("Error: GitHub PAT_TOKEN not found in environment variables.", file=sys.stderr)
        return

    headers = {'Authorization': f'token {access_token}'}

    source_file_response = requests.get(source_api_url, headers=headers)
    print(f"Source API URL: {source_api_url}")

    if source_file_response.status_code == 200:
        source_file_content = source_file_response.json()
        source_commit_sha = source_file_content['sha']

        decoded_content = base64.b64decode(source_file_content['content']).decode()

        payload = {
            'message': commit_message,
            'content': base64.b64encode(decoded_content.encode()).decode(),
            'branch': destination_branch,
            'sha': source_commit_sha
        }

        response = requests.put(destination_api_url, headers=headers, json=payload)

        if response.status_code == 201 or response.status_code == 200:
            print(f"File '{file_path}' successfully pushed to the '{destination_branch}' branch.")
        else:
            print(f"Error: Unable to push file. Status code: {response.status_code}", file=sys.stderr)
            print(response.json(), file=sys.stderr)
    else:
        print(f"Error: Unable to fetch source file. Status code: {source_file_response.status_code}", file=sys.stderr)

push_file_to_branch(
    'Anilathmacloudeqs',
    'demotest',
    'main',
    'release',
    'hello.py',
    'Commit message'
)
