
from behave import *

@when(u'the calculator application is opened')
def step_impl(context):
    print("calculator opens suxxessfully")


@when(u'the user select first number as {first_number:d}')
def step_impl(context, first_number):
    context.first_number=first_number

@when(u'the user select second number as {second_number:d}')
def step_impl(context, second_number):
    context.second_number=second_number
    

@when(u'the user add the first number and second number')
def step_impl(context):
   context.result= context.first_number+context.second_number

@then('the result is {result:d}')
def step_impl(context,result):
    assert context.result == result, f"expected {context.result} but found {result}"
    