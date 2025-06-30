from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TargetAppPage(Page):
    PP_LINK = (By.CSS_SELECTOR, "a[aria-label*='privacy policy']")

    def open_target_app(self):
        self.driver.get('https://www.target.com/c/target-app/-/N-4th2r')



    def click_privacy_link(self):
        sleep(3)
        self.wait_for_element_click(*self.PP_LINK)
