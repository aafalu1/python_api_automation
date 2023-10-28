import requests
from behave import given, when, then

from features.environment import log_to_html_report

# Dummy API URL (replace with your actual API URL)
API_BASE_URL = "httstp://localho:3000"

# Variables to store data between steps
request_headers = {}
request_data = {}


@given("the address is set for the Book Webservices")
def set_api_address(context):
    context.api_base_url = API_BASE_URL


@given('a header item \'{header}\' and the value \'{value}\' is set for the request')
def set_request_header(context, header, value):
    request_headers[header] = value


@when("a body param \'{param}\' and value \'{value}\' is added to the json request")
def add_request_body_param(context, param, value):
    request_data[param] = value


@when("Post method called for a rest service path \'{rest_service_path}\'")
def call_api(context, rest_service_path):
    print(request_data)
    url = f"{context.api_base_url}{rest_service_path}"
    response = requests.post(url, headers=request_headers, json=request_data)
    context.response = response
    print(f"responses from server: {context.response}")


@when("Get method called for a rest service path \'{rest_service_path}\'")
def step_call_get_method(context, rest_service_path):
    url = f"{context.api_base_url}{rest_service_path}"
    response = requests.get(url, headers=request_headers, params=request_data)
    context.response = response
    print(f"responses from server: {context.response}")


@then("the status code is {status_code:d}")
def check_status_code(context, status_code):
    try:
        # Check if the actual status code matches the expected status code
        assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"
    except AssertionError as e:
        # Handle the assertion error
        raise AssertionError(str(e))  # Raise the error to fail the step




@then("validate the field \'{field}\' matches a value \'{value}\'")
def validate_response_field(context, field, value):
    list_data = context.response.json()
    log_to_html_report(context, log_message=f"response: {list_data}")
    actual_data = None
    for data in list_data:
        if data[field] == value:
            actual_data = data[field]
            break
        else:
            print("value not found")
    assert actual_data == value
