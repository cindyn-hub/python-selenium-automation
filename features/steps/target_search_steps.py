from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
  context.driver.get('https://www.target.com/')



@when('Search for tea')
def search_products(context):
  context.driver.find_element(By.ID, 'search').send_keys('tea')
  context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
  sleep(5)


@then('Verify search worked')
def verify_search_results(context):
  actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
  assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"



@when('Click Cart icon')
def click_cart_icon(context):
    sleep(3)
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(5)


@then('Verify cart is empty')
def verify_empty_cart(context):
    actual_text = context.driver.find_element(By.XPATH, '//*[contains(text(), "Your cart is empty")]').text
    assert "Your cart is empty" in actual_text, f"Error, expected 'Your cart is empty' not in actual {actual_text}"




@when('Click Sign In link')
def click_signin_link(context):
    context.driver.find_element(By.XPATH, '//span [@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]').click()
    sleep(2)


@when('Click Sign In from navigation menu')
def click_signin_nav(context):
    context.driver.find_element(By.XPATH, '//button [@data-test="accountNav-signIn"]').click()
    sleep(5)


@then('Verify Sign In form')
def verify_signin_form(context):
  actual_text = context.driver.find_element(By.XPATH, '//*[text()="Sign in or create account"]').text
  assert "Sign in or create account" in actual_text, f"Error, expected 'Sign in or create account' not in actual {actual_text}"
