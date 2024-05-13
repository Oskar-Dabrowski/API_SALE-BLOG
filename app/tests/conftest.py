import pytest
from app import create_app, db
from app.config import Config

@pytest.fixture(scope='module')
def app():
    """ Setup Flask app for testing. """
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """ A test client for the app. This client can be used to send test requests to the application. """
    return app.test_client()

@pytest.fixture
def runner(app):
    """ A test runner for the app's Click commands. This can be used to invoke CLI commands within the app context. """
    return app.test_cli_runner()
