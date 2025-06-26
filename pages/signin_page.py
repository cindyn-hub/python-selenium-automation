from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SigninPage(Page):

    SIGNIN_TXT = By.CSS_SELECTOR, 'h1[class*="h-margin-b-tiny"]'

    def verify_signin_form(self):
        self.verify_partial_text('Sign in or create account', *self.SIGNIN_TXT)