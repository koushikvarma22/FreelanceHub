import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from .models import db
from .seed import seed_database

def create_app():
    load_dotenv()

    app = Flask(__name__)

    # Configuration
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        db_url = 'mysql+pymysql://root:password@localhost:3306/freelancehub'

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET'] = os.getenv('JWT_SECRET', 'freelancehub-secret-key-super-secure-2026')

    # Enable CORS for all routes under /api
    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.projects import projects_bp
    from .routes.users import users_bp
    from .routes.applications import applications_bp
    from .routes.saved import saved_bp
    from .routes.notifications import notifications_bp
    from .routes.admin import admin_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(applications_bp, url_prefix='/api/applications')
    app.register_blueprint(saved_bp, url_prefix='/api/saved')
    app.register_blueprint(notifications_bp, url_prefix='/api/notifications')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')

    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'healthy', 'service': 'FreelanceHub Pro API'})

    # Initialize tables and seed data
    with app.app_context():
        try:
            db.create_all()
            seed_database()
        except Exception as e:
            print(f"Database initialization error with primary URI: {e}")
            # If MySQL connection error, fallback gracefully to SQLite so app never crashes
            if 'mysql' in app.config['SQLALCHEMY_DATABASE_URI']:
                print("Switching to SQLite database fallback (freelancehub.db)...")
                app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freelancehub.db'
                db.engine.dispose()
                db.init_app(app)
                db.create_all()
                seed_database()

    return app
