from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models import db, User
from app.schemas import UserSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    schema = UserSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(email=data.get('email'), password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return schema.dump(new_user), 201

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data['password']

    user = User.query.filter((User.email == email)).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify({'token': token}), 200

@auth_bp.route('/users/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    schema = UserSchema()
    return schema.dump(user), 200
