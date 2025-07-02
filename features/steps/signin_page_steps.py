from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_signin(context):
  context.app.signin_page.open_signin()

@when('Click on Target terms and conditions link')
def click_terms_conditions(context):
  context.app.signin_page.click_terms_conditions()

@when('Switch to the newly opened window')
def switch_window(context):
  context.app.signin_page.switch_to_new_window()

@when('Enter correct email and click Continue')
def enter_email_click(context):
  context.app.signin_page.enter_email_click(context)

@when('Enter incorrect password')
def enter_incorrect_password(context):
  context.app.signin_page.enter_incorrect_password(context)

@when('Click Sign in with password')
def click_sign_in_password(context):
  context.app.signin_page.click_sign_in_password()

@then('Verify error message is shown')
def verify_error_message(context):
  context.app.signin_page.verify_error_message()

@then('Verify Sign In form')
def verify_signin_form(context):
  # actual_text = context.driver.find_element(By.XPATH, '//*[text()="Sign in or create account"]').text
  # assert "Sign in or create account" in actual_text, f"Error, expected 'Sign in or create account' not in actual {actual_text}"
  context.app.signin_page.verify_signin_form()


