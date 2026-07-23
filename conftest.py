import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
import uuid


@pytest.fixture
def browser():
    """Фикстура для создания и закрытия браузера"""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(browser):
    """Создает нового пользователя через UI"""
    # Генерируем уникальные данные
    unique_id = str(uuid.uuid4())[:8]
    email = f"test_user_{unique_id}@test.com"
    password = "Password123!"

    # Открываем страницу регистрации
    browser.get(Urls.REGISTER_PAGE)

    # Ждем загрузки
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Находим все поля ввода
    inputs = WebDriverWait(browser, 10).until(
        lambda driver: driver.find_elements(By.TAG_NAME, "input")
    )

    # Проверяем, что есть поля
    assert len(inputs) >= 3, "Найдено меньше 3 полей ввода"

    # Заполняем поля по порядку: имя, email, пароль
    inputs[0].clear()
    inputs[0].send_keys("Test User")

    inputs[1].clear()
    inputs[1].send_keys(email)

    inputs[2].clear()
    inputs[2].send_keys(password)

    # Нажимаем кнопку регистрации
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
    )
    register_button.click()

    # Ждем перехода на страницу входа
    WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))

    return {
        'email': email,
        'password': password
    }