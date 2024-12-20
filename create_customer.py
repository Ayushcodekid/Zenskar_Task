import requests
from config import BASE_URL, HEADERS

def create_customer():
    url = f"{BASE_URL}/customers"
    data = {
    "external_id": "236862834426",
    "customer_name": "New Customer5",
    "email": "ayush25@gmail.com",
    "phone_number": "+919811333910",
}

    response = requests.post(url, headers=HEADERS, json=data)

    if response.status_code == 200:
        try:
            print("Create Customer Response:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not valid JSON")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response Text:", response.text)

    return response.json()

create_customer()
