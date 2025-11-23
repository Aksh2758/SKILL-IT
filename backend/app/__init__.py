from flask import Flask
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

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    
    # Load Config
    app.config.from_object(Config)

    # Initialize DB
    mongo.init_app(app)

    # Enable CORS
    CORS(app)

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

    @app.get("/")
    def index():
        return {"message": "Skill-It Backend Running 😎"}

    return app
