import json
import logging
from pathlib import Path


#load json config and Extract
class ConfigLoader:
    def __init__(self, path):
        self.path =path
        if not  self.path.exists():
           raise FileNotFoundError(f"Missing config file: {path}")
        try:
           with open(path, "r", encoding="utf-8") as f:
               self.data = json.load(f)
               logging.info(f"Loaded config from {path}")
        except json.JSONDecodeError as e:
               raise ValueError(f"Invalid JSON format in {path}:{e}")
    def Extract_config_1_value(self,value):# Extract value not in nested object
         return self.data.get(value)
    def Extract_config_user_value(self):#Extract user details
        checkout = self.data.get("checkout", {})#dic
        arr_user=[checkout.get("first_name"),checkout.get("last_name"),checkout.get("zip_code")]#list
        logging.info(f"Extract from config user checkout values: {arr_user}")
        return arr_user
    def Extract_config_items_value(self):#Extract Products details
        Products = self.data.get("Products", {}) #dic
        arr_item=[Products.get("Product_1"),Products.get("Product_2"),Products.get("Product_3")] #list
        logging.info(f"Extract from config products values: {arr_item}")
        return arr_item
