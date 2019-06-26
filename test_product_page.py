from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
import pytest
import time

testdata = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


# @pytest.mark.parametrize('link', testdata)
# def test_guest_can_add_product_to_cart(browser, link):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.add_item_to_bascket()
#     product_page.solve_quiz_and_get_code()
#     product_page.check_add_item_to_basket()


# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
