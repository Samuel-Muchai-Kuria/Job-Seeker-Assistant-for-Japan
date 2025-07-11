# backend/app/models/schemas.py

from pydantic import BaseModel
from typing import List, Optional

class ResumeData(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    skills: List[str] = []
    summary: Optional[str]
    education: Optional[str]
    experience: Optional[str]

class JobResult(BaseModel):
    title: str
    company: Optional[str]
    location: Optional[str]
    description: Optional[str]
    url: Optional[str]

class TranslationRequest(BaseModel):
    text: str
    target_lang: str = "EN"

class TranslationResponse(BaseModel):
    translated_text: str
