from scraper.utils import get_repos_from_urls
from selenium.webdriver.common.by import By

def get_hrefs(driver, url):
    hrefs = []
    for a in driver.find_elements(By.TAG_NAME, "a"):
        href = a.get_attribute("href")
        if href and url in href:
            hrefs.append(href)
    return hrefs


if __name__ == "__main__":

    # df  = pd.DataFrame(columns=['id',
    #                             'name',
    #                             'source',
    #                             'description',
    #                             'is_relative',
    #                             'relative_path'])
    url = "https://www.gnome-look.org/p/1099856/"
    print(get_repos_from_urls(url))
    # print("URL: ", url)
    # driver.get(url)

    # driver.implicitly_wait(5)
    # # print(type(ids))
    # # print(ids)

    # # print(driver.page_source)

    # hrefs = get_hrefs(driver, "github.com")
    # if len(hrefs) < 1:
    #     print("No more pages")

    # for href in hrefs:
    #     print("href: ", href)
