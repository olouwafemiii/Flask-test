from flask import Flask
from flask_migrate import Migrate
from app.models import db
from flask_jwt_extended import JWTManager
from app.routes import auth_bp
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    db.init_app(app)
    Migrate(app, db)
    jwt = JWTManager(app)
    app.register_blueprint(auth_bp)
    return app
