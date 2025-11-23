from .career_agent import suggest_roles, recommend_courses
from .match_engine import calculate_skill_match

def generate_role_fit(resume_skills, jd_skills):
    # 1. Top career roles based on resume
    top_roles = suggest_roles(resume_skills)
    top_role, top_score = top_roles[0]

    # 2. Skill gap based on that role
    role_requirements = {
        role: skills for role, skills in [
            ("Data Analyst", ["python", "sql", "excel", "tableau", "statistics", "data visualization"]),
            ("Machine Learning Engineer", ["python", "numpy", "pandas", "sklearn", "deep learning", "ml algorithms"]),
            ("Frontend Developer", ["javascript", "react", "html", "css", "ui design"]),
            ("Backend Developer", ["python", "flask", "django", "rest api", "databases", "docker"]),
            ("Cloud Engineer", ["aws", "azure", "gcp", "terraform", "kubernetes"])
        ]
    }

    required = role_requirements[top_role]
    missing = list(set(required) - set(resume_skills))

    # 3. Skill overlap with JD (if provided)
    jd_match = calculate_skill_match(resume_skills, jd_skills)

    return {
        "best_role": top_role,
        "role_fit_percent": top_score,
        "missing_skills": missing,
        "recommended_courses": recommend_courses(missing),
        "jd_overlap_skills": jd_match["overlap_skills"],
        "jd_missing_skills": jd_match["missing_skills"],
        "jd_match_percent": jd_match["skill_match_percent"]
    }
