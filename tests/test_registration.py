import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from urls import Urls
from helpers import generate_user_data


def register_user(browser, user_data):
    """
    Упрощенная функция регистрации пользователя
    Использует поиск по всем полям ввода на странице
    """
    # Переходим на страницу регистрации
    browser.get(Urls.REGISTER_PAGE)

    # Ждем загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Находим все поля ввода на странице
    try:
        inputs = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
        )
    except TimeoutException:
        # Если не нашли input, ищем другие элементы
        inputs = browser.find_elements(By.CSS_SELECTOR, "input")

    # Проверяем, что есть хотя бы 3 поля ввода
    if len(inputs) < 3:
        # Пробуем найти поля по другим селекторам
        inputs = browser.find_elements(By.XPATH, "//input[@type='text' or @type='email' or @type='password']")

    assert len(inputs) >= 3, f"Найдено только {len(inputs)} полей ввода. Ожидается минимум 3."

    # Заполняем поля по порядку: имя, email, пароль
    # Очищаем поля перед вводом
    inputs[0].clear()
    inputs[0].send_keys(user_data['name'])

    inputs[1].clear()
    inputs[1].send_keys(user_data['email'])

    inputs[2].clear()
    inputs[2].send_keys(user_data['password'])

    # Находим кнопку регистрации
    try:
        register_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"))
        )
    except TimeoutException:
        # Пробуем найти кнопку по классу
        register_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

    # Нажимаем кнопку регистрации
    register_button.click()


class TestRegistration:

    def test_successful_registration(self, browser):
        """
        Проверка успешной регистрации
        """
        user_data = generate_user_data()
        register_user(browser, user_data)

        # Проверяем, что перешли на страницу входа
        WebDriverWait(browser, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
        assert browser.current_url == Urls.LOGIN_PAGE
