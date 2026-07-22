from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный кабинет']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Конструктор
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    EMAIL_INPUT = (By.NAME, "name")  # или (By.XPATH, "//input[@type='email']")
    PASSWORD_INPUT = (By.NAME, "Пароль")  # или (By.XPATH, "//input[@type='password']")


class RegisterPageLocators:
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "name")  # уточните
    PASSWORD_INPUT = (By.NAME, "Пароль")  # уточните


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")