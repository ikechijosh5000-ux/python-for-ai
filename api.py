import os
from dotenv import load_dotenv

load_dotenv()

# Read from environment
api_key = os.environ.get('API_KEY')
debug = os.environ.get('DEBUG')

print(f"Using database: {api_key}")# Now use your variables


print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")


# app.py
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.environ.get('OPENAI_API_KEY')

if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API
headers = {"Authorization": f"Bearer {API_KEY}"}