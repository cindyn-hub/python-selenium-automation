
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened


  Scenario: User can select Help topic Nutrition Information
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Nutrition Information
    Then Verify help Bakery page opened