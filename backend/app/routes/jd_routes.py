from flask import Blueprint, request, jsonify
from ..services.jd_analyzer import extract_jd_skills, analyze_jd_text, calculate_similarity

jd_bp = Blueprint("jd", __name__)

@jd_bp.route("/analyze", methods=["POST"])
def analyze_jd():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "JD text is required"}), 400

    result = analyze_jd_text(text)
    return jsonify(result), 200


@jd_bp.route("/skills", methods=["POST"])
def jd_skills():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "JD text is required"}), 400

    skills = extract_jd_skills(text)
    return jsonify({"skills": skills}), 200

@jd_bp.route("/match", methods=["POST"])
def match_resume_jd():
    data = request.get_json()
    resume = data.get("resume", "")
    jd = data.get("jd", "")

    if not resume or not jd:
        return jsonify({"error": "Both resume and JD text are required"}), 400
    score = calculate_similarity(resume, jd)
    return jsonify({"match_score": score}), 200