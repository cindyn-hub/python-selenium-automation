
Feature: Cart tests


  Scenario: Verify Empty Cart
    Given Open target main page
    When Click Cart icon
    Then Verify cart is empty
    Then Verify Cart page opened