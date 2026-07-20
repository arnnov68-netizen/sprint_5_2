class Urls:
    """URL-адреса приложения Stellar Burgers"""
    BASE_URL = "https://stellarburgers.education-services.ru"

    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    REGISTER_PAGE = f"{BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    ACCOUNT_PAGE = f"{BASE_URL}/account"
    ORDER_FEED_PAGE = f"{BASE_URL}/feed"

    # API эндпоинты (если понадобятся)
    API_BASE = f"{BASE_URL}/api"
    API_REGISTER = f"{API_BASE}/auth/register"
    API_LOGIN = f"{API_BASE}/auth/login"
    API_USER = f"{API_BASE}/auth/user"
    API_ORDERS = f"{API_BASE}/orders"
    API_INGREDIENTS = f"{API_BASE}/ingredients"
