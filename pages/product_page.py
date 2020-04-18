from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        ADD_TO_BASKET = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        ADD_TO_BASKET.click()

    def should_be_success_add_msg(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), "Success message is not presented"

    def should_be_msg_name_matches_product_name(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_NAME).text, "Product name in basket != Product name on catalog!"

    def should_be_basket_total_msg(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Basket total message is not presented"

    def should_be_product_price_matches_basket_total(self):
        assert self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, "Product price != Basket total price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), "Success message is not disappeared"
