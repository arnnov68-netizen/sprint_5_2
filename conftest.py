import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.common.exceptions import InvalidSessionIdException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from urls import Urls
from helpers import generate_user_data
import time


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
    driver = None
    max_retries = 3

    try:
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--allow-insecure-localhost")

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

        driver.implicitly_wait(10)

        # Попытка загрузить страницу с повторными попытками
        for attempt in range(max_retries):
            try:
                print(f"Attempt {attempt + 1}: Loading {Urls.MAIN_PAGE}")
                driver.get(Urls.MAIN_PAGE)
                print(f"Successfully loaded {Urls.MAIN_PAGE}")
                break
            except WebDriverException as e:
                if attempt < max_retries - 1:
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in 2 seconds...")
                    time.sleep(2)
                else:
                    raise

        yield driver

    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass


@pytest.fixture
def registered_user(browser):
    """Фикстура для создания зарегистрированного пользователя"""
    from tests.test_registration import register_user
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException

    user_data = generate_user_data()

    try:
        register_user(browser, user_data)
    except Exception as e:
        try:
            browser.save_screenshot("registration_error.png")
        except:
            pass
        raise AssertionError(f"Registration failed: {str(e)[:200]}")

    # Проверяем, что регистрация прошла успешно
    try:
        WebDriverWait(browser, 15).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
    except TimeoutException:
        try:
            browser.save_screenshot("registration_timeout.png")
        except:
            pass
        raise AssertionError("Registration timed out - didn't redirect to login page")

    yield user_data


@pytest.fixture
def logged_in_user(browser, registered_user):
    """Фикстура для авторизованного пользователя"""
    from tests.test_login import login_user
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from locators import MainPageLocators
    from selenium.common.exceptions import InvalidSessionIdException, TimeoutException

    try:
        success = login_user(browser, registered_user['email'], registered_user['password'])
        if not success:
            raise AssertionError("Login failed")
    except (InvalidSessionIdException, TimeoutException) as e:
        # Если сессия потеряна, пробуем перезапустить браузер
        try:
            browser.quit()
        except:
            pass
        raise AssertionError(f"Login failed due to session error: {e}")

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON)
        )
    except Exception as e:
        try:
            browser.save_screenshot("login_error.png")
        except:
            pass
        raise AssertionError(f"Login failed: {e}")

    yield registered_user
