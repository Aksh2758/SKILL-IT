from flask import Blueprint, request, jsonify
from ..services.career_agent import generate_career_path

career_bp = Blueprint("career", __name__)

@career_bp.route("/advisor", methods=["POST"])
def advisor():
    data = request.get_json()
    resume_skills = data.get("skills", [])

    if not resume_skills:
        return jsonify({"error": "Skills list required"}), 400

    result = generate_career_path(resume_skills)
    return jsonify(result), 200
