from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Tworzenie instancji rozszerzeń
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Konfiguracja aplikacji
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicjalizacja rozszerzeń z aplikacją
    db.init_app(app)
    migrate = Migrate(app, db)  # Inicjalizacja migracji
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Rejestracja blueprintów
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Funkcja ładowania użytkownika dla Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))
    
    return app
