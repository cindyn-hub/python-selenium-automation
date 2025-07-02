from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SigninPage(Page):

    SIGNIN_TXT = By.CSS_SELECTOR, 'h1[class*="h-margin-b-tiny"]'
    TERMS_CONDITIONS_LINK = By.CSS_SELECTOR, 'a[href*="/c/terms-conditions/"]'
    ERROR_MSG_TXT = (By.XPATH, "//div[text() = 'That password is incorrect.']")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[id="username"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[data-test="login-password"]')
    SIGNIN_PASSWORD_BTN = (By.CSS_SELECTOR, 'button[id="login"]')



    def verify_signin_form(self):
        self.verify_partial_text('Sign in or create account', *self.SIGNIN_TXT)

    def open_signin(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_conditions(self):
        sleep(8)
        self.wait_for_element_click(*self.TERMS_CONDITIONS_LINK)

    def enter_email_click(self, text, *locator):
        self.input_text("jafaw86339@asimarif.com", *self.EMAIL_FIELD )
        self.wait_for_element_click(*self.CONTINUE_BTN)
        sleep(3)

    def enter_incorrect_password(self, text, *locator):
        self.input_text("PasswordTest123", *self.PASSWORD_FIELD )

    def click_sign_in_password(self):
        self.wait_for_element_click(*self.SIGNIN_PASSWORD_BTN)

    def verify_error_message(self):
        self.wait_for_element(*self.ERROR_MSG_TXT)

