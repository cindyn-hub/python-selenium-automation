from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Search for {product}')
def search_products(context, product):
  context.driver.find_element(By.ID, 'search').send_keys(product)
  context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
  sleep(5)

@when('Click Cart icon')
def click_cart_icon(context):
    sleep(3)
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(5)

@when('Click Sign In link')
def click_signin_link(context):
    context.driver.find_element(By.XPATH, '//span [@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]').click()
    sleep(2)

@then('Verify header has {number} links')
def verify_header_links(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'