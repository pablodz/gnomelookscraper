import requests


def get_directories_gitlab(repo_url):
    # Extract the owner and repository name from the URL
    owner, repo = repo_url.split("/")[-2:]

    # Construct the URL for the GitLab API's "List repository tree" endpoint
    api_url = f"https://gitlab.com/api/v4/projects/{owner}%2F{repo}/repository/tree"

    # Send a GET request to the API endpoint
    response = requests.get(api_url)

    # Check the status code of the response
    if response.status_code != 200:
        print("[get_directories_gitlab]response: ", response)
        return []

    # Extract the list of directories from the response
    directories = [item["name"] for item in response.json() if item["type"] == "tree"]

    return directories
