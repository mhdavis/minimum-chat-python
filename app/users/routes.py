from flask import Blueprint, request, jsonify

# TODO: replace with Database
users = {
    1: {
        'id': 1, 
        'firstName': 'Annie',
        'lastName': 'Baker',
        'username': 'abaker',
        'dateTimeCreated':  1234567890,
        },
    2: {
        'id': 2, 
        'firstName': 'John',
        'lastName': 'Smith',
        'username': 'jsmith',
        'dateTimeCreated':  1234567890,
        },
    # more users...
}

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@users.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    users[user['id']] = user
    return user, 200

@users.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    message = request.get_json()
    
    if id in users:
        users[id] = message
        return '', 204
    else:
        return f"User with id {id} not found.", 404

@users.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return '', 204
    else:
        return f"User with id {id} not found.", 404