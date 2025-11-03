import logging
import sys
from pathlib import Path

from Pages.LoginPage import loginclass
from Pages.InventoryPage import Inventoryclass
from  Pages.CartPage import CartPage
from Pages.CheckoutInformationPage import CheckoutInformation
from Pages.OrderComplete import OrderComplete
from Utils.Extract_config import ConfigLoader

#gloabl
CONFIG_PATH = Path("config/config.json")

if __name__ == "__main__":
  try:
    config=ConfigLoader(CONFIG_PATH)

    page=loginclass()
    page.open_url(config.Extract_config_1_value("base_url"))
    page.login(config.Extract_config_1_value("username"),config.Extract_config_1_value("password"))
    page.verify_login_successfully()

    inv=Inventoryclass(driver=page.driver)
    item=inv.Add_to_Cart(config.Extract_config_items_value())
    inv.sort_by_name_or_price_by_text("Name (Z to A)")
    inv.sort_by_name_or_price_by_value(config.Extract_config_1_value("sort_by"))
    inv.add_1_item_to_cart("Sauce Labs Bolt T-Shirt",item  )
    inv.remove_1_item_from_cart("Sauce Labs Bolt T-Shirt",item)
    price=inv.sum_price(item)

    Cart = CartPage(driver=inv.driver)
    Cart.cart_button()
    Cart.verifyCartItems(item)
    Cart.checkout_button()

    Check=CheckoutInformation(driver=Cart.driver)
    Check.cancel_button()
    Check.user_data_order(config.Extract_config_user_value())
    Check.click_but_contion()

    order=OrderComplete(driver=Check.driver)
    order.verify_checkout_overview_details(item,price)
    order.cancel_checkout()
    order.finish_button_checkout()

  except Exception as e:
      logging.error(e)
      sys.exit(1)






