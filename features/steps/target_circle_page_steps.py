from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle page')
def open_main(context):
  context.driver.get('https://www.target.com/circle')

@then('Verify at least {cell_number} benefit cells')
def verify_benefit_cells(context, cell_number):
    cells = context.driver.find_elements(By.CSS_SELECTOR, '[data-test*="@web/slingshot-components/CellsComponent/Link"]')
    print(cells)
    assert len(cells) >= int(cell_number), f'Expected at least {cell_number} benefit cells but got {len(cells)}'