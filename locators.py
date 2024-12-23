from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка Личный Кабинет
    LOGO_BUTTON = (By.CSS_SELECTOR, "a > svg")  # Логотип
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка Конструктор


class LoginPageLocators:
    # Локатор кнопки Войти в аккаунт на главной странице
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Локатор кнопки Личный кабинет на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Локатор кнопки Войти в форме регистрации
    LOGIN_BUTTON_IN_REGISTRATION_FORM = (By.CLASS_NAME, "Auth_link__1fOlj")
    # Локатор кнопки Войти в форме восстановления пароля
    LOGIN_BUTTON_IN_PASSWORD_RECOVERY_FORM = (By.CLASS_NAME, "Auth_link__1fOlj")
    # Локатор поля ввода email
    EMAIL_FIELD = (By.NAME, "name")
    # Локатор поля ввода пароля
    PASSWORD_FIELD = (By.NAME, "Пароль")
    # Локатор кнопки входа на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Локатор кнопки выхода на странице входа
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class RegistrationPageLocators:
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

class ConstructorLocators:
    # Локаторы для кнопок
    BUNS_BUTTON = (By.XPATH, ".//span[text()='Булки']/parent::*")
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    TOPPINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    # Локаторы для заголовков
    BUNS_HEADER = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
    SAUCES_HEADER = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    TOPPINGS_HEADER = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
