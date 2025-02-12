from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import URLS

class TestLoginFromPasswordRecoveryPage:
    def test_login_from_password_recovery_form(self,driver):
        driver.get(URLS.forgotpasspage)

        # 2. Находим кнопку Войти в форме восстановления пароля
        recovery_login_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON_IN_PASSWORD_RECOVERY_FORM)
        )

        # 3. Кликаем на кнопку Войти
        recovery_login_button.click()

        # 4. Ожидаем, что мы окажемся на странице входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.loginpage)
        )

        # 5. Проверяем наличие полей для ввода email и пароля
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "Пароль"))
        )

        # 6. Вводим существующие данные для входа
        email_field.send_keys("userok3@yandex.ru")
        password_field.send_keys("123456")

        # 7. Кликаем по кнопке Войти
        login_submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLS.homepage)
        )
        assert driver.current_url == URLS.homepage, f"Ожидался URL {URLS.homepage}, а получен {driver.current_url}"
