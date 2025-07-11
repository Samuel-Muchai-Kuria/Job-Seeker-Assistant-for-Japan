# backend/app/services/deepl.py

import requests
import os

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_URL = "https://api-free.deepl.com/v2/translate"

def translate_text(text: str, target_lang: str = "EN") -> str:
    data = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "target_lang": target_lang.upper()
    }

    response = requests.post(DEEPL_URL, data=data)

    if response.status_code != 200:
        raise Exception(f"DeepL API error: {response.status_code} - {response.text}")

    return response.json()["translations"][0]["text"]
