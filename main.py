from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Acess the API key
API_KEY = os.getenv('NASA_API_KEY')

