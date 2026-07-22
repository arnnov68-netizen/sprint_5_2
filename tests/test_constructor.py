import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from urls import Urls


class TestConstructor:

    def test_buns_tab_active_by_default(self, browser):
        """Проверка, что вкладка «Булки» активна по умолчанию"""
        browser.get(Urls.MAIN_PAGE)

        # Ждем загрузки
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Проверяем, что вкладка "Булки" активна
        buns_tab = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'current')]"))
        )
        assert buns_tab is not None

    def test_switch_to_sauces_tab(self, browser):
        """Проверка перехода к разделу «Соусы»"""
        browser.get(Urls.MAIN_PAGE)

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Нажимаем на вкладку "Соусы"
        sauces_tab = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))
        )
        sauces_tab.click()

        # Проверяем, что вкладка стала активной
        active_tab = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'current')]"))
        )
        assert active_tab is not None

    def test_switch_to_fillings_tab(self, browser):
        """Проверка перехода к разделу «Начинки»"""
        browser.get(Urls.MAIN_PAGE)

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Нажимаем на вкладку "Начинки"
        fillings_tab = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))
        )
        fillings_tab.click()

        # Проверяем, что вкладка стала активной
        active_tab = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'current')]"))
        )
        assert active_tab is not None