import sys
import requests
import base64

def push_file_to_branch(username, repository, source_branch, destination_branch, access_token, file_path, commit_message):
    # API URLs for the source and destination branches
    source_api_url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}?ref={source_branch}'
    destination_api_url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}?ref={destination_branch}'

    headers = {'Authorization': f'token {access_token}'}

    source_file_response = requests.get(source_api_url, headers=headers)
    print(source_api_url)

    if source_file_response.status_code == 200:
        # Get the current commit SHA of the source file
        source_file_content = source_file_response.json()
        source_commit_sha = source_file_content['sha']

        # Encode file content in base64
        encoded_content = base64.b64decode(source_file_content['content']).decode()

        # Prepare payload for creating a new file in the destination branch
        payload = {
            'message': commit_message,
            'content': base64.b64encode(encoded_content.encode()).decode(),
            'branch': destination_branch,
            'sha': source_commit_sha
        }

        # Create or update the file in the destination branch
        response = requests.put(destination_api_url, headers=headers, json=payload)

        if response.status_code == 201 or response.status_code == 200:
            print(f"File '{file_path}' successfully pushed to the '{destination_branch}' branch.")
        else:
            print(f"Error: Unable to push file. Status code: {response.status_code}")
            print(response.json())
    else:
        print(f"Error: Unable to fetch source file. Status code: {source_file_response.status_code}")

if __name__ == "__main__":
    # Get command line arguments
    github_username = sys.argv[1]
    repository_name = sys.argv[2]
    source_branch = sys.argv[3]
    destination_branch = sys.argv[4]
    github_token = sys.argv[5]
    file_path = sys.argv[6]
    commit_message = sys.argv[7]

    # Call the function with command line arguments
    push_file_to_branch(github_username, repository_name, source_branch, destination_branch, github_token, file_path, commit_message)
