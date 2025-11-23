from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_about_me(skills):
    skill_text = ", ".join(skills)
    return f"I am a passionate developer skilled in {skill_text}. I enjoy solving real-world problems and building impactful projects."

def generate_projects(skills):
    projects = []

    if "python" in skills:
        projects.append({
            "title": "Smart Resume Analyzer",
            "description": "AI-powered resume parser using NLP & ML techniques.",
            "tech": ["Python", "NLP", "Flask"]
        })
    
    if "react" in skills or "javascript" in skills:
        projects.append({
            "title": "Portfolio Generator",
            "description": "Dynamic portfolio builder with AI-generated content.",
            "tech": ["React", "Node", "CSS"]
        })
    if "machine learning" in skills:
        projects.append({
            "title": "ML Career Predictor",
            "description": "Predicts job roles based on skills.",
            "tech": ["Python", "ML", "Sklearn"]
        })
    if not projects:
        projects.append({
            "title": "AI Career Advisor",
            "description": "Helps users find suitable career paths based on skills.",
            "tech": ["AI", "ML"]
        })

    return projects


def generate_skills_summary(skills):
    return f"You are proficient in: {', '.join(skills)}."


def build_portfolio(resume_skills):
    return {
        "about_me": generate_about_me(resume_skills),
        "skills_summary": generate_skills_summary(resume_skills),
        "projects": generate_projects(resume_skills),
        "social_links": {
            "github": "https://github.com/your-profile",
            "linkedin": "https://linkedin.com/in/your-profile"
        }
    }
