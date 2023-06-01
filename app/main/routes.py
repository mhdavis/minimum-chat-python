from flask import Flask, request, jsonify

main = Flask(__name__)

@main.route('/')
def home():
    return "Hello, World!"