from page_object_pattern.pages.locators import LoginPageLocators
import time
from time import sleep
from page_object_pattern.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Page actions"""

    """This is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """This is used to check forgot password link"""
    def is_forgot_password_exists(self):
        return self.is_visible(LoginPageLocators.FORGOT_PASSWORD_LINK)

    """This is used to login to app"""
    def log_into_the_page(self, email, password):
        self.do_send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.do_send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.do_click(LoginPageLocators.LOGIN_BUTTON)

