class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'super-secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
