from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()

@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_opened(context):
    context.app.terms_conditions_page.verify_terms_conditions_opened()

@then('User can close new window and switch back to original')
def close_window_and_switch_to_original(context):
    context.app.base_page.close_window()
    context.app.base_page.switch_to_window_by_id(context.original_window)

