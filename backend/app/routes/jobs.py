# backend/app/routes/jobs.py

from fastapi import APIRouter, Query, HTTPException
from app.services import adzuna

router = APIRouter()

@router.get("/search")
def search_jobs(
    keyword: str = Query(..., description="Job keyword to search"),
    location: str = Query("Tokyo", description="Location in Japan"),
    max_results: int = Query(10, description="Maximum number of results")
):
    try:
        results = adzuna.search_jobs_japan(keyword, location, max_results)
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
