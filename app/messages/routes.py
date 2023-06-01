from flask import Blueprint, request, jsonify

messages = Blueprint('messages', __name__)

# TODO: replace with Database
messages = {
    1: {
        'id': 1, 
        'user': {
            'firstName': 'Annie',
            'lastName': 'Baker'
        },
        'message': 'I love this song',
        'dateTimeCreated':  1234567890,
        },
    2: {
        'id': 2, 
        'user': {
            'firstName': 'John',
            'lastName': 'Smith'
        },
        'message': 'hello to my friends',
        'dateTimeCreated':  1234567890,
        },
    # more messages...
}

@messages.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@messages.route('/messages', methods=['POST'])
def add_message():
    message = request.get_json()
    messages[message['id']] = message
    return message, 200

@messages.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    message = request.get_json()
    
    if id in messages:
        messages[id] = message
        return '', 204
    else:
        return f"Message with id {id} not found.", 404

@messages.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    if id in messages:
        del messages[id]
        return '', 204
    else:
        return f"Message with id {id} not found.", 404