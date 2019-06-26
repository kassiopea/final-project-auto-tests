from selenium.webdriver.common.by import By


# class MainPageLocators(object):
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_AFTER_ADD_ITEM = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    TITLE_OF_THE_ITEM = (By.CSS_SELECTOR, "h1")
    PRICE_ITEM = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CardPageLocators(object):
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#content_inner")
