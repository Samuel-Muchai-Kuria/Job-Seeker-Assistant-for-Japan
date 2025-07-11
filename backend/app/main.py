# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import resume, jobs, translate

app = FastAPI(title="Job Seeker Assistant for Japan")

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(translate.router, prefix="/translate", tags=["Translate"])

@app.get("/")
def root():
    return {"message": "Job Seeker Assistant API running."}
