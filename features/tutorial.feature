Feature: Showing of behave

  @behave_tutorial
  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  @behave_tutorial1
  Scenario: Some scenario
    Given a sample text loaded into the frobulator
      """
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
      eiusmod tempor incididunt ut labore et dolore magna aliqua.
      """
    When we activate the frobulator
    Then we will find it similar to English

  @behave_tutorial2
  Scenario: some scenario
    Given a set of specific users
      | name      | department  |
      | Barry     | Beer Cans   |
      | Pudey     | Silly Walks |
      | Two-Lumps | Silly Walks |
    When we count the number of people in each department
    Then we will find two people in "Silly Walks"
    But we will find one person in "Beer Cans"

  @behave_tutorial3
  Scenario: look up a book
    Given I search for a valid book
    Then the result page will include "success"

  @behave_tutorial3
  Scenario: look up an invalid book
    Given I search for a invalid book
    Then the result page will include failure"


@behave_tutorial4
  Scenario: using the regular expression
    Given I am in 'Login' page
    When I click on home button
    Then I am on 'Home' page


