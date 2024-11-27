import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'postgresql://shorten_user:shorten_password@localhost:5433/shortenurl')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
