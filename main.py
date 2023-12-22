import requests

def list_files_in_repo(username, repository, branch, access_token):
    api_url = f'https://api.github.com/repos/{username}/{repository}/contents/'
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(api_url + '?ref=' + branch, headers=headers)

    if response.status_code == 200:
        files = response.json()
        for file in files:
            print(file['name'])
    else:
        print(f"Error: Unable to fetch files. Status code: {response.status_code}")

# Replace 'Anilathmacloudeqs', 'demotest', 'main', and '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' with your actual GitHub username, repository name, branch name, and access token
list_files_in_repo('Anilathmacloudeqs', 'demotest', 'main', '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')
