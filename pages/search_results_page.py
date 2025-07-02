from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = By.CSS_SELECTOR, "[data-test*='chooseOptionsButton']"
    FAV_ICON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TT_TEXT = (By.XPATH, "//*[contains(text(), 'Click to sign in and save')]")
    def verify_search_results(self):
       self.verify_partial_text('tea', *self.SEARCH_RESULTS_TXT)

    def click_add_to_cart(self, *locator):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def hover_fav_icon(self):
        self.hover_element(*self.FAV_ICON)

    def verify_fav_tt_shown(self):
        self.wait_for_element(*self.FAV_TT_TEXT)

