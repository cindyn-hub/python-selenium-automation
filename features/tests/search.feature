Feature: Test for Target Search


  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea


# Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for mug
#    Then Verify search worked for mug

  Scenario: User can see favorites tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown