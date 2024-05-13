import pytest
from app import create_app, db
from app.models import User

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def init_database(app):
    with app.app_context():
        user = User(username='testuser', email='test@example.com', role='user', is_admin=False)
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        yield db
        db.session.remove()
        db.drop_all()
