from scraper.utils import scan_all_items_from_gnomelook,scrape_from_files,remove_duplicates_from_file
# from scraper.repos.github import get_zip_url_for_latest_sha


if __name__ == "__main__":

    # scan_all_items_from_gnomelook()
    # print(get_zip_url_for_latest_sha("https://github.com/B00merang-Project/System-4"))
    # remove_duplicates_from_file("./data/links.txt")
    scrape_from_files("./data/links.txt"+"fixed")