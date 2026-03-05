from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def test_guest_cant_see_product_in_basket_opened_from_page(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_FORM), "Basket form is presented, but should not be"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"