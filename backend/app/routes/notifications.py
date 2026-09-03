from flask import Blueprint, jsonify, g
from ..models import Notification
from ..auth_helper import token_required

notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('', methods=['GET'])
@notifications_bp.route('/', methods=['GET'])
@token_required
def get_notifications():
    user = g.current_user
    notes = Notification.query.filter_by(user_id=user.id).order_by(Notification.created_at.desc()).all()
    return jsonify([n.to_dict() for n in notes])
