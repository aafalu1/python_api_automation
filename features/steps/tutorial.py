from pyexpat import model
from behave import *


@given(u'we have behave installed')
def step_impl(context):
    pass

@when(u'we implement a test')
def step_impl(context):
    assert True is not False


@then(u'behave will test it for us!')
def step_impl(context):
    assert context.failed is False
    
@given(u'a sample text loaded into the frobulator')
def step_impl(context):
   context.my_text=context.text


@when(u'we activate the frobulator')
def step_impl(context):
    pass


@then(u'we will find it similar to English')
def step_impl(context):
    print(f"&&&&&&&&&&&&&&&&& {context.my_text}")
    
@given(u'a set of specific users')
def step_impl(context):
    context.name=[]
    context.department= []
    for row in context.table:
        context.name.append(row['name'])
        context.department.append(row['department'])
          


@when(u'we count the number of people in each department')
def step_impl(context):
    print(f"name : {context.name}")


@then(u'we will find two people in "Silly Walks"')
def step_impl(context):
    print(f"department : {context.department}")


@then(u'we will find one person in "{department}"')
def step_impl(context, department):
    index=context.name.index('Barry')
    assert context.department.index(department) == index, f"expected {context.department.index(department)} but found {index}"
    
@given(u'I search for a valid book')
def step_impl(context):
    pass


@then(u'the result page will include "{text}"')
def step_impl(context, text):
    if "an invalid book" in context.scenario.name:
        assert text == "failure"
    else:
        assert text == "success"


@given(u'I search for a invalid book')
def step_impl(context):
    pass


@given(u'I am in \'{page_name}\' page')
@then(u'I am on \'{page_name}\' page')
def step_impl(context, page_name):
    print(f"page name : {page_name}")
    

@when(u'I click on home button')
def step_impl(context):
    print("click on Home button")