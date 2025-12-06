from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from .routes.auth_routes import auth_bp
from .routes.resume_routes import resume_bp
from .routes.jobs_routes import jobs_bp
from .routes.portfolio_routes import portfolio_bp
from .utils.config import Config
from .routes.jd_routes import jd_bp
from .routes.match_routes import match_bp
from .routes.career_routes import career_bp
from .routes.dashboard_routes import dashboard_bp
from .routes.report_routes import report_bp
from .routes.resume_builder_routes import resume_builder_bp
from datetime import datetime

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    
    # Load Config
    app.config.from_object(Config)

    # Initialize DB
    mongo.init_app(app)

    # Enable CORS with specific configuration
    # TODO: In production, replace '*' with specific frontend URL
    CORS(app, resources={
        r"/*": {
            "origins": ["http://localhost:3000", "http://localhost:3001"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Register Routes
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(resume_bp, url_prefix="/resume")
    app.register_blueprint(jobs_bp, url_prefix="/jobs")
    app.register_blueprint(portfolio_bp, url_prefix="/portfolio")
    app.register_blueprint(jd_bp, url_prefix="/jd")
    app.register_blueprint(match_bp, url_prefix="/match")
    app.register_blueprint(career_bp, url_prefix="/career")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(report_bp, url_prefix="/report")
    app.register_blueprint(resume_builder_bp, url_prefix="/resume-builder")

    # Root endpoint
    @app.get("/")
    def index():
        return {
            "message": "SKILL-IT Backend API",
            "status": "running",
            "version": "1.1.0",
            "endpoints": {
                "auth": "/auth",
                "resume": "/resume",
                "jobs": "/jobs",
                "portfolio": "/portfolio",
                "jd": "/jd",
                "match": "/match",
                "career": "/career",
                "dashboard": "/dashboard",
                "report": "/report",
                "resume_builder": "/resume-builder",
                "health": "/health"
            }
        }

    # Health check endpoint
    @app.get("/health")
    def health():
        try:
            # Check database connection
            mongo.db.command('ping')
            db_status = "healthy"
        except Exception as e:
            db_status = "unhealthy"
        
        return jsonify({
            "status": "healthy" if db_status == "healthy" else "degraded",
            "service": "SKILL-IT Backend",
            "timestamp": datetime.utcnow().isoformat(),
            "components": {
                "api": "healthy",
                "database": db_status
            }
        }), 200 if db_status == "healthy" else 503

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Endpoint not found",
            "message": "The requested URL was not found on the server."
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "error": "Internal server error",
            "message": "An unexpected error occurred. Please try again later."
        }), 500

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "error": "Method not allowed",
            "message": "The method is not allowed for the requested URL."
        }), 405

    return app
