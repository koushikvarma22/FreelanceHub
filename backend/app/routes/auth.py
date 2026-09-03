from flask import Blueprint, request, jsonify, current_app
from ..models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    role = data.get('role', 'freelancer').strip().lower()
    skills = data.get('skills', '').strip()
    hourly_rate = data.get('hourly_rate')

    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required'}), 400

    if role not in ['freelancer', 'client', 'admin']:
        role = 'freelancer'

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'An account with this email already exists'}), 400

    try:
        rate = float(hourly_rate) if hourly_rate else 0.0
    except (ValueError, TypeError):
        rate = 0.0

    user = User(
        name=name,
        email=email,
        role=role,
        skills=skills,
        hourly_rate=rate
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'Account created successfully',
        'user': user.to_dict()
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    token = user.generate_token(current_app.config['JWT_SECRET'])
    return jsonify({
        'token': token,
        'user': user.to_dict(include_details=True)
    })
