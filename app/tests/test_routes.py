import pytest
from app.models import User

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_post_route(client, init_database):
    user = User.query.filter_by(username='testuser').first()
    assert user is not None

    response = client.post('/auth/login', json={'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200
    access_token = response.get_json()['access_token']

    response = client.post('/posts', json={'title': 'New Post', 'content': 'New Content'}, headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 201

def test_protected_route_without_auth(client):
    response = client.get('/auth/protected')
    assert response.status_code == 401
