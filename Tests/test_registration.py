from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from urls import URLS
from helper import generate_unique_email, generate_unique_username

class TestRegistration:
    def test_successful_registration(self,driver):
        # новые переменные где хранятся сгенерированные данные из helper.py
        username = generate_unique_username()
        email = generate_unique_email()

        driver.get(URLS.registerpage)
        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(username)
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.loginpage)
        )
        assert driver.current_url == URLS.loginpage, f"Ожидался URL {URLS.loginpage}, а получен {driver.current_url}"

    def test_registration_invalid_password(self,driver):

        username = generate_unique_username()
        email = generate_unique_email()

        driver.get(URLS.registerpage)
        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(username)
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # проверка что не произошло регистрации из за неверного введенных данных
        WebDriverWait(driver, 10).until(
                EC.url_to_be(URLS.registerpage)
        )

        assert driver.current_url == URLS.registerpage, f"Ожидался URL {URLS.registerpage}, а получен {driver.current_url}"
