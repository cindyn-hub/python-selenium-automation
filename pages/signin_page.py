from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SigninPage(Page):

    SIGNIN_TXT = By.CSS_SELECTOR, 'h1[class*="h-margin-b-tiny"]'
    TERMS_CONDITIONS_LINK = By.CSS_SELECTOR, 'a[href*="/c/terms-conditions/"]'


    def verify_signin_form(self):
        self.verify_partial_text('Sign in or create account', *self.SIGNIN_TXT)

    def open_signin(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_conditions(self):
        sleep(8)
        self.wait_for_element_click(*self.TERMS_CONDITIONS_LINK)



