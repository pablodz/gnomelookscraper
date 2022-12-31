from scraper.utils import (get_repos_from_urls, remove_duplicates_from_file,
                           results_only_with_sources,
                           scan_all_items_from_gnomelook, scrape_from_files)

# from scraper.repos.github import get_zip_url_for_latest_sha


if __name__ == "__main__":

    # scan_all_items_from_gnomelook()
    # print(get_zip_url_for_latest_sha("https://github.com/B00merang-Project/System-4"))
    # remove_duplicates_from_file("./data/links.txt")
    # get_repos_from_urls("https://www.gnome-look.org/p/1715554")
    # scrape_from_files("./data/links.txt"+"fixed")
    results_only_with_sources("./data/result.json")