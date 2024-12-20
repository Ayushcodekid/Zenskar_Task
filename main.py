from create_customer import create_customer
from create_product import create_product
from create_contract import create_contract
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def main():
    try:
        # Step 1: Create a customer
        logging.debug("Creating customer...")
        customer = create_customer()
        if not customer or "id" not in customer:
            logging.error("Failed to create customer or missing 'id' field")
            return
        
        # Step 2: Create products
        logging.debug("Creating products...")
        product1 = create_product(name="One Time Fee", product_type="group", billing="prepaid", frequency="one_time", price=5000)
        if not product1 or "id" not in product1:
            logging.error("Failed to create product 1 or missing 'id' field")
            return
        
        product2 = create_product(name="Monthly Platform Fee", product_type="product", billing="postpaid", frequency="monthly", price=10000)
        if not product2 or "id" not in product2:
            logging.error("Failed to create product 2 or missing 'id' field")
            return
        
        product3 = create_product(name="Monthly User Fee", product_type="product", billing="postpaid", frequency="monthly", price=60)
        if not product3 or "id" not in product3:
            logging.error("Failed to create product 3 or missing 'id' field")
            return

        # Step 3: Create a contract
        logging.debug("Creating contract...")
        contract_response = create_contract(customer_id=customer["id"], product_ids=[product1["id"], product2["id"], product3["id"]])
        
        if not contract_response or "id" not in contract_response:
            logging.error("Failed to create contract")
            return
        
        logging.info("Contract created successfully")
        return contract_response

    except Exception as e:
        logging.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
