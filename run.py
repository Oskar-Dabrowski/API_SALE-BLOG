from flask import Flask
from config import DevelopmentConfig, ProductionConfig, TestingConfig
import os

def create_app(config_class=None):
    app = Flask(__name__)
    if config_class is None:
        env = os.getenv('FLASK_ENV', 'development')
        if env == 'production':
            config_class = ProductionConfig
        elif env == 'testing':
            config_class = TestingConfig
        else:
            config_class = DevelopmentConfig
    app.config.from_object(config_class)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
