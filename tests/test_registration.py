import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import Urls
import uuid


class TestRegistration:

    def test_successful_registration(self, browser):
        """Проверка успешной регистрации"""
        # 1. Генерируем уникальные данные пользователя
        unique_id = str(uuid.uuid4())[:8]
        email = f"test_user_{unique_id}@test.com"
        password = "Password123!"
        name = "Test User"

        # 2. Открываем страницу регистрации
        browser.get(Urls.REGISTER_PAGE)

        # 3. Ждем загрузки страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 4. Находим поля ввода
        inputs = WebDriverWait(browser, 10).until(
            lambda driver: driver.find_elements(By.TAG_NAME, "input")
        )

        # Проверяем, что есть хотя бы 3 поля
        assert len(inputs) >= 3, "Найдено меньше 3 полей ввода"

        # 5. Заполняем поля (имя, email, пароль)
        inputs[0].clear()
        inputs[0].send_keys(name)

        inputs[1].clear()
        inputs[1].send_keys(email)

        inputs[2].clear()
        inputs[2].send_keys(password)

        # 6. Нажимаем кнопку "Зарегистрироваться"
        register_button = None
        for btn in browser.find_elements(By.TAG_NAME, "button"):
            if "зарегистрироваться" in btn.text.lower():
                register_button = btn
                break

        assert register_button is not None, "Кнопка 'Зарегистрироваться' не найдена"
        register_button.click()

        # 7. Проверяем переход на страницу входа
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert browser.current_url == Urls.LOGIN_PAGE