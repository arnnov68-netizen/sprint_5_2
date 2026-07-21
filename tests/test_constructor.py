import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from urls import Urls
from helpers import wait_for_element


class TestConstructor:

    def test_buns_tab_active_by_default(self, browser):
        """
        Проверка, что вкладка «Булки» активна по умолчанию
        """
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text

    def test_switch_to_sauces_tab(self, browser):
        """
        Проверка перехода к разделу «Соусы»
        """
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].click();", sauces_tab)

        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text

    def test_switch_to_fillings_tab(self, browser):
        """
        Проверка перехода к разделу «Начинки»
        """
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Сначала переключаемся на "Соусы"
        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].click();", sauces_tab)
        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )

        fillings_tab = wait_for_element(browser, MainPageLocators.FILLINGS_TAB)
        browser.execute_script("arguments[0].click();", fillings_tab)

        WebDriverWait(browser, 5).until(
            lambda driver: "Начинки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text

    def test_switch_to_buns_tab(self, browser):
        """
        Проверка перехода к разделу «Булки»
        """
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Сначала переключаемся на "Соусы"
        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].click();", sauces_tab)
        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )

        buns_tab = wait_for_element(browser, MainPageLocators.BUNS_TAB)
        browser.execute_script("arguments[0].click();", buns_tab)

        WebDriverWait(browser, 5).until(
            lambda driver: "Булки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text

    def test_switch_to_buns_tab_from_fillings(self, browser):
        """
        Проверка перехода к разделу «Булки» из раздела «Начинки»
        """
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Переключаемся на "Начинки"
        fillings_tab = wait_for_element(browser, MainPageLocators.FILLINGS_TAB)
        browser.execute_script("arguments[0].click();", fillings_tab)
        WebDriverWait(browser, 5).until(
            lambda driver: "Начинки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )

        # Переключаемся на "Булки"
        buns_tab = wait_for_element(browser, MainPageLocators.BUNS_TAB)
        browser.execute_script("arguments[0].click();", buns_tab)

        WebDriverWait(browser, 5).until(
            lambda driver: "Булки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text
