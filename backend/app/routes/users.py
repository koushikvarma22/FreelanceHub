from flask import Blueprint, request, jsonify, g
from ..models import db, User, Portfolio
from ..auth_helper import token_required

users_bp = Blueprint('users', __name__)

@users_bp.route('/freelancers/search', methods=['GET'])
def search_freelancers():
    q = request.args.get('q', '').strip()
    skill = request.args.get('skill', '').strip()

    query = User.query.filter_by(role='freelancer')

    if q:
        search = f"%{q}%"
        query = query.filter(
            (User.name.ilike(search)) |
            (User.bio.ilike(search)) |
            (User.skills.ilike(search))
        )

    if skill:
        query = query.filter(User.skills.ilike(f"%{skill}%"))

    freelancers = query.order_by(User.rating.desc(), User.review_count.desc()).all()
    return jsonify([f.to_dict() for f in freelancers])

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict(include_details=True))

@users_bp.route('/me', methods=['PUT'])
@token_required
def update_profile():
    user = g.current_user
    data = request.get_json() or {}

    if 'bio' in data:
        user.bio = data['bio']
    if 'skills' in data:
        user.skills = data['skills']
    if 'hourly_rate' in data and data['hourly_rate'] != '':
        try:
            user.hourly_rate = float(data['hourly_rate'])
        except (ValueError, TypeError):
            pass
    if 'experience_years' in data and data['experience_years'] != '':
        try:
            user.experience_years = int(data['experience_years'])
        except (ValueError, TypeError):
            pass
    if 'availability' in data:
        user.availability = data['availability']
    if 'location' in data:
        user.location = data['location']

    db.session.commit()
    return jsonify({
        'message': 'Profile updated successfully',
        'user': user.to_dict(include_details=True)
    })

@users_bp.route('/portfolio', methods=['POST'])
@token_required
def add_portfolio():
    user = g.current_user
    data = request.get_json() or {}

    title = data.get('title', '').strip()
    if not title:
        return jsonify({'error': 'Project title is required'}), 400

    item = Portfolio(
        user_id=user.id,
        title=title,
        description=data.get('description', '').strip(),
        technologies=data.get('technologies', '').strip(),
        github_url=data.get('github_url', '').strip(),
        live_url=data.get('live_url', '').strip()
    )
    db.session.add(item)
    db.session.commit()

    return jsonify({
        'message': 'Portfolio item added successfully',
        'portfolio': item.to_dict()
    }), 201
