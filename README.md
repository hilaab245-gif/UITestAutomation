SauceTestAutomation

1. To start the application, run the following command : python main.py


2. Configuration-<br>
   Configuration settings can be modified in the config/config.json file.<br>
   base_url – The URL of the application under test<br>
   username / password – Login credentials <br>
   checkout – User details for checkout user <br>
   Products – List of products to add to cart <br>
   sort_by – Sorting option for inventory page <br>


3.Project Structure: <br>
  Config/ config json- configuration <br>
  Pages/ Implements the Page Object Model each page of the application is represented as a separate class: <br>
  LoginPage.py – actions for the login screen <br>
  InventoryPage.py – actions for the product listing page <br>
  CartPage.py – actions for the shopping cart.<br>
  CheckoutInformationPage.py – filling in user details during checkout.<br>
  OrderComplete.py – validations for the order completion page.<br>
  UI/ locator- contains locators or selectors (XPath, CSS) for UI elements.<br>
  Utils/ Extract_config.py – loads and extracts values from the JSON configuration.<br>
  core/Base_page.py   functionality shared across the project.a base class with common methods.<br>
  (e.g., click_button, verify_page_title, error_mes). ➝ All Page Objects inherit from this.<br>
  logs/ Stores log files generated during test execution. <br>


main.py The main entry point of the project. ➝ Orchestrates the entire test flow: login, adding products, checkout, order completion, and screenshot capture on failure.

