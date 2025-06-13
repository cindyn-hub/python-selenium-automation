
Feature: Test adding product to cart

  Scenario: Verify Kitkat is added to cart
    Given Open target main page
    When Search for kitkat
    And Click add to cart
    And Click add to cart side panel
    And Click view cart side panel
    Then Verify cart total price is 6.01