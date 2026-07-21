import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from urls import Urls
from helpers import generate_user_data
from tests.test_registration import register_user
from tests.test_login import login_user
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture
def browser(request):
    """Фикстура для создания экземпляра браузера"""
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--ignore-certificate-errors")
        if headless:
            options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(browser):
    """Фикстура для создания зарегистрированного пользователя"""
    user_data = generate_user_data()
    register_user(browser, user_data)

    WebDriverWait(browser, 10).until(
        EC.url_to_be(Urls.LOGIN_PAGE)
    )

    return user_data


@pytest.fixture
def logged_in_user(browser, registered_user):
    """Фикстура для авторизованного пользователя"""
    login_user(browser, registered_user['email'], registered_user['password'])

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
    )

    return registered_user
