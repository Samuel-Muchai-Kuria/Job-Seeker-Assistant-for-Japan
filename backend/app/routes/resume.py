# backend/app/routes/resume.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import affinda

router = APIRouter()

@router.post("/parse")
async def parse_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        content = await file.read()
        parsed_data = affinda.parse_resume_file(file.filename, content)
        return {"status": "success", "data": parsed_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
