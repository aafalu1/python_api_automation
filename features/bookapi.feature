# Created by basan at 8/19/2023
Feature: Employee API
  # Enter feature description here

  @SmokeTest
  Scenario Outline: verify add book API functionality
    Given the address is set for the Book Webservices
    And a header item 'content-type' and the value 'application/json' is set for the request
    When a body param '<body_param_1>' and value '<body_param_value_1>' is added to the json request
    And a body param '<body_param_2>' and value '<body_param_value_2>' is added to the json request
    And a body param '<body_param_3>' and value '<body_param_value_3>' is added to the json request
    And a body param '<body_param_4>' and value '<body_param_value_4>' is added to the json request
    And a body param '<body_param_5>' and value '<body_param_value_5>' is added to the json request
    And a body param '<body_param_6>' and value '<body_param_value_6>' is added to the json request
    And Post method called for a rest service path '<rest_service_path>'
    Then the status code is 201
    And validate the field '<response_field_name>' matches a value '<response_value>'
    Examples:
      | rest_service_path | response_field_name | response_value | body_param_1 | body_param_value_1 | body_param_2 | body_param_value_2 | body_param_3 | body_param_value_3 | body_param_4 | body_param_value_4 | body_param_5 | body_param_value_5 | body_param_6 | body_param_value_6 |
      | /employees        | id                  | 6              | id           | 6                  | name         | Harilal            | email        | harilal@aafalu.com | department   | account            | position     | accountant         | salary       | 50000              |


  @SmokeTest1
  Scenario Outline: verify <response_field_name> responses for <rest_service_path>
    Given the address is set for the Book Webservices
    And a header item 'content-type' and the value 'application/json' is set for the request
    When a body param '<body_param_1>' and value '<body_param_value_1>' is added to the json request
    And a body param '<body_param_2>' and value '<body_param_value_2>' is added to the json request
    And Get method called for a rest service path '<rest_service_path>'
    Then the status code is 200
    And validate the field '<response_field_name>' matches a value '<response_value>'


    Examples:
      | rest_service_path | response_field_name | response_value | body_param_1 | body_param_value_1 | body_param_2 | body_param_value_2 |
      | /employees        | salary              | 45000          | id           | 9                  | name         | HariB              |