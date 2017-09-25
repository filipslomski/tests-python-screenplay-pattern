@google
Feature: Google

  @search
  Scenario: Search in google
    Given Filip is on google page
    When he searches for phrase dota then select dota 2 from suggestions list
    Then he should see over 50000 results

   @login
   Scenario: Login as Filip
    Given Filip is on google page
    When Filip logs in
    Then he should see himself as a logged user

    #of course this would require clean environment or checking and potentially logging out in before_scenario
   @login
   Scenario: Login as Karol
    Given Karol is on google page
    When Karol logs in
    Then he should see himself as a logged user