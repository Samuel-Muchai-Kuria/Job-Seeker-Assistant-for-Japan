# backend/app/services/adzuna.py

from dotenv import load_dotenv
load_dotenv()
import requests
import os

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")
# BASE_URL = "https://api.adzuna.com/v1/api/jobs/jp/search/1"  # JP = Japan
BASE_URL = "https://adzuna-api.p.rapidapi.com/v1/api/jobs/jp/search/1"


def search_jobs_japan(keyword: str, location: str, max_results: int):
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": max_results,
        "what": keyword,
        "where": location,
        "language": "en"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Adzuna API error: {response.status_code} - {response.text}")
        raise Exception(f"Adzuna API error: {response.status_code} - {response.text}")

    print(f"Adzuna API response: {response.status_code}")
    return response.json().get("results", [])
