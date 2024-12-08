from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from urls import URLS
from helper import generate_unique_email, generate_unique_username

def test_successful_registration(driver):

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

def test_registration_invalid_password(driver):

        username = generate_unique_username()
        email = generate_unique_email()

        driver.get(URLS.registerpage)
        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(username)
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
