from UI.locator import CheckoutUserLocators as CheckoutUser
from core.Base_page import base_page
from  Pages.CartPage import CartPage


class CheckoutInformation(base_page):
    def __init__(self, driver=None):
        super().__init__(driver=driver)
        self.cart_page = CartPage(driver)

    def cancel_button(self):
        self.click_button(*CheckoutUser.CANCEL_BUTTON, "cancel button ")
        self.cart_page.checkout_button()

    def user_data_order(self, arr):
        first, lastname, zipcode = arr
        self.send_key(*CheckoutUser.FIRST_NAME, first, "First Name")
        self.send_key(*CheckoutUser.LAST_NAME, lastname, "Last Name")
        self.send_key(*CheckoutUser.ZIP_CODE, zipcode, "zipcode")


    def click_but_contion(self):
         self.click_button(*CheckoutUser.CONTINUE_BUTTON, "continue button ")
         self.error_mes()
