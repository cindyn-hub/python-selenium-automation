from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify Sign In form')
def verify_signin_form(context):
  actual_text = context.driver.find_element(By.XPATH, '//*[text()="Sign in or create account"]').text
  assert "Sign in or create account" in actual_text, f"Error, expected 'Sign in or create account' not in actual {actual_text}"
