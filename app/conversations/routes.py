from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.conversation import Conversation
from datetime import datetime

conversations = Blueprint('conversations', __name__)

@conversations.route('/conversations', methods=['GET'])
def get_conversations(): 
    all_conversations = Conversation.query.all()
    return jsonify([conversation.to_dict() for conversation in all_conversations], 200)

@conversations.route('/conversations/<int:id>', methods=['GET'])
def get_conversation(id):
    conversation = Conversation.query.get(id)
    if conversation is None:
        return jsonify({"error": "Conversation not found"}), 404
    else:
        return jsonify(conversation.to_dict()), 200 

@conversations.route('/conversations', methods=['POST'])
def add_conversation():
    data = request.get_json()
    new_conversation = Conversation(
        user_id=data['user_id'],
        participants=data['participants'],
        friend_id=data['friend_id'],
        timestamp_created= datetime.utcnow()
    )
    db.session.add(new_conversation)
    db.session.commit()
    return jsonify({"message": f"Conversation {new_conversation.id} created successfully!"}), 201

@conversations.route('/conversations/<int:id>', methods=['DELETE'])
def delete_conversation(id):
    conversation = Conversation.query.get(id)
    if conversation is None:
        return jsonify({"error": "Conversation not found"}), 404
    else:
        db.session.delete(conversation)
        db.session.commit()
        return jsonify({"message": f"Conversation {conversation.id} deleted successfully"}), 200