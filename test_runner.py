import os
import subprocess


def run_behave_with_html_report(tag):
    report_path = "report.html"
    # Construct the behave command
    command = f"behave -f html-pretty -o {report_path} --tags={tag} --no-capture --no-skipped"

    # Execute the behave command
    subprocess.run(command, shell=True)


# Example usage: Call the function to execute the behave command with the @smoketest tag
run_behave_with_html_report("@SmokeTest1")
