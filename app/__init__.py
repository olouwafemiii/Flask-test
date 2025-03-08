from flask import Flask
from flask_migrate import Migrate
from app.models import db
from flask_jwt_extended import JWTManager
from app.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://yann:password@db/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    db.init_app(app)
    Migrate(app, db)
    jwt = JWTManager(app)
    app.register_blueprint(auth_bp)
    return app
