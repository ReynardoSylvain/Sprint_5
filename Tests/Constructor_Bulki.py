from selenium import webdriver
import time
from locators import ConstructorLocators

class TestConstructorSections:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_navigate_to_constructor_sections(self):

        #Проверка нажатия на Начинки
        self.driver.find_element(*ConstructorLocators.TOPPINGS_BUTTON).click()
        header_toppings = self.driver.find_element(*ConstructorLocators.TOPPINGS_HEADER)
        assert header_toppings.text == 'Начинки'
        time.sleep(1)

        #Проверка нажатия на Начинки Соусы
        self.driver.find_element(*ConstructorLocators.SAUCES_BUTTON).click()
        header_sauces = self.driver.find_element(*ConstructorLocators.SAUCES_HEADER)
        assert header_sauces.text == 'Соусы'
        time.sleep(1)

        #Проверка нажатия на Булки
        self.driver.find_element(*ConstructorLocators.BUNS_BUTTON).click()
        header_bun = self.driver.find_element(*ConstructorLocators.BUNS_HEADER)
        assert header_bun.text == 'Булки'
        time.sleep(1)

    def teardown(self):
        #Закрытие браузера после теста
        self.driver.quit()

if __name__ == "__main__":
    test = TestConstructorSections()
    test.setup()
    test.test_navigate_to_constructor_sections()
    test.teardown()
