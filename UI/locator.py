from selenium.webdriver.common.by import By

class UserData:
    USER_NAME = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.ID,'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

class CartLocators:
    CART_BUTTON=(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    ITEM_CARD = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON =(By.XPATH, '//*[@id="checkout"]')
    Finish_BUTTON=(By.XPATH, '//*[@id="finish"]')
    NAME_ITEM_CART = (By.CLASS_NAME, "inventory_item_name")
    CART_LIST = (By.CLASS_NAME, "cart_list")


class itemlocator:
    ITEM_CARD = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ADD_BUTTON = (By.CSS_SELECTOR, ".pricebar button")
    TITLE=(By.CSS_SELECTOR, '[data-test="title"]')
    SORT_DROP=(By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    PRICE=(By.CLASS_NAME, 'inventory_item_price')

class CheckoutUserLocators:
     FIRST_NAME=(By.ID, 'first-name')
     LAST_NAME=(By.ID, 'last-name')
     ZIP_CODE=(By.ID, 'postal-code')
     CONTINUE_BUTTON=(By.ID, 'continue')
     CANCEL_BUTTON=(By.ID, 'cancel')

class CheckOutLocators :
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BUTTON = (By.CSS_SELECTOR, '[data-test="cancel"]')
    FINISH_BUTTON=(By.XPATH, '//*[@id="finish"]')
    COMPLETE_TEXT=(By.CLASS_NAME, "complete-header")
