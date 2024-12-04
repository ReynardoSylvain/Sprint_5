from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from locators import MainPageLocators
import time

def test_navigation_to_personal_account_and_logo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_MAIN_PAGE)
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Пароль"))
        )

        email_field.send_keys("userok3@yandex.ru")
        password_field.send_keys("123456")

        login_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/")
        )

        personal_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        time.sleep(2)

        logo_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGO_BUTTON)
        )
        logo_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/")
        )
        time.sleep(5)

        print("Тест: Переход в личный кабинет и клик по логотипу пройден успешно.")

    finally:
        driver.quit()

test_navigation_to_personal_account_and_logo()
