# backend/app/routes/translate.py

from fastapi import APIRouter, HTTPException, Query
from app.services import deepl

router = APIRouter()

@router.get("/")
def translate_text(
    text: str = Query(..., description="Text to translate"),
    target_lang: str = Query("EN", description="Target language, e.g. EN or JA")
):
    try:
        translated = deepl.translate_text(text, target_lang)
        return {"status": "success", "translated_text": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))