from flask import Blueprint, request, jsonify
from .. import mongo 
import bcrypt
import jwt 
from datetime import datetime, timedelta, timezone

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

@auth_bp.route('/login', methods=['POST'])
def login():
    # 1. user data from the requests
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # 2. Finding User in db
    user = mongo.db.users.find_one({'email': email})

    # 3. Checking if user with correct password exist
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({'error': 'Invalid credentials'}), 401 # 401 Unauthorized

    # 4. If credentials, create a token
    token = jwt.encode({
        'user_id': str(user['_id']),
        'exp': datetime.now(timezone.utc) + timedelta(hours=24) # Token expires in 24 hours
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    # 5. Return the token to the client
    return jsonify({
        'message': 'Login successful!',
        'token': token
    }), 200