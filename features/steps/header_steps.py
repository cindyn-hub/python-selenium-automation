from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_BAR = By.ID, 'search'
SEARCH_BTN = By.XPATH, "//button[@data-test='@web/Search/SearchButton']"
CART_BTN = By.XPATH, "//div[@data-test='@web/CartIcon']"
SIGNIN_LINK = By.XPATH, '//span [@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]'


@when('Search for {product}')
def search_products(context, product):
  # context.driver.find_element(*SEARCH_BAR).send_keys(product)
  # context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)).click()
  context.app.header.search_product()

@when('Click Cart icon')
def click_cart_icon(context):
    # context.driver.wait.until(EC.element_to_be_clickable(CART_BTN)).click()
    context.app.header.click_cart_icon()

@when('Click Sign In link')
def click_signin_link(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_LINK)).click()


@then('Verify header has {number} links')
def verify_header_links(context, number):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print(links)
    assert len(links) == int(number), f'Expected {number} links but got {len(links)}'