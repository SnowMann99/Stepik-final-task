from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_items_in_basket()
        self.should_be_empty_basket_text()

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_TEXT), "Text about empty basket is not presented"
