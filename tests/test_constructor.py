import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from urls import Urls
from helpers import wait_for_element, wait_for_clickable, wait_for_url


class TestConstructor:

    def test_switch_to_buns_tab(self, browser):
        """
        Проверка перехода к разделу «Булки»
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Переключение на вкладку "Соусы" для проверки переключения обратно
        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].click();", sauces_tab)

        # Проверяем, что вкладка "Соусы" стала активной
        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text, f"Expected 'Соусы' tab to be active, got '{active_tab.text}'"

        # Переключение на вкладку "Булки"
        buns_tab = wait_for_element(browser, MainPageLocators.BUNS_TAB)
        browser.execute_script("arguments[0].click();", buns_tab)

        # Проверка, что вкладка "Булки" стала активной
        WebDriverWait(browser, 5).until(
            lambda driver: "Булки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text, f"Expected 'Булки' tab to be active, got '{active_tab.text}'"

    def test_switch_to_sauces_tab(self, browser):
        """
        Проверка перехода к разделу «Соусы»
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Переключение на вкладку "Соусы"
        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].click();", sauces_tab)

        # Проверка, что вкладка "Соусы" стала активной
        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text, f"Expected 'Соусы' tab to be active, got '{active_tab.text}'"

    def test_switch_to_fillings_tab(self, browser):
        """
        Проверка перехода к разделу «Начинки»
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Переключение на вкладку "Начинки"
        fillings_tab = wait_for_element(browser, MainPageLocators.FILLINGS_TAB)
        browser.execute_script("arguments[0].click();", fillings_tab)

        # Проверка, что вкладка "Начинки" стала активной
        WebDriverWait(browser, 5).until(
            lambda driver: "Начинки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text, f"Expected 'Начинки' tab to be active, got '{active_tab.text}'"

    def test_tabs_switch_sequentially(self, browser):
        """
        Проверка последовательного переключения между всеми вкладками
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Функция для клика по вкладке через JavaScript
        def click_tab_with_js(tab_locator, expected_name):
            tab_element = wait_for_element(browser, tab_locator)
            # Прокручиваем к элементу
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab_element)
            # Кликаем через JavaScript
            browser.execute_script("arguments[0].click();", tab_element)
            # Ожидаем, что вкладка станет активной
            WebDriverWait(browser, 5).until(
                lambda driver: expected_name in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
            )

        # Сначала переключаемся на "Соусы"
        click_tab_with_js(MainPageLocators.SAUCES_TAB, "Соусы")

        # Список вкладок для проверки
        tabs = [
            (MainPageLocators.FILLINGS_TAB, "Начинки"),
            (MainPageLocators.BUNS_TAB, "Булки"),
            (MainPageLocators.SAUCES_TAB, "Соусы")
        ]

        for tab_locator, tab_name in tabs:
            click_tab_with_js(tab_locator, tab_name)

            # Проверка, что вкладка активна
            active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
            assert tab_name in active_tab.text, \
                f"Expected '{tab_name}' tab to be active, got '{active_tab.text}'"

    @pytest.mark.parametrize("tab_locator, tab_name", [
        (MainPageLocators.SAUCES_TAB, "Соусы"),
        (MainPageLocators.FILLINGS_TAB, "Начинки"),
        (MainPageLocators.BUNS_TAB, "Булки")
    ])
    def test_switch_to_tab(self, browser, tab_locator, tab_name):
        """
        Параметризованный тест для проверки переключения на любую вкладку
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Для вкладки "Булки" сначала переключаемся на другую вкладку
        if tab_name == "Булки":
            # Переключаемся на "Соусы", чтобы убрать активность с "Булок"
            sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
            browser.execute_script("arguments[0].click();", sauces_tab)
            WebDriverWait(browser, 5).until(
                lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
            )

        # Находим вкладку и кликаем через JavaScript
        tab_div = wait_for_element(browser, tab_locator)
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab_div)
        browser.execute_script("arguments[0].click();", tab_div)

        # Ожидаем изменения активного таба
        WebDriverWait(browser, 5).until(
            lambda driver: tab_name in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )

        # Проверка, что вкладка стала активной
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert tab_name in active_tab.text, \
            f"Expected '{tab_name}' tab to be active, got '{active_tab.text}'"

    def test_tab_switching_with_actions(self, browser):
        """
        Проверка переключения вкладок с использованием ActionChains
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Сначала переключаемся на "Соусы"
        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", sauces_tab)

        actions = ActionChains(browser)
        actions.move_to_element(sauces_tab).click().perform()

        # Проверяем, что переключились на "Соусы"
        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )

        # Список вкладок для проверки
        tabs = [
            (MainPageLocators.FILLINGS_TAB, "Начинки"),
            (MainPageLocators.BUNS_TAB, "Булки"),
            (MainPageLocators.SAUCES_TAB, "Соусы")
        ]

        for tab_locator, tab_name in tabs:
            tab_div = wait_for_element(browser, tab_locator)

            # Прокручиваем к элементу
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab_div)

            # Создаем новый ActionChains для каждого клика
            actions = ActionChains(browser)
            actions.move_to_element(tab_div).click().perform()

            # Ожидаем изменения активного таба
            WebDriverWait(browser, 5).until(
                lambda driver: tab_name in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
            )

            # Проверяем, что вкладка стала активной
            active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
            assert tab_name in active_tab.text, \
                f"Expected '{tab_name}' tab to be active, got '{active_tab.text}'"

    def test_click_on_active_tab_does_nothing(self, browser):
        """
        Проверка, что клик по уже активной вкладке не вызывает ошибку
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Получаем текущую активную вкладку (должна быть "Булки")
        active_tab_before = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab_before.text, "Buns tab should be active by default"

        # Пытаемся кликнуть по вкладке "Булки" (уже активна)
        buns_tab = wait_for_element(browser, MainPageLocators.BUNS_TAB)

        # Клик через JavaScript не должен вызывать ошибку
        browser.execute_script("arguments[0].click();", buns_tab)

        # Проверяем, что вкладка "Булки" все еще активна
        active_tab_after = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab_after.text, "Buns tab should remain active"

    def test_switch_to_tab_with_wait_for_attribute_change(self, browser):
        """
        Проверка переключения вкладок с ожиданием изменения атрибута
        """
        # Ожидание загрузки главной страницы
        wait_for_element(browser, MainPageLocators.CONSTRUCTOR_TITLE)

        # Переключаемся на "Соусы"
        sauces_tab = wait_for_element(browser, MainPageLocators.SAUCES_TAB)
        browser.execute_script("arguments[0].click();", sauces_tab)

        # Проверяем, что вкладка "Соусы" стала активной
        WebDriverWait(browser, 5).until(
            lambda driver: "Соусы" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text, "Sauces tab should be active"

        # Переключаемся на "Начинки"
        fillings_tab = wait_for_element(browser, MainPageLocators.FILLINGS_TAB)
        browser.execute_script("arguments[0].click();", fillings_tab)

        # Ждем изменения активной вкладки
        WebDriverWait(browser, 5).until(
            lambda driver: "Начинки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text, "Fillings tab should be active"

        # Переключаемся на "Булки"
        buns_tab = wait_for_element(browser, MainPageLocators.BUNS_TAB)
        browser.execute_script("arguments[0].click();", buns_tab)

        # Ждем изменения активной вкладки
        WebDriverWait(browser, 5).until(
            lambda driver: "Булки" in driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        )
        active_tab = wait_for_element(browser, MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text, "Buns tab should be active"
