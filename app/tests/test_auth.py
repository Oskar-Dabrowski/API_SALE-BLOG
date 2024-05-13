def test_register_user(client):
    response = client.post('/auth/register', json={
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'newpassword'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User successfully registered'

def test_register_existing_user(client, init_database):
    response = client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Email already in use'

def test_login_user(client, init_database):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json
    assert response.json['is_admin'] is False

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'
