from flask import Blueprint, jsonify
from ..models import User, Project, Proposal

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/stats', methods=['GET'])
def get_stats():
    total_users = User.query.count()
    total_freelancers = User.query.filter_by(role='freelancer').count()
    total_clients = User.query.filter_by(role='client').count()
    total_projects = Project.query.count()
    total_proposals = Proposal.query.count()

    return jsonify({
        'total_users': total_users,
        'total_freelancers': total_freelancers,
        'freelancers': total_freelancers,
        'total_clients': total_clients,
        'clients': total_clients,
        'total_projects': total_projects,
        'active_projects': total_projects,
        'total_proposals': total_proposals,
        'submitted_proposals': total_proposals
    })
