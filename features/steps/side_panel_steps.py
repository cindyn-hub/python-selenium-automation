from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


ADD_CART_SIDE_BTN = By.CSS_SELECTOR, "[data-test='orderPickupButton']"
VIEW_CART_BTN = By.XPATH, '//a[text()="View cart & check out"]'

@when('Click add to cart side panel')
def click_add_side_panel(context):
  context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_SIDE_BTN)).click()


@when('Click view cart side panel')
def click_view_side_panel(context):
    context.driver.wait.until(EC.element_to_be_clickable(VIEW_CART_BTN)).click()
