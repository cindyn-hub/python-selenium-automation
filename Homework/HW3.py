from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


#Optimal Locators
#Amazon Button
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#Create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#Your Name Textbox
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Email Textbox
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#Password Textbox
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#Password Context Message
driver.find_element(By.CSS_SELECTOR, '#ap_password_context_message_section')

#Re-enter Paswword Textbox
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#Create Account Button
driver.find_element(By.CSS_SELECTOR, '#continue')

#Condition of Use
driver.find_element(By.CSS_SELECTOR, 'a[href*="condition_of_use"]')

#Privacy Notice
driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_privacy_notice"]')

#Sign-in Button
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')

