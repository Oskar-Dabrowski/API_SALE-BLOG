import pytest
from app import create_app, db
from app.models import User, Post

def test_create_user(app):
    with app.app_context():
        user = User(username='testuser', email='test@example.com', role='user', is_admin=False)
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        assert user.id is not None

def test_create_post(app):
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None

        post = Post(title='Test Post', content='Test Content', author=user)
        db.session.add(post)
        db.session.commit()
        assert post.id is not None
