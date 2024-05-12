from flask import Flask
from config import DevelopmentConfig, ProductionConfig, TestingConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    return app

app = create_app(TestingConfig)
