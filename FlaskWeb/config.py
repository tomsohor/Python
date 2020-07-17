import os


class Config:
    SECRET_KEY = '98d48ebbe9b13a2454fbca6cf6c309ed'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@localhost:5432/FlaskWeb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')