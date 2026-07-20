from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

    # Вкладки
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab')][.//span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab')][.//span[text()='Соусы']]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab')][.//span[text()='Начинки']]")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

    # Кнопки
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")

    # Секции
    BUNS_SECTION = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    FILLINGS_SECTION = (By.XPATH, "//h2[contains(text(), 'Начинки')]")


class LoginPageLocators:
    """Локаторы для страницы входа"""
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class RegisterPageLocators:
    """Локаторы для страницы регистрации"""
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")


class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class ProfilePageLocators:
    """Локаторы для страницы личного кабинета (профиля)"""
    # Основные элементы
    PROFILE_NAME = (By.XPATH, "//p[contains(@class, 'text') and contains(text(), 'Имя')]/following-sibling::p")
    PROFILE_EMAIL = (By.XPATH, "//p[contains(@class, 'text') and contains(text(), 'Email')]/following-sibling::p")

    # Кнопки и ссылки
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(text(), 'Конструктор')]")
    LOGO = (By.XPATH, "//a[contains(@class, 'AppHeader_header__logo')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")

    # Поля для редактирования профиля
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    # Кнопки действий
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Отмена')]")
