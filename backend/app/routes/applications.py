from flask import Blueprint, request, jsonify, g
from ..models import db, Proposal, Project, Notification
from ..auth_helper import token_required

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/project/<int:project_id>', methods=['POST'])
@token_required
def submit_proposal(project_id):
    user = g.current_user
    project = Project.query.get_or_404(project_id)

    data = request.get_json() or {}
    proposal_text = data.get('proposal', '').strip()
    bid_amount = data.get('bid_amount')
    estimated_days = data.get('estimated_days', 7)

    if not proposal_text:
        return jsonify({'error': 'Proposal text is required'}), 400

    try:
        bid = float(bid_amount) if bid_amount is not None else float(project.budget)
        days = int(estimated_days) if estimated_days is not None else 7
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid bid amount or estimated days'}), 400

    # Create proposal
    prop = Proposal(
        project_id=project.id,
        freelancer_id=user.id,
        proposal=proposal_text,
        bid_amount=bid,
        estimated_days=days,
        status='submitted'
    )
    db.session.add(prop)

    # Create notification for client
    client_notification = Notification(
        user_id=project.client_id,
        title=f"New proposal for {project.title}",
        message=f"{user.name} submitted a bid of Rs. {int(bid):,} ({days} days): \"{proposal_text[:60]}...\""
    )
    db.session.add(client_notification)

    db.session.commit()

    return jsonify({
        'message': 'Proposal submitted successfully',
        'proposal': prop.to_dict()
    }), 201

@applications_bp.route('/project/<int:project_id>', methods=['GET'])
@token_required
def get_project_proposals(project_id):
    proposals = Proposal.query.filter_by(project_id=project_id).all()
    return jsonify([p.to_dict() for p in proposals])
