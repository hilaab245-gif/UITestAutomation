import logging

from UI.locator import CheckOutLocators as CHECKOUT
from core.Base_page import base_page
from  Pages.CartPage import CartPage


class OrderComplete(base_page):
    def __init__(self, driver=None):
        super().__init__(driver=driver)
        self.verify_page_title("Checkout: Overview")
        self.cart_page = CartPage(driver)

    def verify_checkout_overview_details(self,item,sum):
            self.cart_page.verifyCartItems(item)
            sum_checkout =self.driver.find_element(*CHECKOUT.ITEM_TOTAL)
            sum_total = float(sum_checkout.text.strip().replace('Item total: $',''))
            assert sum_total == sum, f"Total mismatch. Expected {sum}, Found {sum_total}"

    def cancel_checkout(self):
        self.click_button(*CHECKOUT.CANCEL_BUTTON,"cancel checkout button" )
        self.driver.back()
    def finish_button_checkout(self):
        try:
            self.click_button(*CHECKOUT.FINISH_BUTTON, "Finish checkout button")
            self.verify_page_title("Checkout: Complete!")
            text=self.driver.find_element(*CHECKOUT.COMPLETE_TEXT).text.strip()
            if text == "Thank you for your order!":
                logging.info("Order Complete")
        except Exception as e:
            logging.exception(f"Checkout finish failed: {e}")
            raise RuntimeError (f"Checkout finish failed: {e}")



















