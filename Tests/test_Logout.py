from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import URLS

class TestNavigationToPersonalAccountAndLogout:
    def test_navigation_to_personal_account_and_logout(self,driver):
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON_MAIN_PAGE)
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.loginpage)
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
            EC.url_to_be(URLS.homepage)
        )

        personal_account_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()


        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.loginpage)
        )

        assert driver.current_url == URLS.loginpage, f"Ожидался URL {URLS.loginpage}, а получен {driver.current_url}"
