from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):
    CART_EMPTY_TXT = (By.XPATH, '//*[contains(text(), "Your cart is empty")]')

    def verify_empty_cart(self):
        actual_text = self.find_element(*self.CART_EMPTY_TXT).text
        assert "Your cart is empty" in actual_text, f"Error, expected 'Your cart is empty' not in actual {actual_text}"
