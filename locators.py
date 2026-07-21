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
    LOGIN_BUTTON_MAIN_ALT = (By.XPATH, "//button[contains(@class, 'button') and contains(text(), 'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")
    PERSONAL_ACCOUNT_BUTTON_ALT = (By.XPATH, "//p[contains(text(), 'Личный кабинет')]/parent::a")


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
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")


class ProfilePageLocators:
    """Локаторы для страницы личного кабинета"""
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

    # Исправленные локаторы для навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/') and contains(text(), 'Конструктор')]")
    CONSTRUCTOR_BUTTON_ALT = (By.XPATH,
                              "//a[contains(@class, 'AppHeader_header__link')][.//p[contains(text(), 'Конструктор')]]")

    LOGO = (By.XPATH, "//a[contains(@class, 'AppHeader_header__logo')]")
    LOGO_ALT = (By.XPATH,
                "//a[contains(@href, '/')]//*[local-name()='svg' and contains(@class, 'AppHeader_header__logo')]/parent::a")

    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
