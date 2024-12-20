import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
ORG_ID = os.getenv("ORG_ID")

HEADERS = {
    "x-api-key": API_KEY,
    "organisation": ORG_ID,
    "Content-Type": "application/json"
}
