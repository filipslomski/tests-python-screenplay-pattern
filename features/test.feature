Feature: google search
  @google
  Scenario: Search in google
    Given I am on google page
    When I search for dota
    And I select dota 2 from search suggestions
    Then I should see over 50000 results