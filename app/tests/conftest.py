import pytest
from app import create_app, db

@pytest.fixture(scope='module')
def app():
    """
    Create and configure a new app instance for each test.
    This fixture initializes the application, sets up the database, and tears it down after tests.
    """
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """
    A test client for the app. This client can be used to send test requests to the application.
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    A test runner for the app's Click commands. This can be used to invoke CLI commands within the app context.
    """
    return app.test_cli_runner()
