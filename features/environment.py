from behave import fixture, use_fixture
import base64

from behave.model import Scenario

from file_handler import FileHandler


def before_all(context):
    for formatter in context._runner.formatters:
        if formatter.name == "html-pretty":
            context.embed = formatter.embed
            context.formatter = formatter


# @fixture
# def set_html_header(context):
#     image_path = FileHandler.generate_file_path("images", file_name="rose.jpg")
#     with open(image_path, "rb") as image_file:
#         data_encoded = base64.b64encode(image_file.read()).decode("utf-8")
#     # Assuming you have base64-encoded image data in data_encoded
#     icon_data = f"data:image/svg+xml;base64,{data_encoded}"
#     context.formatter.set_icon(icon=icon_data)
#     yield context
#
#
# @use_fixture(set_html_header, context=None)
# def run_scenario(context):
#     pass


# Define your Behave scenarios below this line


def log_to_html_report(context, log_message=None):
    return context.embed("text", str(log_message), "Click For More Info")

def after_scenario(context, scenario):
    if "calculator" in scenario.tags:
        print(f"it is true")
    else:
        print(f"it is false")
    
