from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import random
import string


def wait_for_element(browser, locator, timeout=10):
    """Ожидание появления элемента на странице"""
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_clickable(browser, locator, timeout=10):
    """Ожидание кликабельности элемента"""
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_url(browser, url, timeout=10):
    """Ожидание определенного URL"""
    return WebDriverWait(browser, timeout).until(
        EC.url_to_be(url)
    )


def find_input_by_placeholder(browser, placeholder_text, timeout=10):
    """Поиск поля ввода по placeholder"""
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='{placeholder_text}']"))
    )


def find_all_inputs(browser, timeout=10):
    """Поиск всех полей ввода на странице"""
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
    )


def generate_user_data():
    """Генерация данных для нового пользователя"""

    def generate_random_string(length=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    return {
        'name': generate_random_string(6),
        'email': f"{generate_random_string(8)}@testmail.com",
        'password': generate_random_string(10)
    }


def generate_invalid_password():
    """Генерация неверного пароля для тестов"""
    return "wrong_password_123"
