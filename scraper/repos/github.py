import requests


def get_directories_github(repo_url):
    # Extract the owner and repository name from the URL
    print("[get_directories_github]", repo_url)
    owner, repo = repo_url.split("/")[-2:]

    # Construct the URL for the GitHub API's "List contents" endpoint
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    # Send a GET request to the API endpoint
    response = requests.get(api_url)

    # Check the status code of the response
    if response.status_code != 200:
        print("[get_directories_github]response: ", response)

    # Extract the list of directories from the response
    directories = [item["name"] for item in response.json() if item["type"] == "dir"]

    return directories
