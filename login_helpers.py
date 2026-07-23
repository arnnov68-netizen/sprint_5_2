from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordPageLocators,
    ProfilePageLocators
)
from urls import Urls
from helpers import wait_for_element, wait_for_clickable, find_all_inputs  # Импорт из helpers.py


class LoginHelpers:
    """Класс с вспомогательными методами для тестов входа"""

    def login_with_credentials(self, browser, email, password):
        """Выполняет вход с указанными учетными данными"""
        # Переход на страницу входа
        browser.get(Urls.LOGIN_PAGE)

        # Ждем загрузки страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Находим все поля ввода
        inputs = find_all_inputs(browser)
        if len(inputs) < 2:
            raise AssertionError("Не найдены поля ввода")

        # Заполняем поля
        inputs[0].clear()
        inputs[0].send_keys(email)
        inputs[1].clear()
        inputs[1].send_keys(password)

        # Нажимаем кнопку входа
        login_button = wait_for_clickable(browser, LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def click_login_button_main(self, browser):
        """Нажимает кнопку 'Войти в аккаунт' на главной странице"""
        button = wait_for_clickable(browser, MainPageLocators.LOGIN_BUTTON_MAIN)
        button.click()

        # Ожидаем перехода на страницу входа
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

    def login_from_main_page(self, browser, email, password):
        """Выполняет вход через кнопку на главной странице"""
        browser.get(Urls.MAIN_PAGE)
        wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)

        self.click_login_button_main(browser)
        self.login_with_credentials(browser, email, password)

    def login_from_personal_account(self, browser, email, password):
        """Выполняет вход через кнопку личного кабинета"""
        browser.get(Urls.MAIN_PAGE)
        wait_for_element(browser, MainPageLocators.PLACE_ORDER_BUTTON)

        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        self.login_with_credentials(browser, email, password)

    def login_from_register_page(self, browser, email, password):
        """Выполняет вход через ссылку на странице регистрации"""
        browser.get(Urls.REGISTER_PAGE)
        wait_for_element(browser, RegisterPageLocators.REGISTER_BUTTON)

        login_link = wait_for_clickable(browser, RegisterPageLocators.LOGIN_LINK)
        login_link.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        self.login_with_credentials(browser, email, password)

    def login_from_forgot_password_page(self, browser, email, password):
        """Выполняет вход через ссылку на странице восстановления пароля"""
        browser.get(Urls.FORGOT_PASSWORD_PAGE)
        wait_for_element(browser, ForgotPasswordPageLocators.RECOVER_BUTTON)

        login_link = wait_for_clickable(browser, ForgotPasswordPageLocators.LOGIN_LINK)
        login_link.click()

        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        self.login_with_credentials(browser, email, password)

    def logout(self, browser):
        """Выполняет выход из аккаунта"""
        # Переход в профиль
        personal_account = wait_for_clickable(browser, MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        personal_account.click()
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # Выход
        logout_button = wait_for_clickable(browser, ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()