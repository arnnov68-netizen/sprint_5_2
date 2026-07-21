import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from locators import (
    MainPageLocators,
    ProfilePageLocators,
    LoginPageLocators,
    RegisterPageLocators
)
from urls import Urls
from helpers import wait_for_element, wait_for_clickable


class TestPersonalAccount:

    def test_go_to_personal_account(self, browser, logged_in_user):
        """
        Проверка перехода в личный кабинет по клику на «Личный кабинет»
        """
        # Клик на "Личный кабинет"
        try:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        except TimeoutException:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON_ALT)
        personal_account.click()

        # Ожидание перехода в профиль
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.PROFILE_PAGE)
        )

        # Проверка, что мы на странице профиля
        assert browser.current_url == Urls.PROFILE_PAGE

        # Проверка наличия кнопки "Выйти"
        logout_button = wait_for_element(browser, ProfilePageLocators.LOGOUT_BUTTON)
        assert logout_button.is_displayed()

    def test_go_to_constructor_from_profile(self, browser, logged_in_user):
        """
        Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»
        """
        # Переход в личный кабинет
        try:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        except TimeoutException:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON_ALT)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Клик на "Конструктор"
        try:
            constructor_button = wait_for_clickable(browser, ProfilePageLocators.CONSTRUCTOR_BUTTON)
        except TimeoutException:
            constructor_button = wait_for_clickable(browser, ProfilePageLocators.CONSTRUCTOR_BUTTON_ALT)
        constructor_button.click()

        # Ожидание перехода на главную страницу
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверка, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_go_to_main_from_profile_by_logo(self, browser, logged_in_user):
        """
        Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers
        """
        # Переход в личный кабинет
        try:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        except TimeoutException:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON_ALT)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Клик на логотип
        try:
            logo = wait_for_clickable(browser, ProfilePageLocators.LOGO)
        except TimeoutException:
            logo = wait_for_clickable(browser, ProfilePageLocators.LOGO_ALT)
        logo.click()

        # Ожидание перехода на главную страницу
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверка, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_logout_from_profile(self, browser, logged_in_user):
        """
        Проверка выхода из аккаунта через личный кабинет
        """
        # Переход в личный кабинет
        try:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        except TimeoutException:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON_ALT)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Нажимаем кнопку "Выйти"
        logout_button = wait_for_clickable(browser, ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()

        # Ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )

        # Проверка, что мы на странице входа
        assert browser.current_url == Urls.LOGIN_PAGE

        # Проверка, что кнопка "Войти" отображается
        login_button = wait_for_element(browser, LoginPageLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()
