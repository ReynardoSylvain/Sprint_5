import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators


def test_successful_registration():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("userok3")

        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys("userok3@yandex.ru")

        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123456")

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        time.sleep(7)

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        print("Тест успешной регистрации пройден")
    finally:
        driver.quit()


def test_registration_invalid_password():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("userok33")

        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys("userok33@yandex.ru")

        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123")

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        time.sleep(7)

        print("Тест с паролем менее 3 символов пройден")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_successful_registration()
    test_registration_invalid_password()
