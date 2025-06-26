
Feature: Test adding product to cart

  Scenario: Verify fanta bottle is added to cart
    Given Open target main page
    When Search for fanta bottle
    And Click add to cart
    And Click add to cart side panel
    And Click view cart side panel
    Then Verify cart total price is 3.14