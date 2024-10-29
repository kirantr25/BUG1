from selenium.webdriver.common.by import By
from .base_page import BasePage

class SignUpPage(BasePage):
    SIGN_UP_BUTTON = (By.LINK_TEXT, "Sign Up")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "send2")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, "p.success")

    def go_to_sign_up_page(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.click(*self.SIGN_UP_BUTTON)

    def enter_email(self, email):
        self.enter_text(*self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD_FIELD, password)

    def submit_form(self):
        self.click(*self.SUBMIT_BUTTON)

    def get_confirmation_message(self):
        return self.wait_for_element(*self.CONFIRMATION_MESSAGE).text