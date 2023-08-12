from flask import Blueprint

conversations = Blueprint('conversations', __name__)

from . import routes