import json
import re

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

from scraper.repos.github import extra_info_github, get_directories_github
from scraper.repos.gitlab import get_directories_gitlab

options = ChromeOptions()
options.add_argument("--window-size=1280,720")
options.add_argument("--headless")
# add javascript render
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
# change user agent
options.add_argument(
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/108.0.0.0 Safari/537.36"
)

driver = Chrome(options=options)


def extra_info_repo(repo_url):
    """Get extra information from a repository URL.

    Args:
        repo_url (str): The URL of the repository.

    Returns:
        dict: A dictionary with extra information.
    """
    if "github.com" in repo_url:
        return extra_info_github(repo_url)
    elif "gitlab.com" in repo_url:
        # return extra_info_gitlab(repo_url)
        return {}
    else:
        raise Exception(f"Unsupported repository: {repo_url}")


def get_directories_from_repo(repo_url):
    """Get a list of directories from a repository URL.

    Args:
        repo_url (str): The URL of the repository.

    Returns:
        list: A list of directories in the repository.
    """
    if "github.com" in repo_url:
        return get_directories_github(repo_url)
    elif "gitlab.com" in repo_url:
        return get_directories_gitlab(repo_url)
    else:
        raise Exception(f"Unsupported repository: {repo_url}")


def scan_all_items_from_gnomelook():
    page = 133  # max 135 # starts 28
    while True:
        result = {}
        print("Page: ", page)
        # newest necessary to only create new items
        url = f"http://www.gnome-look.org/browse?cat=135&page={page}&ord=newest"
        print("URL: ", url)
        driver.get(url)

        driver.implicitly_wait(5)
        hrefs = get_hrefs(driver, "/p/")
        if len(hrefs) < 1:
            print("No more pages")
            break

        for h in hrefs:
            repos = get_repos_from_urls(h)
            print("Checking: ", h, "[repos]", repos)
            extras = {}
            for r in repos:
                extra = extra_info_repo(r)
                extras = extra
            result[page] = {
                "url": h,
                "sources": extras,
            }
            break

        # result to json file
        with open(f"./data/{page}.json", "w") as f:
            json.dump(result, f, indent=4)

        break

        page += 1


def get_hrefs(driver, url):
    hrefs = []
    for a in driver.find_elements(By.TAG_NAME, "a"):
        href = a.get_attribute("href")
        if href and url in href:
            hrefs.append(href)
    return hrefs


def remove_duplicates_list(urls: list):
    return list(dict.fromkeys(urls))


def filter_hrefs(urls: list):
    new_urls = []
    for u in urls:
        if "gnome-look.org" in new_urls:
            new_urls.append(u)

    return remove_duplicates_list(new_urls)


def remove_subpaths_in_url_repo(urls: list):

    # Compile the regular expression
    for u in urls:
        pattern = re.compile(r"^(https://[^/]+/[^/]+/[^/]+).*$")
        match = pattern.match(u)
        base_url = match.group(1)
        urls[urls.index(u)] = base_url

    return urls


def valid_dir_repository(dirs: list):
    for d in dirs:
        if "gtk-3.0" in d or "gtk-2.0" in d or "gtk-4.0" in d:
            return True
    return False


def get_repos_from_urls(url: str):
    # print("URL: ", url)
    driver.get(url)
    driver.implicitly_wait(5)

    hrefs_github = get_hrefs(driver, "github.com")
    hrefs_gitlab = get_hrefs(driver, "gitlab.com")
    total_git_repos = hrefs_github + hrefs_gitlab
    total_git_repos = remove_subpaths_in_url_repo(total_git_repos)
    total_git_repos = remove_duplicates_list(total_git_repos)
    total_git_repos_valid = []
    for g in total_git_repos:
        # print("[get_repos_from_urls]href: ", g)
        dirs = get_directories_from_repo(g)
        # print("dirs: ", dirs)
        valid = valid_dir_repository(dirs)
        if valid:
            print("[get_repos_from_urls]valid: ", g, "[dirs]", dirs)
            total_git_repos_valid += [g]
        else:
            print("[get_repos_from_urls]invalid: ", g, "[dirs]", dirs)
            continue

    return total_git_repos_valid
