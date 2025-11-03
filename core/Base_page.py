import logging
from pathlib import Path
from telnetlib import EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from UI.locator import itemlocator as  ITEM_LOCATOR
from UI.locator import UserData
from selenium.webdriver.support.ui import Select

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
log_file = LOG_DIR / "app.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s" ,
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()  # גם למסך
    ]
)

class base_page:
    def __init__(self, driver):
        if driver:
              self.driver = driver
              logging.info("Using existing WebDriver")
        else:
             logging.info("Initializing incognito Page")
             opts = Options() #לcreate obl
             logging.debug("Chrome Options object created.")
             opts.add_argument("--incognito")
             try:
                 logging.info("Attempting to open Chrome browser")
                 self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
                 self.driver.maximize_window()
                 logging.info("PASS: start Chrome WebDriver successfully")
             except Exception as e:  # If any error occurs during browser setup- Logs a fail message
                    logging.exception("FAIL: Could not start Chrome WebDriver")
                    raise RuntimeError("Could not start Chrome WebDriver") from e

    def click_button(self,by,value,name):
            logging.info("Wait until the  field is present")
            locator = (by, value)
            button=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            try:
                button.click()
                logging.info("PASS: Clicked %s successfully", name)
            except Exception as e:
                logging.exception("FAIL: not found %s element ",name)
                raise RuntimeError("Could not found element ")


    def send_key(self,by,value, key,name):
        locator = (by, value)
        try:
            logging.info("Wait until the field is present")
            field=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            field.clear()
            field.send_keys(key)
            logging.info("PASS: User successful type %s in %s field",key,name)
        except Exception as e:
            logging.exception("FAIL: Could not send key: %s in %s field ",key,name)
            raise RuntimeError("Could not send key ",{key})

    def error_mes(self):
        try:
             error_container = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(UserData.ERROR_MESSAGE))
             logging.warning(f"Fail: Error message display {error_container.text }")
             raise RuntimeError(f" Error message display: {error_container.text }")
        except TimeoutException:
                logging.info("PASS: No error message display.")

    def verify_page_title(self,expected_title):
        logging.info(f"check if the user move to next page ")
        try:
           title = self.driver.find_element(*ITEM_LOCATOR.TITLE)
           title_text = title.text.strip()
           if title_text == expected_title.strip():
               logging.info(f"PASS: User moved to the next page successfully. Title: '{title_text}'")
           else:
               logging.error(f"FAIL: Expected title '{expected_title}' but got '{title_text}'")
               raise RuntimeError(f"Expected title '%s' but got %s", expected_title, title_text)
        except Exception as e:
           logging.error(f" page {expected_title}did not load within the expected time.", expected_title)
           raise RuntimeError(f" page {expected_title} did not load within the expected time.%s", expected_title)

    def dropdown_by(self,key,by):
        logging.info("sort the dropdown by text")
        try:
            dropdown = Select(self.driver.find_element(*ITEM_LOCATOR.SORT_DROP))
            if by=="text":
                dropdown.select_by_visible_text(key)
                logging.info("PASS: Dropdown selected to text successfully.")
            elif by == "value":
                dropdown.select_by_value(key)
                logging.info("PASS: Dropdown selected to value successfully.")
            item_names = self.driver.find_elements(*ITEM_LOCATOR.ITEM_NAME)
            return item_names
        except Exception as e:
            logging.error("Failed to sort by name or price: %s", str(e))
            raise RuntimeError("Failed to sort by name or price")

    def print_dropdown(self,item_name):
        names = [item.text.strip() for item in item_name]
        [logging.info(i) for i in names]












