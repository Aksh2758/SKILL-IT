from flask import Blueprint, jsonify
from ..utils.decorators import token_required
from ..services.history_service import get_user_history

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/my-history", methods=["GET"])
@token_required
def history(current_user):
    user_id = str(current_user["_id"])
    data = get_user_history(user_id)

    for d in data:
        d["_id"] = str(d["_id"])

    return jsonify({"history": data}), 200
