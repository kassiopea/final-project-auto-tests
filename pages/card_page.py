from .base_page import BasePage
from .locators import CardPageLocators


class CardPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_items_in_the_basket()
        self.shout_be_text_empty_basket()

    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*CardPageLocators.BASKET_ITEMS), \
            "Success message is presented, but should not be"

    def shout_be_text_empty_basket(self):
        text_message_in_basket = self.browser.find_element(*CardPageLocators.MESSAGE_IN_BASKET).text
        assert "Your basket is empty" in text_message_in_basket, \
            "The basket not exist the message that basket is empty"

