from flask import Blueprint, request, jsonify, g
from ..models import db, Project
from ..auth_helper import token_required

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('', methods=['GET'])
@projects_bp.route('/', methods=['GET'])
def get_projects():
    q = request.args.get('q', '').strip()
    skill = request.args.get('skill', '').strip()
    min_budget = request.args.get('min_budget', '').strip()
    max_budget = request.args.get('max_budget', '').strip()
    experience = request.args.get('experience', '').strip()
    project_type = request.args.get('project_type', '').strip()

    query = Project.query

    if q:
        search = f"%{q}%"
        query = query.filter(
            (Project.title.ilike(search)) |
            (Project.description.ilike(search)) |
            (Project.skills.ilike(search))
        )

    if skill:
        query = query.filter(Project.skills.ilike(f"%{skill}%"))

    if min_budget:
        try:
            query = query.filter(Project.budget >= float(min_budget))
        except ValueError:
            pass

    if max_budget:
        try:
            query = query.filter(Project.budget <= float(max_budget))
        except ValueError:
            pass

    if experience:
        query = query.filter(Project.experience_level.ilike(f"%{experience}%"))

    if project_type:
        query = query.filter(Project.project_type.ilike(f"%{project_type}%"))

    projects = query.order_by(Project.created_at.desc()).all()
    return jsonify([p.to_dict() for p in projects])

@projects_bp.route('', methods=['POST'])
@projects_bp.route('/', methods=['POST'])
@token_required
def create_project():
    user = g.current_user
    data = request.get_json() or {}

    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    skills = data.get('skills', '').strip()
    budget = data.get('budget')
    deadline = data.get('deadline', '').strip()
    experience_level = data.get('experience_level', 'intermediate').strip()
    project_type = data.get('project_type', 'fixed').strip()

    if not title or not description or budget is None:
        return jsonify({'error': 'Title, description, and budget are required'}), 400

    try:
        budget_val = float(budget)
    except (ValueError, TypeError):
        return jsonify({'error': 'Budget must be a valid number'}), 400

    project = Project(
        client_id=user.id,
        title=title,
        description=description,
        skills=skills,
        budget=budget_val,
        deadline=deadline,
        experience_level=experience_level,
        project_type=project_type,
        status='open'
    )
    db.session.add(project)
    db.session.commit()

    return jsonify({
        'message': 'Project posted successfully',
        'project': project.to_dict()
    }), 201

@projects_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict())
