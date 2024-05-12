from datetime import timedelta

class Config:
    """Base configuration settings."""
    SECRET_KEY = 'your-secret-key'  # Replace with your real key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///default.db'  # Main database URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret'  # Replace with your real JWT secret key
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)  # Access token expiration time

class ProductionConfig(Config):
    """Production specific configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/prod_db'  # Example production database URI

class DevelopmentConfig(Config):
    """Development environment specific configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'  # Development database

class TestingConfig(Config):
    """Testing environment specific configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for tests
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Shorter token for tests

