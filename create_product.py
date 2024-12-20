import requests
from config import BASE_URL, HEADERS

def create_product(name, product_type, billing, frequency, price):
    url = f"{BASE_URL}/products"
    data = {
        "name": name,
        "type": product_type,
        "billing": billing,
        "frequency": frequency,
        "price": price
    }
    response = requests.post(url, headers=HEADERS, json=data)
    print(f"Create Product Response for {name}:", response.json())
    return response.json()

def create_all_products():
    # Product 1: One Time Fee
    create_product("One Time Fee", "group", "prepaid", "one_time", 5000)
    
    # Product 2: Monthly Platform Fee
    create_product("Monthly Platform Fee", "product", "postpaid", "monthly", 10000)
    
    # Product 3: Monthly User Fee
    create_product("Monthly User Fee", "product", "postpaid", "monthly", 60)

if __name__ == "__main__":
    create_all_products()
