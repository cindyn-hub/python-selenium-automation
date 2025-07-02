from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = By.CSS_SELECTOR, "[data-test*='chooseOptionsButton']"
SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@when('Click add to cart')
def click_add_to_cart(context):
  # sleep(10)
  # context.driver.find_element(*ADD_TO_CART_BTN).click()
  # sleep(3)
  context.app.search_results_page.click_add_to_cart()


@then('Verify search worked for {expected_product}')
def verify_search_results(context, expected_product):
  # actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
  # assert expected_product in actual_text, f"Error, expected {expected_product} not in actual {actual_text}"
  context.app.search_results_page.verify_search_results()


@when('Hover favorites icon')
def hover_fav_icon(context):
  context.app.search_results_page.hover_fav_icon()

@then('Favorites tooltip is shown')
def verify_fav_tt_shown(context):
  context.app.search_results_page.verify_fav_tt_shown()

