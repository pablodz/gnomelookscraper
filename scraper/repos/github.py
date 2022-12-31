import requests


def get_directories_github(repo_url):
    # Extract the owner and repository name from the URL
    print("[get_directories_github]", repo_url)
    # remove from # to final from url
    repo_url = repo_url.split("#")[0]
    owner, repo = repo_url.split("/")[-2:]

    # Construct the URL for the GitHub API's "List contents" endpoint
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    # Send a GET request to the API endpoint
    response = requests.get(api_url)

    # Check the status code of the response
    if response.status_code != 200:
        print("[get_directories_github]response: ", response)
        return []
    
    print(response.text)

    # Extract the list of directories from the response
    directories = [item["name"] for item in response.json() if item["type"] == "dir"]

    return directories


def extra_info_github(repo_url):
    
    return {
        "repository": repo_url,
        "last_commit": get_latest_sha_commit(repo_url),
        "zip_url": get_zip_url_for_latest_sha(repo_url)
    }
    

def get_latest_sha_commit (repo_url):
    # Extract the owner and repository name from the URL
    print("[get_latest_sha_commit]", repo_url)
    owner, repo = repo_url.split("/")[-2:]

    # Construct the URL for the GitHub API's "List contents" endpoint
    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    # Send a GET request to the API endpoint
    response = requests.get(api_url)

    # Check the status code of the response
    if response.status_code != 200:
        print("[get_latest_sha_commit]response: ", response)
        return []

    # Extract the list of directories from the response
    sha = response.json()[0]["sha"]

    return sha

def get_zip_url_for_latest_sha (repo_url):
    # Extract the owner and repository name from the URL
    print("[get_zip_url_for_latest_sha]", repo_url)
    owner, repo = repo_url.split("/")[-2:]

    # Construct the URL for the GitHub API's "List contents" endpoint
    api_url = f"https://api.github.com/repos/{owner}/{repo}/zipball"

    return api_url