from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import URLS

def test_navigation_to_personal_account(driver):
        # 1) Открываем главную страницу
        driver.get(URLS.homepage)

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
            EC.url_to_be(URLS.homepage)
        )

        # 8) Находит кнопку Личный Кабинет и кликаем по ней
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

