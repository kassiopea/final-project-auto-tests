from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_bascket()
    product_page.solve_quiz_and_get_code()
    product_page.check_add_item_to_basket()

