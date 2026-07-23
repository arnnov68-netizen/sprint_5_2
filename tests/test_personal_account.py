import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import Urls


class TestPersonalAccount:

    def test_go_to_personal_account(self, browser, registered_user):
        """Проверка перехода в личный кабинет"""
        # 1. Вход
        browser.get(Urls.LOGIN_PAGE)
        inputs = WebDriverWait(browser, 10).until(
            lambda driver: driver.find_elements(By.TAG_NAME, "input")
        )
        inputs[0].send_keys(registered_user['email'])
        inputs[1].send_keys(registered_user['password'])

        for btn in browser.find_elements(By.TAG_NAME, "button"):
            if "войти" in btn.text.lower():
                btn.click()
                break
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.MAIN_PAGE))

        # 2. Нажимаем "Личный кабинет"
        for link in browser.find_elements(By.TAG_NAME, "a"):
            if "личный кабинет" in link.text.lower():
                link.click()
                break

        # 3. Проверяем профиль
        WebDriverWait(browser, 10).until(EC.url_to_be(Urls.PROFILE_PAGE))
        assert browser.current_url == Urls.PROFILE_PAGE