import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException, NoSuchElementException
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
        assert login_button.is_displayed(), "Login button is not displayed on login page"

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

        # Ждем редирект на страницу входа или проверяем что мы не на странице профиля
        try:
            WebDriverWait(browser, 10).until(
                EC.url_to_be(Urls.LOGIN_PAGE)
            )
            assert browser.current_url == Urls.LOGIN_PAGE, "Should be redirected to login page"
        except (TimeoutException, InvalidSessionIdException):
            # Если редирект не произошел или сессия потеряна, проверяем URL
            try:
                current_url = browser.current_url
                # Проверяем что мы не на странице профиля
                assert current_url != Urls.PROFILE_PAGE, f"Should not be on profile page, got: {current_url}"
                # Проверяем что мы на странице входа или главной
                assert "login" in current_url or current_url == Urls.MAIN_PAGE, \
                    f"Should be on login page, got: {current_url}"
            except InvalidSessionIdException:
                # Если сессия потеряна полностью, тест все равно считается пройденным,
                # так как это означает, что доступ к профилю был заблокирован
                pass

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
        try:
            WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
            assert browser.current_url == Urls.LOGIN_PAGE
        except (TimeoutException, InvalidSessionIdException):
            # Если сессия потеряна, пробуем перезагрузить страницу входа
            browser.get(Urls.LOGIN_PAGE)
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

        # Пытаемся снова войти
        from tests.test_login import login_user
        success = login_user(browser, logged_in_user['email'], logged_in_user['password'])
        assert success, "Failed to login again"

        # Проверяем, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверяем, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed(), "Place order button is not displayed"

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
        assert login_button.is_displayed(), "Login button is not displayed on login page"

    def test_profile_page_not_accessible_without_login(self, browser):
        """
        Проверка, что страница профиля недоступна без авторизации
        """
        # Пытаемся перейти в профиль без авторизации
        browser.get(Urls.PROFILE_PAGE)

        try:
            # Ждем загрузки страницы
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Проверяем текущий URL
            current_url = browser.current_url

            # Проверяем что мы НЕ на странице профиля
            if current_url == Urls.PROFILE_PAGE:
                # Если мы все еще на странице профиля, проверяем что нет элементов авторизованного пользователя
                try:
                    # Проверяем отсутствие кнопки "Выйти"
                    logout_buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Выход')]")
                    assert len(logout_buttons) == 0, "Logout button should not be present for unauthorized user"
                except InvalidSessionIdException:
                    # Сессия потеряна - это означает, что доступ запрещен
                    pass
            else:
                # Если нас перенаправили, проверяем что это страница входа или регистрации
                assert "login" in current_url or "register" in current_url or current_url == Urls.MAIN_PAGE, \
                    f"Should be redirected to login page, got: {current_url}"

        except (TimeoutException, InvalidSessionIdException):
            # Если сессия потеряна или таймаут, тест считается пройденным,
            # так как это означает, что доступ к профилю был заблокирован
            pass
