from flask import Blueprint, request, jsonify
from ..utils.decorators import token_required
from ..services.history_service import get_user_history

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/search", methods=["POST"])
def search_jobs():
    """
    Search for jobs based on skills and preferences.
    This is a placeholder for future integration with job APIs.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        skills = data.get("skills", [])
        location = data.get("location", "")
        experience_level = data.get("experience_level", "")
        
        # Placeholder response - integrate with real job APIs later
        # (LinkedIn Jobs API, Indeed API, GitHub Jobs, etc.)
        sample_jobs = [
            {
                "id": 1,
                "title": "Full Stack Developer",
                "company": "Tech Corp",
                "location": location or "Remote",
                "experience": "2-4 years",
                "skills_required": ["Python", "React", "MongoDB"],
                "match_score": 85,
                "description": "Looking for a full stack developer with experience in Python and React.",
                "salary_range": "$80,000 - $120,000",
                "posted_date": "2025-12-01"
            },
            {
                "id": 2,
                "title": "Backend Developer",
                "company": "StartUp Inc",
                "location": location or "New York, NY",
                "experience": "1-3 years",
                "skills_required": ["Python", "Flask", "SQL"],
                "match_score": 78,
                "description": "Backend developer needed for our growing startup.",
                "salary_range": "$70,000 - $100,000",
                "posted_date": "2025-12-02"
            },
            {
                "id": 3,
                "title": "Machine Learning Engineer",
                "company": "AI Solutions",
                "location": location or "San Francisco, CA",
                "experience": "3-5 years",
                "skills_required": ["Python", "ML", "Deep Learning", "NLP"],
                "match_score": 72,
                "description": "ML engineer to work on cutting-edge AI projects.",
                "salary_range": "$120,000 - $160,000",
                "posted_date": "2025-12-03"
            }
        ]
        
        # Filter jobs based on user skills (basic matching)
        if skills:
            user_skills_set = set([s.lower() for s in skills])
            for job in sample_jobs:
                job_skills_set = set([s.lower() for s in job["skills_required"]])
                overlap = len(user_skills_set.intersection(job_skills_set))
                total = len(job_skills_set)
                job["match_score"] = round((overlap / total) * 100, 2) if total > 0 else 0
            
            # Sort by match score
            sample_jobs.sort(key=lambda x: x["match_score"], reverse=True)
        
        return jsonify({
            "message": "Job search results",
            "total_jobs": len(sample_jobs),
            "jobs": sample_jobs,
            "note": "This is sample data. Integrate with real job APIs for production."
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Job search failed. Please try again."}), 500


@jobs_bp.route("/recommendations", methods=["GET"])
@token_required
def get_recommendations(user):
    """
    Get personalized job recommendations based on user's history and skills.
    """
    try:
        user_id = str(user["_id"])
        
        # Get user's match history to understand their skills
        history = get_user_history(user_id)
        
        # Extract skills from history
        all_skills = set()
        for entry in history:
            if "skill_overlap" in entry:
                all_skills.update(entry["skill_overlap"])
        
        user_skills = list(all_skills)
        
        # Sample recommended jobs based on user's skills
        recommended_jobs = [
            {
                "id": 101,
                "title": "Senior Full Stack Developer",
                "company": "Enterprise Solutions",
                "location": "Remote",
                "experience": "3-5 years",
                "skills_required": user_skills[:5] if len(user_skills) >= 5 else user_skills,
                "match_score": 92,
                "description": "We're looking for an experienced full stack developer.",
                "salary_range": "$100,000 - $140,000",
                "posted_date": "2025-12-04",
                "why_recommended": "Matches your skill profile"
            }
        ]
        
        return jsonify({
            "message": "Personalized job recommendations",
            "user_skills": user_skills,
            "total_recommendations": len(recommended_jobs),
            "jobs": recommended_jobs,
            "note": "Recommendations based on your match history. Integrate with real job APIs for production."
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Failed to get recommendations. Please try again."}), 500


@jobs_bp.route("/save", methods=["POST"])
@token_required
def save_job(user):
    """
    Save a job to user's saved jobs list.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        job_id = data.get("job_id")
        
        if not job_id:
            return jsonify({"error": "Job ID is required"}), 400
        
        # TODO: Implement saving to database
        # For now, return success message
        
        return jsonify({
            "message": "Job saved successfully",
            "job_id": job_id,
            "note": "Database integration pending"
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Failed to save job. Please try again."}), 500


@jobs_bp.route("/saved", methods=["GET"])
@token_required
def get_saved_jobs(user):
    """
    Get user's saved jobs.
    """
    try:
        user_id = str(user["_id"])
        
        # TODO: Fetch from database
        # For now, return empty list
        
        return jsonify({
            "message": "Saved jobs retrieved",
            "user_id": user_id,
            "saved_jobs": [],
            "note": "Database integration pending"
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Failed to retrieve saved jobs. Please try again."}), 500


@jobs_bp.route("/apply", methods=["POST"])
@token_required
def track_application(user):
    """
    Track job application status.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        job_id = data.get("job_id")
        status = data.get("status", "applied")  # applied, interviewing, offered, rejected
        
        if not job_id:
            return jsonify({"error": "Job ID is required"}), 400
        
        # TODO: Save application tracking to database
        
        return jsonify({
            "message": "Application tracked successfully",
            "job_id": job_id,
            "status": status,
            "note": "Database integration pending"
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Failed to track application. Please try again."}), 500


@jobs_bp.route("/applications", methods=["GET"])
@token_required
def get_applications(user):
    """
    Get user's job applications and their status.
    """
    try:
        user_id = str(user["_id"])
        
        # TODO: Fetch from database
        
        return jsonify({
            "message": "Applications retrieved",
            "user_id": user_id,
            "applications": [],
            "note": "Database integration pending"
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Failed to retrieve applications. Please try again."}), 500
