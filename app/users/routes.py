from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.user import User
from datetime import datetime

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    return jsonify([user.to_dict() for user in all_users]), 200

@users.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(user.to_dict()), 200

@users.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        first_name=data['first_name'], 
        last_name=data['last_name'], 
        username=data['username'], 
        email=data['email'], 
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": f"User {new_user.id} created successfully!"}), 201

@users.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    else:
        data = request.get_json()
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.timestamp_created = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": f"User {user.id} updated successfully!"}), 200

@users.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    else:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User {user.id} deleted successfully!"}), 200