# Automated tests - using Selenium, Python and PyTest

This is a project for automated E2E tests for app: https://staging.app.zaplify.com/login using Selenium, Python,
Pytest, allure reports and page object model.

## Visuals

Project includes screenshots of failed tests using allure report (https://docs.qameta.io/allure/).

## Installation

git clone https://github.com/msjozwiak/Tests-Selenium.git

## Usage

1. Requirements:
    * pip==19.0.3
    * setuptools==40.8.0
    * pytest==7.0.1
    * selenium==3.141.0
    * webdriver-manager==3.7.1
    * allure-pytest==2.12.0
    * assertpy==1.1
    * requests ==2.27.1
2. Tests execution: $ pytest --alluredir=/tmp/my_allure_results
3. Generating report to temp directory: $ allure serve /tmp/my_allure_results

## Test features and strategy

Test strategy - I've focused on happy paths and added a few negative paths for functional tests on the Chrome browser.
I've tested the most basic test cases.
I've tested the following features:
1. Login feature

