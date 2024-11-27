from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})
    db.init_app(app)

    with app.app_context():
        from models import URL
        db.create_all()

    return app
