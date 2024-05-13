def test_app_initialization(app):
    assert app is not None

def test_config(app):
    assert app.config['TESTING']
