from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click add to cart')
def click_add_to_cart(context):
  sleep(3)
  context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
  sleep(3)


@then('Verify search worked for {expected_product}')
def verify_search_results(context, expected_product):
  actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
  assert expected_product in actual_text, f"Error, expected {expected_product} not in actual {actual_text}"
