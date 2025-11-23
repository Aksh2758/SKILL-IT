import spacy
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

ROLE_SKILL_MAP = {
    "Data Analyst": ["python", "sql", "excel", "tableau", "statistics", "data visualization"],
    "Machine Learning Engineer": ["python", "numpy", "pandas", "sklearn", "deep learning", "ml algorithms"],
    "Frontend Developer": ["javascript", "react", "html", "css", "ui design"],
    "Backend Developer": ["python", "flask", "django", "rest api", "databases", "docker"],
    "Cloud Engineer": ["aws", "azure", "gcp", "terraform", "kubernetes"]
}

COURSE_MAP = {
    "python": "Python for Everybody – Coursera",
    "sql": "Databases & SQL – Udemy",
    "machine learning": "Andrew Ng ML – Coursera",
    "react": "React Frontend Bootcamp – Udemy",
    "aws": "AWS Solution Architect – Coursera",
    "data visualization": "Tableau A–Z – Udemy",
}

def suggest_roles(resume_skills):
    scores = {}
    for role, required in ROLE_SKILL_MAP.items():
        overlap = set(resume_skills).intersection(required)
        score = len(overlap) / len(required)
        scores[role] = round(score * 100, 2)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:3]

def recommend_courses(missing_skills):
    recs = []
    for s in missing_skills:
        if s in COURSE_MAP:
            recs.append(COURSE_MAP[s])
    return recs[:5]

def generate_career_path(resume_skills):
    roles = suggest_roles(resume_skills)
    top_role = roles[0][0]

    required = ROLE_SKILL_MAP[top_role]
    missing = list(set(required) - set(resume_skills))

    return {
        "recommended_role": top_role,
        "match_percent": roles[0][1],
        "required_skills": required,
        "missing_skills": missing,
        "course_recommendations": recommend_courses(missing)
    }
