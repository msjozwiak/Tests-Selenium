import pytest
import allure
from allure_commons.types import AttachmentType
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from page_object_pattern.pages.login_page import LoginPage
from page_object_pattern.config.config import TestData


@pytest.fixture()
def setup(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.maximize_window()
    # driver.implicitly_wait(5)
    web_driver.get(TestData.LOGIN_URL)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    # request.cls.login_page = LoginPage(driver)
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(web_driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    web_driver.quit()
