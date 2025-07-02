
Feature: Signin Tests

  Scenario: Navigate to Sign In
    Given Open target main page
    When Click Sign In link
    And Click Sign In from navigation menu
    Then Verify Sign In form


  Scenario: Correct email and incorrect password
    Given Open sign in page
    When Enter correct email and click Continue
    And Enter incorrect password
    And Click Sign in with password
    Then Verify error message is shown