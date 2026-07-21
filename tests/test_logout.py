import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from locators import (
    MainPageLocators,
    ProfilePageLocators,
    LoginPageLocators
)
from urls import Urls
from helpers import wait_for_element, wait_for_clickable


class TestLogout:

    def test_logout_from_profile(self, browser, logged_in_user):
        """
        Проверка выхода из аккаунта через личный кабинет
        """
        # Переход в личный кабинет
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Выход из аккаунта
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

    def test_cannot_access_profile_after_logout(self, browser, logged_in_user):
        """
        Проверка, что после выхода нельзя перейти в профиль без авторизации
        """
        # Переход в личный кабинет
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Выход из аккаунта
        logout_button = wait_for_clickable(browser, ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

        # Проверяем, что мы на странице входа
        assert browser.current_url == Urls.LOGIN_PAGE

        # Пытаемся перейти в профиль
        browser.get(Urls.PROFILE_PAGE)

        # Проверяем, что кнопка "Выйти" отсутствует
        logout_buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Выход')]")
        assert len(logout_buttons) == 0, "Logout button should not be present for unauthorized user"

    def test_logout_and_login_again(self, browser, logged_in_user):
        """
        Проверка что после выхода можно снова войти
        """
        # Переход в личный кабинет
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Выход из аккаунта
        logout_button = wait_for_clickable(browser, ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()

        # Ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert browser.current_url == Urls.LOGIN_PAGE

        # Снова входим
        from tests.test_login import login_user
        login_user(browser, logged_in_user['email'], logged_in_user['password'])

        # Проверяем, что мы на главной странице
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверяем, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_logout_from_any_page(self, browser, logged_in_user):
        """
        Проверка, что выход работает с любой страницы
        """
        # Переходим на страницу конструктора
        browser.get(Urls.MAIN_PAGE)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        )

        # Переход в личный кабинет
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Выход из аккаунта
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

    def test_profile_page_not_accessible_without_login(self, browser):
        """
        Проверка, что страница профиля недоступна без авторизации
        """
        # Пытаемся перейти в профиль без авторизации
        browser.get(Urls.PROFILE_PAGE)

        # Ждем загрузки страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Проверяем, что кнопка "Выйти" отсутствует
        # Это основной признак того, что пользователь не авторизован
        logout_buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Выход')]")
        assert len(logout_buttons) == 0, "Logout button should not be present for unauthorized user"

        # Дополнительно проверяем, что страница не содержит личной информации
        # (проверяем отсутствие имени пользователя на странице)
        try:
            # Проверяем, что нет элемента с классом profile или user info
            profile_elements = browser.find_elements(By.XPATH,
                                                     "//div[contains(@class, 'profile')]//p[contains(text(), 'Имя')]")
            assert len(profile_elements) == 0, "Profile information should not be visible"
        except:
            pass
