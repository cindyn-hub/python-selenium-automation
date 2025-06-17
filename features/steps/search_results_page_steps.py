from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = By.CSS_SELECTOR, "[data-test*='chooseOptionsButton']"
SIDE_NAV_PRODUCT_NAME = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@when('Click add to cart')
def click_add_to_cart(context):
  sleep(10)
  context.driver.find_element(*ADD_TO_CART_BTN).click()
  sleep(3)



@then('Verify search worked for {expected_product}')
def verify_search_results(context, expected_product):
  actual_text = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
  assert expected_product in actual_text, f"Error, expected {expected_product} not in actual {actual_text}"
