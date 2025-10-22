from flask import Blueprint

bp = Blueprint('assets', __name__)

from app.blueprints.assets import routes
