from selenium.webdriver.common.by import By
from pages.base_page import Page




class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = By.CSS_SELECTOR, "[data-test*='chooseOptionsButton']"


    def verify_search_results(self):
       self.verify_partial_text('tea', *self.SEARCH_RESULTS_TXT)

    def click_add_to_cart(self, *locator):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)