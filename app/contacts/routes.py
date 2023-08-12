from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.contact import Contact
from datetime import datetime

contacts = Blueprint('contacts', __name__)

@contacts.route('/contacts', methods=['GET'])
def get_contacts(): 
    all_contacts = Contact.query.all()
    return jsonify([contact.to_dict() for contact in all_contacts], 200)

@contacts.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return jsonify({"error": "Contact not found"}), 404
    else:
        return jsonify(contact.to_dict()), 200 

@contacts.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = Contact(
        user_id=data['user_id'],
        friend_id=data['friend_id'],
        timestamp_created= datetime.utcnow()
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": f"Contact {new_contact.id} created successfully!"}), 201

@contacts.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact is None:
        return jsonify({"error": "Contact not found"}), 404
    else:
        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": f"Contact {contact.id} deleted successfully"}), 200