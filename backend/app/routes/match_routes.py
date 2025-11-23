from flask import Blueprint, request, jsonify
from ..services.match_engine import (
    calculate_skill_match,
    calculate_text_similarity,
    generate_final_score
)
from ..services.history_service import save_match_history
from ..utils.decorators import token_required


match_bp = Blueprint("match", __name__)

@match_bp.route("/calculate", methods=["POST"])
@token_required
def calculate_match():
    data = request.get_json()

    resume_text = data.get("resume_text", "")
    jd_text = data.get("jd_text", "")
    resume_skills = data.get("resume_skills", [])
    jd_skills = data.get("jd_skills", [])

    if not resume_text or not jd_text:
        return jsonify({"error": "Both resume text and JD text required"}), 400

    # 1. Skill gap analysis
    skill_data = calculate_skill_match(resume_skills, jd_skills)

    # 2. Text similarity
    text_score = calculate_text_similarity(resume_text, jd_text)

    # 3. Final score
    final_score = generate_final_score(
        skill_data["skill_match_percent"],
        text_score
    )

    save_match_history(
        user_id=str(current_user["_id"]),
        final_score=final_score,
        overlap=skill_data["overlap_skills"],
        missing=skill_data["missing_skills"],
        role="N/A",
        match_percent=skill_data["skill_match_percent"]
    )

    return jsonify({
        "skill_overlap": skill_data["overlap_skills"],
        "missing_skills": skill_data["missing_skills"],
        "skill_match_percent": skill_data["skill_match_percent"],
        "text_similarity": text_score,
        "final_score": final_score
    }), 200
