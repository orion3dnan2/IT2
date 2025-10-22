from flask import Blueprint

bp = Blueprint('maintenance', __name__)

from app.blueprints.maintenance import routes
