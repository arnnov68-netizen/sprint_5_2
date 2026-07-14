import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import generate_random_email, generate_random_password
from locators import BASE_URL

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--headless')  # раскомментировать для headless-режима
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def new_user_data():
    """Возвращает данные для регистрации нового пользователя"""
    return {
        'name': 'Тестовый',
        'email': generate_random_email(),
        'password': generate_random_password()
    }