from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, '//*[contains(text(), "Your cart is empty")]')
    cart_empty_txt = 'Your cart is empty'
    CART_PRICE_TXT = By.CSS_SELECTOR, 'div[class*="sc-6e829a3-1 dyLWXU"]'

    def verify_empty_cart(self):
        self.verify_text(self.cart_empty_txt, *self.CART_EMPTY_MSG)

    def verify_cart_opened(self):
        self.verify_partial_url('/cart')

    def verify_cart_price(self):
       self.verify_partial_text('3.14', *self.CART_PRICE_TXT)
