from locators import *

class TestLogin:

    def test_login_by_button_on_main_page(self, driver, registered_user):
        driver.find_element(*LOGIN_ACCOUNT_BUTTON_MAIN).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(registered_user['email'])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user['password'])
        driver.find_element(*LOGIN_BUTTON).click()

        assert driver.find_element(*PERSONAL_ACCOUNT_BUTTON).is_displayed()

    def test_login_by_personal_account_button(self, driver, registered_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(registered_user['email'])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user['password'])
        driver.find_element(*LOGIN_BUTTON).click()

        assert driver.find_element(*PERSONAL_ACCOUNT_BUTTON).is_displayed()

    def test_login_from_registration_form(self, driver, registered_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*REGISTER_LINK).click()
        driver.find_element(*LOGIN_FROM_REGISTER_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(registered_user['email'])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user['password'])
        driver.find_element(*LOGIN_BUTTON).click()

        assert driver.find_element(*PERSONAL_ACCOUNT_BUTTON).is_displayed()

    def test_login_from_forgot_password_form(self, driver, registered_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*FORGOT_PASSWORD_LINK).click()
        driver.find_element(*LOGIN_FROM_FORGOT_PASSWORD_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(registered_user['email'])
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(registered_user['password'])
        driver.find_element(*LOGIN_BUTTON).click()

        assert driver.find_element(*PERSONAL_ACCOUNT_BUTTON).is_displayed()