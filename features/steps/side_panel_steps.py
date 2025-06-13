from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click add to cart side panel')
def click_add_side_panel(context):
  sleep(3)
  context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
  sleep(3)

@when('Click view cart side panel')
def click_view_side_panel(context):
    sleep(3)
    context.driver.find_element(By.XPATH, '//a[text()="View cart & check out"]').click()
    sleep(3)

