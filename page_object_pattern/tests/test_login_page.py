
from page_object_pattern.config.config import TestData
from page_object_pattern.pages.login_page import LoginPage
import allure
from assertpy import assert_that
from page_object_pattern.pages.locators import LoginPageLocators
from page_object_pattern.tests.test_base import BaseTest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@allure.parent_suite('Login feature')
@allure.description('TestLoginPage')
class TestLoginPage(BaseTest):

    @allure.title('Login with valid data. Check if url has been changed')
    def test_correct_data_url(self):
        loginPage = LoginPage(self.driver)
        loginPage.log_into_the_page(TestData.EMAIL, TestData.PASSWORD)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(TestData.HOME_URL))
        assert_that(self.driver.current_url).is_equal_to(TestData.LOGIN_URL)

    @allure.title('Login with valid data. Check if user icon tekst is correct')
    def test_correct_data_customer(self):
        loginPage = LoginPage(self.driver)
        loginPage.log_into_the_page(TestData.EMAIL, TestData.PASSWORD)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.USER_ICON))
        text = loginPage.get_element_text(LoginPageLocators.USER_ICON).lower()
        assert text == TestData.EMAIL[0]

    @allure.title('Login with empty email and empty password fields. Check if url has not been changed')
    def test_all_fields_empty(self):
        loginPage = LoginPage(self.driver)
        loginPage.clear_text(LoginPageLocators.EMAIL_INPUT)
        loginPage.clear_text(LoginPageLocators.PASSWORD_INPUT)
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        loginPage.do_click(LoginPageLocators.LOGIN_BUTTON)
        assert_that(self.driver.current_url).is_equal_to(TestData.LOGIN_URL)

    @allure.title('Login with empty email field. Password is correct. Check if the appropriate alert is displayed')
    def test_email_field_empty(self):
        loginPage = LoginPage(self.driver)
        loginPage.clear_text(LoginPageLocators.EMAIL_INPUT)
        loginPage.do_send_keys(LoginPageLocators.PASSWORD_INPUT, TestData.PASSWORD)
        loginPage.do_click(LoginPageLocators.LOGIN_BUTTON)
        alert = loginPage.get_element_text(LoginPageLocators.EMAIL_REQUIRED_ALERT)
        assert_that(alert).contains("Required")

    @allure.title('Login with empty password field. Email is correct. Check if the appropriate alert is displayed')
    def test_password_field_empty(self):
        loginPage = LoginPage(self.driver)
        loginPage.do_send_keys(LoginPageLocators.EMAIL_INPUT, TestData.EMAIL)
        loginPage.clear_text(LoginPageLocators.PASSWORD_INPUT)
        loginPage.do_click(LoginPageLocators.LOGIN_BUTTON)
        alert = loginPage.get_element_text(LoginPageLocators.PASSWORD_REQUIRED_ALERT)
        assert_that(alert).contains("You must type in a password")

    @allure.title('Login with invalid data. Check if the appropriate alert is displayed')
    def test_incorrect_data(self):
        loginPage = LoginPage(self.driver)
        loginPage.log_into_the_page(TestData.EMAIL[1:], TestData.PASSWORD[1:])
        alert = loginPage.get_element_text(LoginPageLocators.PASSWORD_OR_EMAIL_INCORRECT_ALERT)
        assert_that(alert).contains("The password or email you entered is incorrect.")

    @allure.title('Login with invalid email and valid password. Check if the appropriate alert is displayed')
    def test_incorrect_email(self):
        loginPage = LoginPage(self.driver)
        loginPage.log_into_the_page(TestData.EMAIL[1:], TestData.PASSWORD)
        alert = loginPage.get_element_text(LoginPageLocators.PASSWORD_OR_EMAIL_INCORRECT_ALERT)
        assert_that(alert).contains("The password or email you entered is incorrect.")

    @allure.title('Login with invalid password and valid email. Check if the appropriate alert is displayed')
    def test_incorrect_password(self):
        loginPage = LoginPage(self.driver)
        loginPage.log_into_the_page(TestData.EMAIL, TestData.PASSWORD[1:])
        alert = loginPage.get_element_text(LoginPageLocators.PASSWORD_OR_EMAIL_INCORRECT_ALERT)
        assert_that(alert).contains("Email or password incorrect")

    @allure.title('Before login in to the page. Check if forgot password link is clickable and have correct text')
    def test_forgot_password_visible(self):
        loginPage = LoginPage(self.driver)
        text = loginPage.get_element_text(LoginPageLocators.FORGOT_PASSWORD_LINK)
        assert text == TestData.FORGOT_PASSWORD_LINK_TEXT

    @allure.title('Before login in to the page. Check if Login Page Title is correct')
    def test_login_page_title(self):
        loginPage = LoginPage(self.driver)
        title = loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE


