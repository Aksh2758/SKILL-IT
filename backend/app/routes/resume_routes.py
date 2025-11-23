from flask import Blueprint, request, jsonify
from ..services.resume_analyzer import parse_resume_text, extract_skills_from_text

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/parse", methods=["POST"])
def parse_resume():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Resume text is required"}), 400

    parsed = parse_resume_text(text)
    return jsonify(parsed), 200


@resume_bp.route("/extract-skills", methods=["POST"])
def extract_skills():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Resume text is required"}), 400

    skills = extract_skills_from_text(text)
    return jsonify({"skills": skills}), 200
