from flask import Blueprint, request, jsonify
from .. import db
from ..models import User
from flask_jwt_extended import create_access_token
from .lessons import logicwordpuzzles 

auth_bp = Blueprint('auth', __name__)
lessons_bp = Blueprint('lessons', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'msg': 'Username already exists'}), 409

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    if not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({'msg': 'Missing required fields'}), 400
    return jsonify({'msg': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({'msg': 'Invalid credentials'}), 401

@lessons_bp.route("/api/lessons", methods=["GET"])
def get_lessons():
    return jsonify(logicwordpuzzles)
