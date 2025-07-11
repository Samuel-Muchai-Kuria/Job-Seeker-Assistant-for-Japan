# backend/app/services/affinda.py
from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()
# Use a direct Affinda key, not from RapidAPI
AFFINDA_API_KEY = os.getenv("AFFINDA_API_KEY")
AFFINDA_URL = "https://api.affinda.com/v2/resumes/upload"

def parse_resume_file(filename: str, content: bytes):
    headers = {
        "Authorization": f"Bearer {AFFINDA_API_KEY}"
    }
    print(f"Uploading resume file: {AFFINDA_URL}")
    files = {
        "file": (filename, content, "application/pdf")
    }

    response = requests.post(AFFINDA_URL, headers=headers, files=files)
    
    if response.status_code != 201:
        raise Exception(f"Affinda API error: {response.status_code} - {response.text}")

    return response.json()
