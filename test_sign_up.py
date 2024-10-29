import pytest
from pytest_bdd import scenarios, given, when, then
from pages.sign_up_page import SignUpPage
from utils.browser_setup import browser_setup

# Load scenarios from the feature file
scenarios('../features/sign_up.feature')

@pytest.fixture
def sign_up_page(browser):
    return SignUpPage(browser)

@given("I am on the Magento sign-up page")
def open_sign_up_page(sign_up_page):
    sign_up_page.go_to_sign_up_page()

@when("I enter valid user details")
def enter_user_details(sign_up_page):
    sign_up_page.enter_email("test@example.com")
    sign_up_page.enter_password("SecurePassword123")

@when("I leave the email field blank")
def leave_email_blank(sign_up_page):
    sign_up_page.enter_password("SecurePassword123")

@when("I submit the form")
def submit_form(sign_up_page):
    sign_up_page.submit_form()

@then("I should see the account creation confirmation message")
def check_confirmation_message(sign_up_page):
    assert "Account created successfully" in sign_up_page.get_confirmation_message()

@then("I should see the error message 'Email required'")
def check_error_message(sign_up_page):
    assert "Email required" in sign_up_page.get_confirmation_message()