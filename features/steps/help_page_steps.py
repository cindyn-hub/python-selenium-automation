from behave import given, when, then



@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {value}')
def select_promotions(context, value):
    context.app.help_page.select_promotions(value)

@then('Verify help Returns page opened')
def verify_returns_opened(context):
    context.app.help_page.verify_returns_opened()

@then('Verify help Current promotions page opened')
def verify_promotions_opened(context):
    context.app.help_page.verify_promotions_opened()

@then('Verify help Bakery page opened')
def verify_bakery_opened(context):
    context.app.help_page.verify_bakery_opened()



