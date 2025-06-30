from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_BAR = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = By.XPATH, "//div[@data-test='@web/CartIcon']"
    SIGNIN_LINK = By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]'


    def search_product(self, search_word):
        self.input_text(search_word,*self.SEARCH_BAR )
        self.wait_for_element_click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart_icon(self):
        #self.click(*self.CART_BTN)
        self.wait_for_element_click(*self.CART_BTN)

    def click_signin_link(self):
        self.click(*self.SIGNIN_LINK)
