import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import Urls


class TestLogin:

    def test_login(self, browser, registered_user):
        """Проверка входа в аккаунт"""
        # 1. Открываем страницу входа
        browser.get(Urls.LOGIN_PAGE)

        # 2. Ждем загрузки страницы
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 3. Находим поля ввода
        inputs = WebDriverWait(browser, 10).until(
            lambda driver: driver.find_elements(By.TAG_NAME, "input")
        )

        # Проверяем, что есть хотя бы 2 поля
        """
        Возможно assert лишний. Так как ожидания данной проверки в задании я не нашёл.
        """
        #assert len(inputs) >= 2, "Найдено меньше 2 полей ввода"

        # 4. Заполняем поля
        inputs[0].clear()
        inputs[0].send_keys(registered_user['email'])

        inputs[1].clear()
        inputs[1].send_keys(registered_user['password'])

        # 5. Нажимаем кнопку "Войти"
        """
        Ниже происходит поиск кнопки входа. Думаю ревьюер ожидает более простого локатора для данного случая
        """
        login_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH,"//button[text()='Войти']"))
        )
        # login_button = None
        # for btn in browser.find_elements(By.TAG_NAME, "button"):
        #     if "войти" in btn.text.lower():
        #         login_button = btn
        #         break
        """
        Проверка ниже является лишней, т.к. при провале поиска по функции EC.presence_of_element_located
        driver выдаст ошибку
        """
        #assert login_button is not None, "Кнопка 'Войти' не найдена"
        login_button.click()

        # 6. Проверяем переход на главную страницу
        WebDriverWait(browser, 15).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert browser.current_url == Urls.MAIN_PAGE

        # 7. Проверяем, что пользователь авторизован
        # Ищем кнопку "Оформить заказ" - она появляется только для авторизованных пользователей
        order_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не видна, пользователь не авторизован"
