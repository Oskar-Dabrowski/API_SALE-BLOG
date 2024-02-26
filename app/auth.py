from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    # Retrieve data from the request
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if the user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({'message': 'Email already registered'}), 400

    # Create a new user
    new_user = User(username=username, email=email)
    new_user.set_password(password)  # Assuming you have such a method in the User model

    # Adding a user to the database and saving changes
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()

    # Password check and user login
    if user and user.check_password(data.get('password')):
        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200
