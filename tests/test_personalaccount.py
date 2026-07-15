from locators import *

class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, logged_in_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.find_element(*ACCOUNT_HEADER).is_displayed()

    def test_go_to_constructor_from_account(self, driver, logged_in_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*BUNS_TAB).is_displayed()

    def test_go_to_constructor_by_logo(self, driver, logged_in_user):
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LOGO).click()
        assert driver.find_element(*BUNS_TAB).is_displayed()
