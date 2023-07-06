from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def get_results_count(self):
        result_stats = self.find_element((By.CSS_SELECTOR, "#firstHeading > span"))
        return result_stats.text