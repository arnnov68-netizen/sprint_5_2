from locators import *

class TestLogout:

    def test_logout(self, driver, logged_in_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LOGOUT_BUTTON).click()
        assert driver.find_element(*LOGIN_BUTTON).is_displayed()