# import requests
# from config import BASE_URL, HEADERS
# from datetime import datetime

# def convert_to_unix_timestamp(date_str):
#     """Convert ISO 8601 date string to Unix timestamp."""
#     return int(datetime.fromisoformat(date_str).timestamp())

# def create_contract(customer_id, product_ids, template_id):
#     url = f"{BASE_URL}/contracts"

#     # Convert start and end dates to Unix timestamps
#     start_date = convert_to_unix_timestamp("2024-01-01")
#     end_date = convert_to_unix_timestamp("2024-12-31")

#     products = [
#         {"product_id": product_ids[0], "start_date": convert_to_unix_timestamp("2024-01-01"), "end_date": convert_to_unix_timestamp("2024-12-31")},  # One Time Fee
#         {"product_id": product_ids[1], "start_date": convert_to_unix_timestamp("2024-01-01"), "end_date": convert_to_unix_timestamp("2024-03-31")},  # Monthly Platform Fee for first 3 months
#         {"product_id": product_ids[2], "start_date": convert_to_unix_timestamp("2024-01-01"), "end_date": convert_to_unix_timestamp("2024-12-31")}   # Monthly User Fee
#     ]

#     data = {
#         "customer": customer_id,
#         "template_id": template_id, 
#         "start_date": start_date,
#         "end_date": end_date,
#         "products": products
#     }

#     response = requests.post(url, headers=HEADERS, json=data)
#     print("Create Contract Response:", response.json())
#     return response.json()

# # Example of how to call the function
# customer_id = "da8aae72-bc38-4688-a5d9-9255bfa56fdd"  # Replace with actual customer ID
# product_ids = ["a787435e-33d9-4fe2-b983-755f3adc1591", "d546adb5-0e11-4168-8c5d-4531e00659d4", "6ee0829b-56da-4d69-818e-792bfbadb746"]  # Replace with actual product IDs
# template_id = "1234567890101"  # Replace with a valid template ID
# create_contract(customer_id, product_ids, template_id)















import requests
from config import BASE_URL, HEADERS
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def convert_to_unix_timestamp(date_str):
    """Convert ISO 8601 date string to Unix timestamp."""
    try:
        timestamp = int(datetime.fromisoformat(date_str).timestamp())
        logging.debug(f"Converted {date_str} to timestamp {timestamp}")
        return timestamp
    except Exception as e:
        logging.error(f"Error converting date {date_str} to timestamp: {e}")
        raise

def create_contract(customer_id, product_ids, template_id):
    url = f"{BASE_URL}/contracts"

    # Convert start and end dates to Unix timestamps
    try:
        start_date = convert_to_unix_timestamp("2024-01-01")
        end_date = convert_to_unix_timestamp("2024-12-31")
    except Exception as e:
        logging.error("Error converting start or end date")
        return

    # Products section
    products = [
        {"product_id": product_ids[0], "start_date": start_date, "end_date": end_date},  # One Time Fee
        {"product_id": product_ids[1], "start_date": start_date, "end_date": convert_to_unix_timestamp("2024-03-31")},  # Monthly Platform Fee for first 3 months
        {"product_id": product_ids[2], "start_date": start_date, "end_date": end_date}   # Monthly User Fee
    ]

    # Data structure to match the API response format
    data = {
        "status": "active",
        "name": "Dhiman",  # Adjust this as per your requirements
        "description": None,
        "customer": customer_id,  # Ensure this is passed as `customer`
        "template_id": template_id,  # Corrected to None
        "currency": 1000,  # Currency as a number
        "start_date": start_date,
        "end_date": end_date,
        "products": products
    }

    # Log the request data
    logging.debug(f"Request data: {data}")

    try:
        response = requests.post(url, headers=HEADERS, json=data)
        
        # Log the response status code and content
        logging.debug(f"Response Status Code: {response.status_code}")
        logging.debug(f"Response Headers: {response.headers}")
        logging.debug(f"Response Text: {response.text}")
        
        # Check for successful response
        if response.status_code == 200:
            logging.info("Contract created successfully")
            return response.json()
        else:
            logging.error(f"Error creating contract: {response.status_code} - {response.text}")
            return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during request: {e}")
        return {"error": str(e)}

# Example of how to call the function
customer_id = "da8aae72-bc38-4688-a5d9-9255bfa56fdd"  # Replace with actual customer ID
product_ids = ["a787435e-33d9-4fe2-b983-755f3adc1591", "d546adb5-0e11-4168-8c5d-4531e00659d4", "6ee0829b-56da-4d69-818e-792bfbadb746"]  # Replace with actual product IDs
template_id = "a85773ae-708f-430c-92ad-b37241f6245f"  # Template ID can be None if not needed
create_contract(customer_id, product_ids, template_id)

