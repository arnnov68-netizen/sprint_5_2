import random
import string

def generate_random_email():
    """Генерирует email вида: имя_фамилия_когорта_3цифры@домен"""
    name = "test"
    surname = "user"
    cohort = "5"  # Укажи номер своей когорты
    digits = ''.join(random.choices(string.digits, k=3))
    domain = "yandex.ru"
    return f"{name}_{surname}_{cohort}_{digits}@{domain}"

def generate_random_password(length=6):
    """Генерирует пароль заданной длины (по умолчанию 6 символов)"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_invalid_password():
    """Генерирует пароль короче 6 символов"""
    return ''.join(random.choices(string.ascii_letters, k=5))