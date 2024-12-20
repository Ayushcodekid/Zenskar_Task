# Zenskar Assignment Documentation


NOTE:
The api-key , org-id , base-url are present in my .env file which is added  to gitignore , as it contains sensitive informtion.

This repository contains Python scripts to interact with the Zenskar API for creating customers, products, and contracts.

## Prerequisites

1. Install Python (version 3.8 or above).
2. Install the required libraries:
   pip install requests python-dotenv



Create Customer
Description: Creates a new customer in the Zenskar system.
How to Run:  python create_customer.py


2. Create Products
Description: Creates three types of products:
How to Run: python create_products.py



4. Create Contract
Description: Creates a contract for the customer, associating them with products and a template.
How to Run:  python create_contract.py


5. Or else run: py main.py 
This will run all the three scripts one by one and create all the json data together



Verify Output
After running each script, check the console for API responses to confirm the operation.
Verify the created data using an API testing tool like Postman or directly in your backend.


