from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.message import Message
from datetime import datetime

messages = Blueprint('messages', __name__)

@messages.route('/messages', methods=['GET'])
def get_messages(): 
    all_messages = Message.query.all()
    return jsonify([message.to_dict() for message in all_messages], 200)

@messages.route('/messages/<int:id>', methods=['GET'])
def get_message(id):
    message = Message.query.get(id)
    if message is None:
        return jsonify({"error": "Message not found"}), 404
    else:
        return jsonify(message.to_dict()), 200 

@messages.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    new_message = Message(
        user_id=data['user_id'],
        content=data['content'],
        timestamp_created= datetime.utcnow()
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message": f"Message {new_message.id} created successfully!"}), 201

@messages.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    message = Message.query.get(id)
    if message is None:
        return jsonify({"error": "Message not found"}), 404
    else:
        data = request.get_json()
        if 'content' in data:
            message.content = data['content']
            message.is_editted = True
            message.timestamp_editted = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": f"fMessage {message.id} updated successfully!"}), 200

@messages.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get(id)
    if message is None:
        return jsonify({"error": "Message not found"}), 404
    else:
        db.session.delete(message)
        db.session.commit()
        return jsonify({"message": f"Message {message.id} deleted successfully"}), 200