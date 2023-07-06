from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search(driver):
    phrase = "Test automation"

    home_page = HomePage(driver)
    home_page.navigate_to()
    home_page.search(phrase)

    search_results_page = SearchResultsPage(driver)
    results_count = search_results_page.get_results_count()

    assert phrase.lower() in results_count.lower(), f"The phrase '{phrase}' was not found"