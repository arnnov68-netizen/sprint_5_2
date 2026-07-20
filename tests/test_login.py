import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators,
    ProfilePageLocators
)
from urls import Urls
from helpers import wait_for_element, wait_for_clickable, find_all_inputs


def login_user(browser, email, password, expected_url=Urls.MAIN_PAGE):
    """
    Вспомогательная функция для входа в аккаунт

    Args:
        browser: экземпляр браузера
        email: email пользователя
        password: пароль пользователя
        expected_url: ожидаемый URL после входа (по умолчанию главная страница)

    Returns:
        bool: True если вход выполнен успешно
    """
    # Переход на страницу входа, если мы не на ней
    if browser.current_url != Urls.LOGIN_PAGE:
        browser.get(Urls.LOGIN_PAGE)

    # Ждем загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Пробуем найти поля ввода разными способами
    try:
        # Способ 1: найти все поля ввода и заполнить по порядку
        inputs = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
        )

        if len(inputs) >= 2:
            inputs[0].clear()
            inputs[0].send_keys(email)

            inputs[1].clear()
            inputs[1].send_keys(password)
        else:
            raise Exception("Не найдено достаточно полей ввода")

    except Exception:
        try:
            # Способ 2: найти по атрибуту name
            email_input = wait_for_element(browser, LoginPageLocators.EMAIL_INPUT)
            email_input.clear()
            email_input.send_keys(email)

            password_input = wait_for_element(browser, LoginPageLocators.PASSWORD_INPUT)
            password_input.clear()
            password_input.send_keys(password)

        except Exception:
            try:
                # Способ 3: найти по placeholder
                email_input = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']"))
                )
                email_input.clear()
                email_input.send_keys(email)

                password_input = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
                )
                password_input.clear()
                password_input.send_keys(password)

            except Exception:
                # Способ 4: через JavaScript
                browser.execute_script(
                    "document.querySelector('input[type=\"email\"], input[name=\"email\"]').value = arguments[0];",
                    email
                )
                browser.execute_script(
                    "document.querySelector('input[type=\"password\"]').value = arguments[0];",
                    password
                )

    # Находим кнопку входа
    try:
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
        )
    except:
        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

    login_button.click()

    # Ожидание перехода на ожидаемую страницу
    try:
        WebDriverWait(browser, 10).until(
            EC.url_to_be(expected_url)
        )
        return True
    except TimeoutException:
        return False


class TestLogin:

    def test_login_main_button(self, browser, registered_user):
        """
        Проверка входа по кнопке «Войти в аккаунт» на главной странице
        """
        # На главной странице нажимаем кнопку "Войти в аккаунт"
        login_button = wait_for_clickable(browser, MainPageLocators.LOGIN_BUTTON_MAIN)
        login_button.click()

        # Ожидание загрузки страницы входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )

        # Вход в аккаунт
        success = login_user(browser, registered_user['email'], registered_user['password'])
        assert success, "Login failed"

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверка, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed(), "Place order button is not displayed"

    def test_login_personal_account_button(self, browser, registered_user):
        """
        Проверка входа через кнопку «Личный кабинет»
        """
        # Нажимаем кнопку "Личный кабинет" на главной
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()

        # Ожидание загрузки страницы входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )

        # Вход в аккаунт
        success = login_user(browser, registered_user['email'], registered_user['password'])
        assert success, "Login failed"

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверка, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed(), "Place order button is not displayed"

    def test_login_register_form_button(self, browser, registered_user):
        """
        Проверка входа через кнопку в форме регистрации
        """
        # Переход на страницу регистрации
        browser.get(Urls.REGISTER_PAGE)
        wait_for_element(browser, RegisterPageLocators.REGISTER_BUTTON)

        # Нажимаем ссылку "Войти" на странице регистрации
        login_link = wait_for_clickable(browser, RegisterPageLocators.LOGIN_LINK)
        login_link.click()

        # Ожидание загрузки страницы входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )

        # Вход в аккаунт
        success = login_user(browser, registered_user['email'], registered_user['password'])
        assert success, "Login failed"

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверка, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed(), "Place order button is not displayed"

    def test_login_forgot_password_form_button(self, browser, registered_user):
        """
        Проверка входа через кнопку в форме восстановления пароля
        """
        # Переход на страницу восстановления пароля
        browser.get(Urls.FORGOT_PASSWORD_PAGE)
        wait_for_element(browser, ForgotPasswordPageLocators.RECOVER_BUTTON)

        # Нажимаем ссылку "Войти" на странице восстановления
        login_link = wait_for_clickable(browser, ForgotPasswordPageLocators.LOGIN_LINK)
        login_link.click()

        # Ожидание загрузки страницы входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )

        # Вход в аккаунт
        success = login_user(browser, registered_user['email'], registered_user['password'])
        assert success, "Login failed"

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверка, что кнопка "Оформить заказ" отображается
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed(), "Place order button is not displayed"

    def test_login_invalid_credentials(self, browser):
        """
        Проверка входа с неверными данными
        """
        browser.get(Urls.LOGIN_PAGE)
        wait_for_element(browser, LoginPageLocators.LOGIN_BUTTON)

        # Заполнение полей неверными данными
        email_input = wait_for_element(browser, LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys("invalid@test.com")

        password_input = wait_for_element(browser, LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys("wrongpassword")

        login_button = wait_for_clickable(browser, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Проверка, что мы остались на странице входа
        assert browser.current_url == Urls.LOGIN_PAGE

    @pytest.mark.parametrize("email, password, expected_url", [
        ("invalid@test.com", "wrongpassword", Urls.LOGIN_PAGE),
        ("test@test.com", "", Urls.LOGIN_PAGE),
        ("", "password123", Urls.LOGIN_PAGE),
        ("", "", Urls.LOGIN_PAGE)
    ])
    def test_login_with_invalid_credentials_parametrized(self, browser, email, password, expected_url):
        """
        Параметризованный тест для проверки входа с неверными данными
        """
        browser.get(Urls.LOGIN_PAGE)
        wait_for_element(browser, LoginPageLocators.LOGIN_BUTTON)

        # Заполнение полей
        email_input = wait_for_element(browser, LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

        password_input = wait_for_element(browser, LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

        login_button = wait_for_clickable(browser, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Проверка, что мы остались на странице входа
        assert browser.current_url == expected_url, f"Expected URL: {expected_url}, got: {browser.current_url}"

    def test_login_and_logout(self, browser, registered_user):
        """
        Проверка входа и выхода из аккаунта
        """
        # Вход в аккаунт
        browser.get(Urls.LOGIN_PAGE)
        success = login_user(browser, registered_user['email'], registered_user['password'])
        assert success, "Login failed"

        # Проверка, что мы на главной странице
        assert browser.current_url == Urls.MAIN_PAGE

        # Переход в личный кабинет
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()

        # Ожидание загрузки страницы личного кабинета
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.PROFILE_PAGE)
        )
        assert browser.current_url == Urls.PROFILE_PAGE

        # Нажимаем кнопку выхода
        logout_button = wait_for_clickable(browser, ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()

        # Ожидание перехода на страницу входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
        assert browser.current_url == Urls.LOGIN_PAGE
