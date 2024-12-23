from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import URLS

class TestNavigationToPersonalAccount:
    def test_navigation_to_personal_account(self,driver):
        # 1) Находит кнопку "Войти в аккаунт" на главной странице и кликаем по ней
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_MAIN_PAGE)
        )
        login_button.click()

        # 2) Ожидает загрузку страницы логина
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        # 3) Проверяет наличие полей для ввода данных
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Пароль"))
        )

        # 4) Вводит существующие данные для входа
        email_field.send_keys("userok3@yandex.ru")
        password_field.send_keys("123456")

        # 5) Кликает по кнопке логина
        login_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_submit_button.click()

        # 6) После авторизации проверяет, что вернулись на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.homepage)
        )

        # 7) Находит кнопку Личный Кабинет и кликаем по ней
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("personal_account")
        )
        assert URLS.personal_account in driver.current_url, f"Ожидался URL, содержащий {URLS.personal_account}, а получен {driver.current_url}"



