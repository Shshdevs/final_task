from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.NAME_IN_MESSAGE))
        self.should_be_equal_product_name()
        self.should_be_equal_product_price()
    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_equal_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, f"Product name in message is not equal to product name on page: expected {product_name}, got {product_name_in_message}"

    def should_be_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert product_price == product_price_in_message, f"Product price in message is not equal to product price on page: expected {product_price}, got {product_price_in_message}"