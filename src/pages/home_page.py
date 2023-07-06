from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    URL = "https://en.wikipedia.org/"

    def navigate_to(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.find_element((By.ID, "searchInput"))    
        search_input.send_keys(phrase)
        search_input.submit()