from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-add-to-basket")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'a.btn[href$="/basket/"]')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "div#content_inner > p ")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
