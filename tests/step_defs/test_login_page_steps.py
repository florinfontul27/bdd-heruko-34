from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from pytest_bdd import scenarios, when, given, then

from tests.conftest import browser

#Scenario
scenarios('../features/test_login_page.feature')

@given('the user open the login page')
def open_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()

@when('the user type username')
def type_username(browser):
    login_page = LoginPage(browser)
    login_page.insert_username_field('tomsmith')
@when('the user type password')
def input_password(browser):
    login_page = LoginPage(browser)
    login_page.insert_password_field('SuperSecretPassword')
@when('the user click log in')
def click_login(browser):
    login_page = LoginPage(browser)
    login_page.click_login_button()
@then('the user is on secure page')
def check_url(browser):
    secure_page = SecurePage(browser)
    assert secure_page.URL == secure_page.get_current_url()
@then('the welcome message is displayed')
def check_welcome_message(browser):
    secure_page = SecurePage(browser)
    assert "Welcome to the Secure Area. When you are done click logout below." == secure_page.getWelcomeMessage()




