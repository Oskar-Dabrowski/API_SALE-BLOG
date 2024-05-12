import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Ensure the path is correctly set up to find the 'config' module
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Assuming 'config.py' contains different classes for configurations
from config import DevelopmentConfig, ProductionConfig, TestingConfig

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_name=os.getenv('FLASK_ENV', 'development')):
    """
    Create a Flask application using the app factory pattern.

    :param config_name: The configuration environment to use (development, production, testing).
    """
    app = Flask(__name__)
    
    # Load configuration based on the FLASK_ENV environment variable
    if config_name == 'production':
        app.config.from_object(ProductionConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

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
