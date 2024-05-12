from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'super-secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
