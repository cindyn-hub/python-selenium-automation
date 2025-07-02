from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.base_page import Page



class HelpPage(Page):

    RETURNS_HEADER = (By.XPATH, "//h1[text()=' Returns']")
    PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    BAKERY_HEADER = (By.XPATH, "//h1[text()=' Bakery']")
    SELECT_DD = (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")


    def open_help_returns(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')
        sleep(3)

    def select_promotions(self, value):
        dd = self.find_element(*self.SELECT_DD)
        select = Select(dd)
        select.select_by_value(value)


    def verify_returns_opened(self):
        self.wait_for_element(*self.RETURNS_HEADER)


    def verify_promotions_opened(self):
        self.wait_for_element(*self.PROMOTIONS_HEADER)

    def verify_bakery_opened(self):
        self.wait_for_element(*self.BAKERY_HEADER)

