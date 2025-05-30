# 2. Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)
#
# Test Case: Users can navigate to SignIn page
# 1. Open https://www.target.com/
# 2. Click Account button
# 3. Click SignIn btn from side navigationAyAu
# 4. Verify SignIn page opened:
# “Sign in or create account” text is shown,
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
driver.implicitly_wait(4)
account_button = driver.find_element(By.XPATH, '//span [@class="sc-43f80224-3 fBDEOp h-margin-r-x3"]')
account_button.click()
sign_in_button = driver.find_element(By.XPATH, '//button [@data-test="accountNav-signIn"]')
sign_in_button.click()
driver.find_element(By.XPATH, '//*[text()="Sign in or create account"]')
driver.find_element(By.XPATH, '//button[@type="button"]')