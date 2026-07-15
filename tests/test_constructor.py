from locators import *

class TestConstructor:

    def test_buns_tab(self, driver):
        driver.find_element(*SAUCES_TAB).click()
        driver.find_element(*BUNS_TAB).click()
        active_tab_text = driver.find_element(*ACTIVE_TAB).text
        assert 'Булки' in active_tab_text

    def test_sauces_tab(self, driver):
        driver.find_element(*SAUCES_TAB).click()
        active_tab_text = driver.find_element(*ACTIVE_TAB).text
        assert 'Соусы' in active_tab_text

    def test_fillings_tab(self, driver):
        driver.find_element(*FILLINGS_TAB).click()
        active_tab_text = driver.find_element(*ACTIVE_TAB).text
        assert 'Начинки' in active_tab_text
