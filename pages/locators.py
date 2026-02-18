from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[text()='Add to basket']")

    NAME = (By.CSS_SELECTOR, ".product_main h1")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3) strong")