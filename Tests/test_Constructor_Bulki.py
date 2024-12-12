from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators


class TestConstructorSections:
    def test_navigate_to_toppings(self,driver):
        driver.find_element(*ConstructorLocators.TOPPINGS_BUTTON).click()
        header_toppings = driver.find_element(*ConstructorLocators.TOPPINGS_HEADER)
        assert header_toppings.text == 'Начинки'
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.TOPPINGS_HEADER)
        )

    def test_navigate_to_sauces(self, driver):
        driver.find_element(*ConstructorLocators.SAUCES_BUTTON).click()
        header_sauces = driver.find_element(*ConstructorLocators.SAUCES_HEADER)
        assert header_sauces.text == 'Соусы'
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.SAUCES_HEADER)
        )

    def test_navigate_to_buns(self, driver):
        driver.find_element(*ConstructorLocators.TOPPINGS_BUTTON).click()
        driver.find_element(*ConstructorLocators.BUNS_BUTTON).click()
        header_bun = driver.find_element(*ConstructorLocators.BUNS_HEADER)
        assert header_bun.text == 'Булки'
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorLocators.BUNS_HEADER)
        )
