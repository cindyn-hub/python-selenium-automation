from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIGNIN_NAV_BTN = By.XPATH, '//button [@data-test="accountNav-signIn"]'

@when('Click Sign In from navigation menu')
def click_signin_nav(context):
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_NAV_BTN)).click()
    context.app.navigation_panel.click_signin_nav()
