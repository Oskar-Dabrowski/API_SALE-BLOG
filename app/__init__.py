from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask extensions outside of the create_app function
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the application
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import and registration of blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    return app
