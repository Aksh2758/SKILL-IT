from flask import Blueprint, request, jsonify
from .. import mongo # Import the mongo instance from __init__.py
import bcrypt

# "Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # 1. Get user data from the incoming request JSON
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # 2. Basic validation
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # 3. Check if user already exists in the database
    if mongo.db.users.find_one({'email': email}):
        return jsonify({'error': 'User with this email already exists'}), 409 

    # 4. Hash the password for security
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # 5. Insert user to db
    user_id = mongo.db.users.insert_one({
        'email': email,
        'password': hashed_password
    }).inserted_id

    # 6. Return a success response
    return jsonify({
        'message': 'User registered successfully!',
        'user_id': str(user_id)
    }), 201 
