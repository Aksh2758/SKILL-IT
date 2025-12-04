from sentence_transformers import SentenceTransformer, util

# Load the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_skill_match(resume_skills, jd_skills):
    """
    Calculate skill match between resume and job description.
    
    Args:
        resume_skills: List of skills from resume
        jd_skills: List of skills from job description
        
    Returns:
        Dictionary with overlap_skills, missing_skills, and skill_match_percent
    """
    # Convert to sets for comparison
    resume_set = set([skill.lower().strip() for skill in resume_skills if skill])
    jd_set = set([skill.lower().strip() for skill in jd_skills if skill])
    
    # Calculate overlap and missing skills
    overlap_skills = list(resume_set.intersection(jd_set))
    missing_skills = list(jd_set - resume_set)
    
    # Calculate match percentage
    if len(jd_set) > 0:
        skill_match_percent = round((len(overlap_skills) / len(jd_set)) * 100, 2)
    else:
        skill_match_percent = 0.0
    
    return {
        "overlap_skills": overlap_skills,
        "missing_skills": missing_skills,
        "skill_match_percent": skill_match_percent
    }


def calculate_text_similarity(resume_text, jd_text):
    """
    Calculate semantic similarity between resume and job description texts.
    
    Args:
        resume_text: Full resume text
        jd_text: Full job description text
        
    Returns:
        Similarity score as percentage (0-100)
    """
    if not resume_text or not jd_text:
        return 0.0
    
    # Generate embeddings
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(jd_text, convert_to_tensor=True)
    
    # Calculate cosine similarity
    score = util.cos_sim(emb1, emb2).item()
    
    # Convert to percentage
    percentage = round(score * 100, 2)
    
    return percentage


def generate_final_score(skill_match_percent, text_similarity):
    """
    Generate final matching score by combining skill match and text similarity.
    
    Args:
        skill_match_percent: Percentage of skill match (0-100)
        text_similarity: Text similarity score (0-100)
        
    Returns:
        Final score as percentage (0-100)
    """
    # Weighted average: 60% skill match, 40% text similarity
    final_score = (skill_match_percent * 0.6) + (text_similarity * 0.4)
    
    return round(final_score, 2)
