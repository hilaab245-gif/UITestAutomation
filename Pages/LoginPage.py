
import logging
from UI.locator import UserData as loc
from core.Base_page import base_page

class loginclass(base_page):
    def __init__(self, driver=None, incognito: bool = True):
        super().__init__(driver=driver)

    def open_url(self, base_url: str):  # open url
        logging.info("Attempting to navigate to URL: %s", base_url)  # Log the attempt to open the URL
        try:
            self.driver.get(base_url)
            logging.info("PASS: opened %s", base_url)  # Logs a success to open the url
        except Exception as e:
            logging.error("FAIL: could not open URL: %s", base_url)
            raise RuntimeError(f"Could not open URL: {base_url}") from e

    def login(self,username,password):
            self.send_key(*loc.USER_NAME,username,name="Username")
            self.send_key(*loc.PASSWORD,password,name="Password")
            self.click_button(*loc.LOGIN_BUTTON, name="Login button")

    def verify_login_successfully(self):
            self.error_mes()
            self.verify_page_title("Products")
