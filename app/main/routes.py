from . import main

@main.route('/')
def home():
    return "Hello, World!"