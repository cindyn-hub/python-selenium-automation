from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_BAR = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = By.XPATH, "//div[@data-test='@web/CartIcon']"

    def search_product(self):
        self.input_text('tea',*self.SEARCH_BAR )
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart_icon(self):
        self.click(*self.CART_BTN)
        sleep(5)
