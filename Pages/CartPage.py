
import logging
from core.Base_page import base_page
from UI.locator import CartLocators
#לרשום פונקציה מחיקה מהעגלה
class CartPage(base_page):
    def __init__(self, driver=None):
        super().__init__(driver=driver)

    def cart_button(self):
            logging.info("Navigating to the Cart page")
            self.click_button(*CartLocators.CART_BUTTON,"Cart button")

    def verifyCartItems(self,item):
            logging.info("Starting cart validation ")
            carts = self.driver.find_element(*CartLocators.CART_LIST)
            cart_items = carts.find_elements(*CartLocators.ITEM_CARD)
            count=0
            for cart in cart_items:
                name=cart.find_element(*CartLocators.NAME_ITEM_CART)
                name_item=name.text.strip()
                if name_item in item:
                    logging.info(f" Found item: {name_item}")
                    count=count+1
            assert count == len(item),logging.info( f" Validation failed: expected {len(item)} items, found {count}")
            logging.info(" Item cart validation - success")

    def checkout_button(self):
        self.click_button(*CartLocators.CHECKOUT_BUTTON, "Checkout button")
        self.verify_page_title("Checkout: Your Information")
   # def delete_the_first_item_cart(self,item):







