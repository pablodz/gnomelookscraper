from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

def get_hrefs(driver, url):
    hrefs = []
    for a in driver.find_elements(By.TAG_NAME, 'a'):
        href = a.get_attribute('href')
        if href and url in href:
            hrefs.append(href)
    return hrefs 


if __name__ == "__main__":
    page = 1
    while True:
        print("Page: ", page)
        url = f"http://www.gnome-look.org/browse?cat=135&page={page}"
        print("URL: ", url)
        driver.get(url)


        driver.implicitly_wait(15)
        # print(type(ids))
        # print(ids)

        # print(driver.page_source)

        hrefs = get_hrefs(driver, "/p/")
        if len(hrefs) < 1:
            print("No more pages")
            break

        for href in hrefs:
            print("href: ", href)
            
        if page==1: # TODO: REMOVE THIS
            break
        page += 1
