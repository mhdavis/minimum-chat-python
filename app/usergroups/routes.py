from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.usergroup import UserGroup
from datetime import datetime

usergroups = Blueprint('usergroups', __name__)

@usergroups.route('/usergroups', methods=['GET'])
def get_usergroups(): 
    all_usergroups = UserGroup.query.all()
    return jsonify([usergroup.to_dict() for usergroup in all_usergroups], 200)

@usergroups.route('/usergroups/<int:id>', methods=['GET'])
def get_usergroup(id):
    usergroup = UserGroup.query.get(id)
    if usergroup is None:
        return jsonify({"error": "UserGroup not found"}), 404
    else:
        return jsonify(usergroup.to_dict()), 200 

@usergroups.route('/usergroups', methods=['POST'])
def add_usergroup():
    data = request.get_json()
    new_usergroup = UserGroup(
        name=data['name'],
        description=data.get('description', ''),  # Default to empty string if not provided
        timestamp_created=datetime.utcnow()
    )
    db.session.add(new_usergroup)
    db.session.commit()
    return jsonify({"message": f"UserGroup {new_usergroup.id} created successfully!"}), 201

@usergroups.route('/usergroups/<int:id>', methods=['PUT'])
def update_usergroup(id):
    usergroup = UserGroup.query.get(id)
    if usergroup is None:
        return jsonify({"error": "UserGroup not found"}), 404
    else:
        data = request.get_json()
        usergroup.name = data.get('name', usergroup.name)
        usergroup.description = data.get('description', usergroup.description)
        db.session.commit()
        return jsonify({"message": f"UserGroup {usergroup.id} updated successfully!"}), 200

@usergroups.route('/usergroups/<int:id>', methods=['DELETE'])
def delete_usergroup(id):
    usergroup = UserGroup.query.get(id)
    if usergroup is None:
        return jsonify({"error": "UserGroup not found"}), 404
    else:
        db.session.delete(usergroup)
        db.session.commit()
        return jsonify({"message": f"UserGroup {usergroup.id} deleted successfully!"}), 200
