from flask import Blueprint

usergroups = Blueprint('usergroups', __name__)

from . import routes