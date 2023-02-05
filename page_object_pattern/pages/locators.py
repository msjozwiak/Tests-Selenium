from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'submit')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '.jss18.jss19')
    USER_ICON = (By.XPATH, "(//div[@class='first-letter'])[1]")
    EMAIL_REQUIRED_ALERT = (
    By.XPATH, "(//p[@class='MuiFormHelperText-root MuiFormHelperText-contained helper Mui-error'])[1]")
    PASSWORD_REQUIRED_ALERT = (
        By.XPATH, "(//p[@class='MuiFormHelperText-root MuiFormHelperText-contained helper Mui-error'])[1]")
    PASSWORD_OR_EMAIL_INCORRECT_ALERT = (By.CLASS_NAME, "error")
