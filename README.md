# Reviews  Saucedemo Automation Project

## How To Run:
 To start the application, run the following command : python main.py

## Configuration:
   Configuration settings can be modified in the config/config.json file.<br>
   base_url – The URL of the application under test<br>
   username / password – Login credentials <br>
   checkout – User details for checkout user <br>
   Products – List of products to add to cart <br>
   sort_by – Sorting option for inventory page <br>

## Project Structure: 
-  Config/ config json- configuration <br>
-  Pages/ Implements -the Page Object Model each page of the application is represented as a separate class: <br>
-  LoginPage.py – actions for the login screen <br>
-  InventoryPage.py – actions for the product listing page <br>
- CartPage.py – actions for the shopping cart.<br>
-  CheckoutInformationPage.py – filling in user details during checkout.<br>
-  OrderComplete.py – validations for the order completion page.<br>
-  UI/ locator- contains locators or selectors (XPath, CSS) for UI elements.<br>
-  Utils/ Extract_config.py – loads and extracts values from the JSON configuration.<br>
-  core/Base_page.py -  functionality shared across the project.a base class with common methods.<br>
  (e.g., click_button, verify_page_title, error_mes). ➝ All Page Objects inherit from this class.<br>
-  logs/app.log- Stores log files generated during test execution. <br>
   main.py The main of the project.
