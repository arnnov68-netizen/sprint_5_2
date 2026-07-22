from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import platform


def get_chrome_driver():
    """Получение драйвера Chrome с правильной настройкой для Windows"""
    system = platform.system()

    if system == "Windows":
        # Для Windows используем специальную настройку
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service as ChromeService

        # Очищаем кэш webdriver-manager
        cache_path = os.path.expanduser("~/.wdm")
        if os.path.exists(cache_path):
            import shutil
            try:
                shutil.rmtree(cache_path)
            except:
                pass

        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(service=service, options=options)
    else:
        # Для других ОС
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        return webdriver.Chrome(service=service, options=options)