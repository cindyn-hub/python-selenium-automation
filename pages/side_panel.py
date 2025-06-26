from selenium.webdriver.common.by import By
from pages.base_page import Page

class SidePanel(Page):
    ADD_CART_SIDE_BTN = By.CSS_SELECTOR, "[data-test='orderPickupButton']"
    VIEW_CART_BTN = By.XPATH, '//a[text()="View cart & check out"]'


    def click_add_side_panel(self, *locator):
        self.wait_for_element_click(*self.ADD_CART_SIDE_BTN)

    def click_view_side_panel(self, *locator):
        self.wait_for_element_click(*self.VIEW_CART_BTN)