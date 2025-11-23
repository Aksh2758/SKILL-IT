import jwt
from functools import wraps
from flask import request, jsonify, current_app
from .. import mongo

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token missing"}), 401

        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user = mongo.db.users.find_one({"_id": ObjectId(data['user_id'])})
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(user, *args, **kwargs)
    return wrapper
