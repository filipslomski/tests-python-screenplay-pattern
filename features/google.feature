@google
Feature: Google

  @search
  Scenario: Search in google
    Given I am on google page
    When I search for dota
    And I select dota 2 from search suggestions
    Then I should see over 50000 results

   @login
   Scenario: Login A
    Given I am on google page
    When I log in as user A
    Then I should see user A as a logged user

    #of course this would require clean environment or checking and potentially logging out in before_scenario
   @login
   Scenario: Login B
    Given I am on google page
    When I log in as user B
    Then I should see user B as a logged user