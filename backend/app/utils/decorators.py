import jwt
from functools import wraps
from flask import request, jsonify, current_app
from bson import ObjectId

def get_mongo():
    """Helper function to get mongo instance from current_app"""
    from flask_pymongo import PyMongo
    return current_app.extensions['pymongo']['MONGO'][0]

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token missing"}), 401

        try:
            mongo = get_mongo()
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user = mongo.db.users.find_one({"_id": ObjectId(data['user_id'])})
            
            if not user:
                return jsonify({"error": "User not found"}), 401
                
        except Exception as e:
            return jsonify({"error": "Invalid or expired token"}), 401

        return f(user, *args, **kwargs)
    return wrapper
