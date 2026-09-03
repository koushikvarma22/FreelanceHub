import os
from datetime import datetime, timezone
import jwt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='freelancer') # freelancer, client, admin
    bio = db.Column(db.Text, default='')
    skills = db.Column(db.String(255), default='')
    hourly_rate = db.Column(db.Float, default=0.0)
    experience_years = db.Column(db.Integer, default=1)
    availability = db.Column(db.String(50), default='available')
    location = db.Column(db.String(100), default='')
    rating = db.Column(db.Float, default=5.0)
    review_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    portfolios = db.relationship('Portfolio', backref='user', lazy=True, cascade="all, delete-orphan")
    projects = db.relationship('Project', backref='client_user', lazy=True, foreign_keys='Project.client_id')
    proposals = db.relationship('Proposal', backref='freelancer', lazy=True, foreign_keys='Proposal.freelancer_id')
    notifications = db.relationship('Notification', backref='user', lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_token(self, secret):
        payload = {
            'user_id': self.id,
            'role': self.role,
            'email': self.email,
            'name': self.name
        }
        return jwt.encode(payload, secret, algorithm='HS256')

    def to_dict(self, include_details=False):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'bio': self.bio or '',
            'skills': self.skills or '',
            'hourly_rate': self.hourly_rate or 0,
            'experience_years': self.experience_years or 1,
            'availability': self.availability or 'available',
            'location': self.location or '',
            'rating': round(self.rating or 5.0, 1),
            'review_count': self.review_count or 0
        }
        if include_details:
            data['portfolio'] = [p.to_dict() for p in self.portfolios]
        return data


class Portfolio(db.Model):
    __tablename__ = 'portfolios'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, default='')
    technologies = db.Column(db.String(255), default='')
    github_url = db.Column(db.String(255), default='')
    live_url = db.Column(db.String(255), default='')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'technologies': self.technologies,
            'github_url': self.github_url,
            'live_url': self.live_url
        }


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills = db.Column(db.String(255), default='')
    budget = db.Column(db.Float, nullable=False, default=0.0)
    deadline = db.Column(db.String(50), default='')
    experience_level = db.Column(db.String(50), default='intermediate')
    project_type = db.Column(db.String(50), default='fixed')
    status = db.Column(db.String(50), default='open')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    proposals = db.relationship('Proposal', backref='project', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        client_name = self.client_user.name if self.client_user else 'Client'
        return {
            'id': self.id,
            'client_id': self.client_id,
            'client': client_name,
            'title': self.title,
            'description': self.description,
            'skills': self.skills,
            'budget': self.budget,
            'deadline': self.deadline,
            'experience_level': self.experience_level,
            'project_type': self.project_type,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'proposal_count': len(self.proposals)
        }


class Proposal(db.Model):
    __tablename__ = 'proposals'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    freelancer_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    proposal = db.Column(db.Text, nullable=False)
    bid_amount = db.Column(db.Float, nullable=False)
    estimated_days = db.Column(db.Integer, nullable=False, default=7)
    status = db.Column(db.String(50), default='submitted')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'freelancer_id': self.freelancer_id,
            'freelancer_name': self.freelancer.name if self.freelancer else 'Freelancer',
            'proposal': self.proposal,
            'bid_amount': self.bid_amount,
            'estimated_days': self.estimated_days,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class SavedProject(db.Model):
    __tablename__ = 'saved_projects'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))


class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Milestone(db.Model):
    __tablename__ = 'milestones'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending') # pending, funded, released
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'title': self.title,
            'amount': self.amount,
            'status': self.status
        }
