from flask import Blueprint

app = Blueprint('app_bp', __name__)

from . import routes