# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
API_KEY = os.getenv('NOCODB_API_KEY')
HOST = os.getenv('NOCODB_HOST')
TABLE_ID = os.getenv('NOCODB_TABLE_ID')
VIEW_ID = os.getenv('NOCODB_VIEW_ID')

# Validation
if not API_KEY:
    raise ValueError("NOCODB_API_KEY environment variable is not set")