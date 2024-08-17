# !!!!!!!!!!!! PLEASE NOTE THAT THE FOLLOWING PACKAGE NEED TO BE INSTALL !!!!!!!!!!!!
# pip install requests

import requests

# Variables
GITHUB_TOKEN = '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' # !!!!!!!!!!!! THIS TOKEN IS RELATED TO MY ACCOUNT !!!!!!!!!!!!
GITHUB_USERNAME = 'koami'
REPO_NAME = 'versionning_exam'

ISSUES = [
    {'title': 'Issue one', 'body': 'This is the first issue on this repo'},
    {'title': 'Issue two', 'body': 'This is the second issue on this repo'}
]

# Headers for Auth
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Repo creation
def create_github_repo(repo_name):
    url = f'https://api.github.com/user/repos'
    data = {
        'name': repo_name,
        'description': 'This repo is create in regard to my master degree class with GitHub REST API.',
        'private': False  # Note that by putting False I make this repo public
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Github repo '{repo_name}' has been created.")
        return response.json()
    else:
        print(f"An error has occured during the Github repo creation: {response.status_code} {response.text}")
        return None

# Add a ticket
def create_github_issue(repo_name, issue):
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/issues'
    response = requests.post(url, json=issue, headers=headers)
    if response.status_code == 201:
        print(f"Ticket '{issue['title']}' has been created.")
    else:
        print(f"An error has occured during the ticket creation : {response.status_code} {response.text}")

# main
if __name__ == '__main__':
    repo = create_github_repo(REPO_NAME)
    if repo:
        for issue in ISSUES: # This loop allow us to add all tickets that are in our ISSUES array
            create_github_issue(REPO_NAME, issue)
