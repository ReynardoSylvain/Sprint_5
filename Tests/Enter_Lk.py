from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
import time

def test_navigation_to_personal_account():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        # 1) Открываем главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")

        # 2) Находит кнопку "Войти в аккаунт" на главной странице и кликаем по ней
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_MAIN_PAGE)
        )
        login_button.click()

        # 3) Ожидает загрузку страницы логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        # 4) Проверяет наличие полей для ввода данных
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Пароль"))
        )

        # 5) Вводит существующие данные для входа
        email_field.send_keys("userok3@yandex.ru")
        password_field.send_keys("123456")

        # 6) Кликает по кнопке логина
        login_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_submit_button.click()

        # 7) После авторизации проверяет, что вернулись на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_contains("/")
        )

        # 8) Находит кнопку Личный Кабинет и кликаем по ней
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        time.sleep(5)

        print("Тест: Переход в личный кабинет пройден успешно.")

    finally:
        driver.quit()

test_navigation_to_personal_account()
