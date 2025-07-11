# backend/app/utils/matcher.py

from typing import List, Dict
import re

def calculate_match_score(resume_skills: List[str], job_description: str) -> float:
    """
    Calculate a simple match score based on how many resume skills appear in the job description.
    """
    job_text = job_description.lower()
    matched_skills = [skill for skill in resume_skills if re.search(rf"\\b{re.escape(skill.lower())}\\b", job_text)]
    
    if not resume_skills:
        return 0.0

    score = len(matched_skills) / len(resume_skills)
    return round(score, 2)

def sort_jobs_by_match(resume_skills: List[str], jobs: List[Dict]) -> List[Dict]:
    for job in jobs:
        job_desc = job.get("description", "")
        job["match_score"] = calculate_match_score(resume_skills, job_desc)
    return sorted(jobs, key=lambda x: x["match_score"], reverse=True)
