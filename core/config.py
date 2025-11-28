import os
from dotenv import load_dotenv

load_dotenv()

def load_api_config():
    key = os.getenv("RAPIDAPI_KEY")
    host = os.getenv("RAPIDAPI_HOST")
    url = os.getenv("RAPIDAPI_URL")

    if not key or not host or not url:
        raise RuntimeError("Missing API configuration in .env")

    return {
        "key": key,
        "host": host,
        "url": url,
    }