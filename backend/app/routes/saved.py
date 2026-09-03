from flask import Blueprint, request, jsonify, g
from ..models import db, SavedProject, Project
from ..auth_helper import token_required

saved_bp = Blueprint('saved', __name__)

@saved_bp.route('/<int:project_id>', methods=['POST'])
@token_required
def save_project(project_id):
    user = g.current_user
    project = Project.query.get_or_404(project_id)

    existing = SavedProject.query.filter_by(user_id=user.id, project_id=project_id).first()
    if not existing:
        saved = SavedProject(user_id=user.id, project_id=project_id)
        db.session.add(saved)
        db.session.commit()

    return jsonify({'message': 'Project saved successfully'}), 200

@saved_bp.route('', methods=['GET'])
@saved_bp.route('/', methods=['GET'])
@token_required
def get_saved_projects():
    user = g.current_user
    saved_entries = SavedProject.query.filter_by(user_id=user.id).all()
    project_ids = [s.project_id for s in saved_entries]
    projects = Project.query.filter(Project.id.in_(project_ids)).all() if project_ids else []
    return jsonify([p.to_dict() for p in projects])
