from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def verify_empty_cart(context):
    # actual_text = context.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]').text
    # assert "Your cart is empty" in actual_text, f"Error, expected 'Your cart is empty' not in actual {actual_text}"
    context.app.cart_page.verify_empty_cart()


@then('Verify cart total price is 6.01')
def verify_cart_price(context):
    actual_text = context.driver.find_element(By.XPATH, '//*[contains(text(), "6.01")]').text
    assert "6.01" in actual_text, f"Error, expected cart total '6.01' not in actual {actual_text}"
