import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import Urls


class TestLogout:

    def test_login_and_logout(self, browser, registered_user):
        """Проверка входа и выхода из аккаунта"""
        # 1. Открываем страницу входа
        browser.get(Urls.LOGIN_PAGE)

        # 2. Ждем появления полей
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

        # 3. Заполняем поля
        inputs = browser.find_elements(By.TAG_NAME, "input")
        inputs[0].send_keys(registered_user['email'])
        inputs[1].send_keys(registered_user['password'])

        # 4. Нажимаем "Войти"
        for btn in browser.find_elements(By.TAG_NAME, "button"):
            if "войти" in btn.text.lower():
                btn.click()
                break

        # 5. Проверяем главную страницу
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))

        # 6. Нажимаем "Личный кабинет"
        for link in browser.find_elements(By.TAG_NAME, "a"):
            if "личный кабинет" in link.text.lower():
                link.click()
                break

        # 7. Проверяем профиль
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))

        # 8. Нажимаем "Выйти"
        for btn in browser.find_elements(By.TAG_NAME, "button"):
            if "выход" in btn.text.lower():
                btn.click()
                break

        # 9. Проверяем страницу входа
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert browser.current_url == Urls.LOGIN_PAGE