import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Ensure the path is correctly set up to find the 'config' module
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    """
    Create a Flask application using the app factory pattern.
    """
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
  # Use Config to load configuration

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import and register blueprints
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
