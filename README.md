# Selenium-Appium-Project
Nike Automated Tests
This repository contains automated tests for various functionalities on the Nike website. These tests are written using Python's unittest framework, Selenium WebDriver for web automation, and Appium for mobile automation.

Tests Overview
1. Test Call Store
Description: This test navigates to the Nike website, searches for a store location, retrieves the phone number, and simulates calling the store using a mobile dialer app.

Key Actions:

Search for a Nike store location.

Retrieve the store's phone number.

Simulate calling the store using the mobile dialer app.

2. Test Get Directions
Description: This test navigates to the Nike website, searches for a store location, retrieves the store's address, and searches for directions using a maps app.

Key Actions:

Search for a Nike store location.

Retrieve the store's address.

Search for directions to the store using the maps app.

3. Test SMS Store
Description: This test navigates to the Nike website, searches for a store location, retrieves the phone number, and simulates sending an SMS message to the store.

Key Actions:

Search for a Nike store location.

Retrieve the store's phone number.

Simulate sending an SMS message to the store using the mobile messaging app.

4. Test Product Price Exchange
Description: This test navigates to the Nike website, searches for a product in the men's category, retrieves the product's price in shekels, converts the price to USD using an exchange rate, and verifies the conversion using a calculator app.

Key Actions:

Search for a product in the men's category.

Retrieve the product's name and price in shekels.

Obtain the exchange rate from an external service.

Calculate the price in USD using the mobile calculator app.

Verify the calculated price.

5. Test Calculate Prices of Two Products
Description: This test navigates to the Nike website, searches for two products in the men's category, retrieves their prices, sums the prices using a calculator app, and verifies the total.

Key Actions:

Search for two products in the men's category.

Retrieve the names and prices of the products.

Calculate the total price using the mobile calculator app.

Verify the total price.

Helper Functions
choose_store_number_func: Helper function to retrieve the phone number of the first store listed in the store search results.

choose_store_address_func: Helper function to retrieve the address of the first store listed in the store search results.

Running the Tests
To run the tests, ensure you have the necessary dependencies installed and configured. Use the following command to execute the tests:

bash
python -m unittest discover
Dependencies
Python 3.x

Selenium

Appium

Edge WebDriver