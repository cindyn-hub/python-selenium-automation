Feature: Test for Target Search


  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked


  Scenario: Verify Empty Cart
    Given Open target main page
    When Click Cart icon
    Then Verify cart is empty

  Scenario: Navigate to Sign In
    Given Open target main page
    When Click Sign In link
    And Click Sign In from navigation menu
    Then Verify Sign In form