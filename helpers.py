# helpers.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def wait_for_element(browser, locator, timeout=10):
    """Ожидает появления элемента на странице"""
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_clickable(browser, locator, timeout=10):
    """Ожидает, когда элемент станет кликабельным"""
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def find_all_inputs(browser):
    """Находит все поля ввода на странице"""
    return browser.find_elements(By.TAG_NAME, "input")