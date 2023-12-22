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
    
        # Update payload to include the filename in the destination branch
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


# Replace 'Anilathmacloudeqs', 'demotest', 'main', 'release', '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', and 'hello.py'
# with your actual GitHub username, repository name, source branch, destination branch, access token, and file path
push_file_to_branch('Anilathmacloudeqs', 'demotest', 'main', 'release', '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',
                    'hello.py', 'Commit message')
