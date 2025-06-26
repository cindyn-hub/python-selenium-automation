from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class NavigationPanel(Page):
    SIGNIN_NAV_BTN = By.XPATH, '//button [@data-test="accountNav-signIn"]'

    def click_signin_nav(self):
        self.wait_for_element_click(*self.SIGNIN_NAV_BTN)