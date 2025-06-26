from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def verify_empty_cart(context):
    # actual_text = context.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]').text
    # assert "Your cart is empty" in actual_text, f"Error, expected 'Your cart is empty' not in actual {actual_text}"
    context.app.cart_page.verify_empty_cart()


@then('Verify cart total price is {price}')
def verify_cart_price(context, price):
    # actual_text = context.driver.find_element(By.XPATH, '//*[contains(text(), "{price}")]').text
    # assert price in actual_text, f"Error, expected cart total '{price}' not in actual {actual_text}"
    context.app.cart_page.verify_cart_price()

@then('Verify Cart page opened')
def verify_cart_opened(context):
    context.app.cart_page.verify_cart_opened()