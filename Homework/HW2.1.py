#1. Practice with locators.
# Create locators + search strategy for these page elements of Amazon Sign in page:
# Amazon logo
# Email field
# Continue button
# Conditions of use link
# Privacy Notice link
# Need help link
# Forgot your password link
# Other issues with Sign-In link
# Create your Amazon account button


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%3F&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# 1. Amazon logo
logo = driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')

# 2. Email field
email = driver.find_element(By.ID, 'ap_email')

# 3. Continue button
continue_button = driver.find_element(By.XPATH, '//input[@class="a-button-input"]')

# 4. Conditions of use link
conditions_of_use = driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088"]')

# 5. Privacy Notice link
privacy_notice = driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496"]')

#6. Need help link
need_help = driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')

#7. Forgot your password link
forgot_password = driver.find_element(By.ID, 'auth-fpp-link-bottom')

#8. Other issues with Sign-In link
other_issues = driver.find_element(By.ID, 'ap-other-signin-issues-link')

#9. Create your Amazon account button
create_account = driver.find_element(By.ID, 'createAccountSubmit')


