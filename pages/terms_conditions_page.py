from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class TermsConditionsPage(Page):


    def verify_terms_conditions_opened(self):
        self.wait_for_url_contains('terms-conditions')
