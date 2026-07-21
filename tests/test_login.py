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


def login_user(browser, email, password):
    """Вспомогательная функция для входа в аккаунт"""
    # Переход на страницу входа
    browser.get(Urls.LOGIN_PAGE)

    # Ждем загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Находим все поля ввода
    inputs = find_all_inputs(browser)
    assert len(inputs) >= 2, "Не найдены поля ввода"

    # Заполняем поля
    inputs[0].clear()
    inputs[0].send_keys(email)
    inputs[1].clear()
    inputs[1].send_keys(password)

    # Нажимаем кнопку входа
    login_button = wait_for_clickable(browser, LoginPageLocators.LOGIN_BUTTON)
    login_button.click()

    # Проверяем успешность входа
    try:
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )
        return True
    except TimeoutException:
        return False


def click_login_button_main(browser):
    """Нажать кнопку 'Войти в аккаунт' на главной странице"""
    try:
        # Пробуем основной локатор
        button = wait_for_clickable(browser, MainPageLocators.LOGIN_BUTTON_MAIN)
        button.click()
    except TimeoutException:
        try:
            # Пробуем альтернативный локатор
            button = wait_for_clickable(browser, MainPageLocators.LOGIN_BUTTON_MAIN_ALT)
            button.click()
        except TimeoutException:
            # Пробуем найти кнопку через JavaScript
            browser.execute_script("""
                var buttons = document.querySelectorAll('button');
                for (var i = 0; i < buttons.length; i++) {
                    if (buttons[i].textContent.includes('Войти в аккаунт') || 
                        buttons[i].textContent.includes('Войти')) {
                        buttons[i].click();
                        break;
                    }
                }
            """)


class TestLogin:

    def test_login_main_button(self, browser, registered_user):
        """Проверка входа по кнопке «Войти в аккаунт» на главной странице"""
        # Нажимаем кнопку "Войти в аккаунт"
        click_login_button_main(browser)

        # Ждем перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

        # Вход в аккаунт
        login_user(browser, registered_user['email'], registered_user['password'])

        # Проверяем переход на главную
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        # Проверяем наличие кнопки оформления заказа
        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_login_personal_account_button(self, browser, registered_user):
        """Проверка входа через кнопку «Личный кабинет»"""
        # Нажимаем "Личный кабинет"
        try:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        except TimeoutException:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON_ALT)
        personal_account.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

        login_user(browser, registered_user['email'], registered_user['password'])

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_login_register_form_button(self, browser, registered_user):
        """Проверка входа через ссылку в форме регистрации"""
        browser.get(Urls.REGISTER_PAGE)
        wait_for_element(browser, RegisterPageLocators.REGISTER_BUTTON)

        login_link = wait_for_clickable(browser, RegisterPageLocators.LOGIN_LINK)
        login_link.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

        login_user(browser, registered_user['email'], registered_user['password'])

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_login_forgot_password_form_button(self, browser, registered_user):
        """Проверка входа через ссылку в форме восстановления пароля"""
        browser.get(Urls.FORGOT_PASSWORD_PAGE)
        wait_for_element(browser, ForgotPasswordPageLocators.RECOVER_BUTTON)

        login_link = wait_for_clickable(browser, ForgotPasswordPageLocators.LOGIN_LINK)
        login_link.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

        login_user(browser, registered_user['email'], registered_user['password'])

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        place_order_button = wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)
        assert place_order_button.is_displayed()

    def test_login_invalid_credentials(self, browser):
        """Проверка входа с неверными данными"""
        browser.get(Urls.LOGIN_PAGE)
        wait_for_element(browser, LoginPageLocators.LOGIN_BUTTON)

        inputs = find_all_inputs(browser)
        inputs[0].clear()
        inputs[0].send_keys("invalid@test.com")
        inputs[1].clear()
        inputs[1].send_keys("wrongpassword")

        login_button = wait_for_clickable(browser, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        # Остаемся на странице входа
        assert browser.current_url == Urls.LOGIN_PAGE

    @pytest.mark.parametrize("email, password", [
        ("invalid@test.com", "wrongpassword"),
        ("test@test.com", ""),
        ("", "password123"),
        ("", "")
    ])
    def test_login_with_invalid_credentials_parametrized(self, browser, email, password):
        """Параметризованный тест входа с неверными данными"""
        browser.get(Urls.LOGIN_PAGE)
        wait_for_element(browser, LoginPageLocators.LOGIN_BUTTON)

        inputs = find_all_inputs(browser)
        inputs[0].clear()
        inputs[0].send_keys(email)
        inputs[1].clear()
        inputs[1].send_keys(password)

        login_button = wait_for_clickable(browser, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

        assert browser.current_url == Urls.LOGIN_PAGE

    def test_login_and_logout(self, browser, registered_user):
        """Проверка входа и выхода из аккаунта"""
        # Вход
        browser.get(Urls.LOGIN_PAGE)
        login_user(browser, registered_user['email'], registered_user['password'])

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        # Переход в профиль
        try:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        except TimeoutException:
            personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON_ALT)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Выход
        logout_button = wait_for_clickable(browser, ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert browser.current_url == Urls.LOGIN_PAGE
