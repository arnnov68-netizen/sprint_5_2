from selenium.webdriver.common.by import By

# URL
BASE_URL = "https://stellarburgers.education-services.ru"

# Главная страница
LOGIN_ACCOUNT_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка «Личный кабинет»

# Регистрация
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться»
REGISTER_HEADER = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок страницы регистрации
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/parent::div//input")  # Поле ввода имени
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::div//input")  # Поле ввода email
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div//input")  # Поле ввода пароля
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Ошибка некорректного пароля

# Вход
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::div//input")  # Поле email на странице входа
LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div//input")  # Поле пароля на странице входа
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
LOGIN_FROM_REGISTER_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» на странице регистрации
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»
LOGIN_FROM_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти» на странице восстановления пароля

# Личный кабинет
ACCOUNT_HEADER = (By.XPATH, "//h2[text()='Личный кабинет']")  # Заголовок личного кабинета
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка «Выйти»

# Конструктор
CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@href='/constructor']")  # Кнопка «Конструктор»
LOGO = (By.XPATH, "//a[contains(@class, 'logo')]")  # Логотип Stellar Burgers
BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::button")  # Вкладка «Булки»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::button")  # Вкладка «Соусы»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::button")  # Вкладка «Начинки»
ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")  # Активная вкладка