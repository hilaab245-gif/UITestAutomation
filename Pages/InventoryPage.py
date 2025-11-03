import logging
import time

from UI.locator import itemlocator as itemloc
from core.Base_page import base_page
class Inventoryclass(base_page):
    def __init__(self, driver=None):
        super().__init__(driver=driver)

    def find_item_card(self, card):
        try:
            name = card.find_element(*itemloc.ITEM_NAME).text.strip()
            price = card.find_element(*itemloc.PRICE).text.strip().replace("$", "")
            button = card.find_element(*itemloc.ADD_BUTTON)
            button_text = button.text.strip().lower()
            return {
                "name": name,
                "price": price,
                "button": button,
                "button_text": button_text
            }
        except Exception as e:
            logging.warning("Could not extract item data from card", exc_info=e)
            return None

    def Add_to_Cart(self,arr):
        added = {}
        cards = self.driver.find_elements(*itemloc.ITEM_CARD)
        for card in cards:
            data=self.find_item_card(card)
            if data and data["name"] in arr and data["name"] not in added and data["button_text"] == "add to cart":
                    try:
                        logging.info(f"Clicking button for item: {data['button_text']}")
                        data["button"].click()
                        added[data["name"]] = data["price"]
                        time.sleep(1)
                        logging.info("Add to cart item from json file: %s", data["name"] )
                    except Exception as e: logging.exception("FAIL: Could not click button")
                    if len(added) == len(arr):
                        logging.info("All requested items were added: %s", added)
                        break
        if len(added) != 3:
            logging.info(f"Not all the items were added: {added}")
        return added

    def sort_by_name_or_price_by_text(self,value):
               logging.info("sort by name or price-select_by_visible_text:")
               item_name= self.dropdown_by(value,"text")
               self.print_dropdown(item_name)

    def sort_by_name_or_price_by_value (self,value):
        logging.info("sort by name or price-select_by_visible_value:")
        item_name = self.dropdown_by(value,"value")
        self.print_dropdown(item_name)

    def add_1_item_to_cart(self,item ,arr):
            logging.info("adding 1 item to cart:")
            if item in arr:
                logging.info("item already added to cart")
            try:
                cards = self.driver.find_elements(*itemloc.ITEM_CARD)
                for card in cards:
                    data = self.find_item_card(card)
                    if data["name"]==item and   data["button_text"].lower()=="add to cart":
                        data["button"].click()
                        arr[data["name"]]=data["price"]
                        logging.info(f"PASS: The {item} was added to cart", )
            except Exception as e:
                logging.error("FAIL: item not added to cart" ,e)

    def remove_1_item_from_cart(self,item_n,arr):
                logging.info("Removing 1 item from cart: %s", item_n)
                try:
                    found = False
                    cards = self.driver.find_elements(*itemloc.ITEM_CARD)
                    for card in cards:
                        data = self.find_item_card(card)
                        if data["name"].lower() == item_n.lower() :
                                    data["button"].click()
                                    del arr[data["name"]]
                                    logging.info("PASS: The item '%s' was removed from cart", item_n)
                                    found = True
                                    break
                    if not found:
                           logging.warning("Item '%s' not found in cart list", item_n)
                except Exception as e:
                    logging.error("FAIL: Item not removed from cart: %s", str(e))
                    raise RuntimeError("Failed to remove item from cart")

    def sum_price(self,arr):
        total_price=0
        logging.info("Calculate Total Product Sum")
        try:
            total_price = sum(float(v) for v in arr.values())
            logging.info(f"PASS: The total price is {total_price} for item {arr}")
            return total_price
        except Exception as e:
            logging.error("FAIL: Could not sum price for item: %s", str(e))
            raise RuntimeError("FAIL: Could not sum price for i")

















