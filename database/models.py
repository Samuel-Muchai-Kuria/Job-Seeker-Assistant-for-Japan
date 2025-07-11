# backend/database/models.py

from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    skills = Column(JSON)
    summary = Column(Text)
    education = Column(Text)
    experience = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class JobMatch(Base):
    __tablename__ = "job_matches"

    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer)
    job_title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    url = Column(String)
    match_score = Column(String)
    matched_at = Column(DateTime, default=datetime.utcnow)
