import random

def generate_unique_email():
    #генерация случайной почты в формате user****
    return f"user{random.randint(1000, 9999)}@yandex.ru"

def generate_unique_username():
    #генерация случайного имя пользователя в формате user****
    return f"user{random.randint(1000, 9999)}"
