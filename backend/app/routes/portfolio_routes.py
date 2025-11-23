from flask import Blueprint, request, jsonify
from ..services.portfolio_service import build_portfolio

portfolio_bp = Blueprint("portfolio", __name__)

@portfolio_bp.route("/generate", methods=["POST"])
def generate_portfolio():
    data = request.get_json()
    skills = data.get("skills", [])

    if not skills:
        return jsonify({"error": "Skills required"}), 400

    result = build_portfolio(skills)
    return jsonify(result), 200
