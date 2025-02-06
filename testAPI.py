import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print(f"Using API Key: {api_key[:5]}...")  # To verify it's loaded


