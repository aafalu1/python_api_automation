Feature: variables in behave framehork

@calculator
Scenario: storing variable with context keyword and reusint it on subsequent steps
When the user opens calculator application
And the user select first number as 2
And the user select second number as 3
And the user add the first number and second number
Then the result is 5
