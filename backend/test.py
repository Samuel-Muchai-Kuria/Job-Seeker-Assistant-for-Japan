# test.py (Run from project root)

from app.services.affinda import parse_resume_file
from app.services.adzuna import search_jobs_japan
from app.utils.matcher import sort_jobs_by_match
from app.services.deepl import translate_text

# Load .env keys (optional, if not using dotenv CLI)
from dotenv import load_dotenv
load_dotenv()

print("\n==== TESTING RESUME PARSING ====")
try:
    with open("Samuel_Muchai_resume.pdf", "rb") as f:
        content = f.read()
        resume_data = parse_resume_file("Samuel_Muchai_resume.pdf", content)
        print("Parsed Resume Name:", resume_data.get("name"))
        print("Skills:", resume_data.get("skills"))
except Exception as e:
    print("Resume parsing failed:", e)

print("\n==== TESTING JOB SEARCH ====")
try:
    jobs = search_jobs_japan("engineer", "Tokyo", 5)
    print(f"Found {len(jobs)} job(s). Sample title:", jobs[0].get("title"))
except Exception as e:
    print("Job search failed:", e)

print("\n==== TESTING MATCHER ====")
try:
    resume_skills = [s.get("name") for s in resume_data.get("skills", []) if s.get("name")]
    matched_jobs = sort_jobs_by_match(resume_skills, jobs)
    for job in matched_jobs[:2]:
        print(f"{job['title']} -> Match Score: {job['match_score']}")
except Exception as e:
    print("Match scoring failed:", e)

print("\n==== TESTING TRANSLATION ====")
try:
    translated = translate_text("こんにちは、エンジニアを探しています。", "EN")
    print("Translated Text:", translated)
except Exception as e:
    print("Translation failed:", e)
