from locators import *
from helpers import generate_invalid_password

class TestRegistration:

    def test_successful_registration(self, driver, new_user_data):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*REGISTER_LINK).click()
        driver.find_element(*NAME_INPUT).send_keys(new_user_data['name'])
        driver.find_element(*EMAIL_INPUT).send_keys(new_user_data['email'])
        driver.find_element(*PASSWORD_INPUT).send_keys(new_user_data['password'])
        driver.find_element(*REGISTER_BUTTON).click()

        assert driver.find_element(*LOGIN_HEADER).is_displayed()

    def test_registration_invalid_password(self, driver, new_user_data):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*REGISTER_LINK).click()
        driver.find_element(*NAME_INPUT).send_keys(new_user_data['name'])
        driver.find_element(*EMAIL_INPUT).send_keys(new_user_data['email'])
        driver.find_element(*PASSWORD_INPUT).send_keys(generate_invalid_password())
        driver.find_element(*REGISTER_BUTTON).click()

        assert driver.find_element(*PASSWORD_ERROR).is_displayed()