from flask import Blueprint

bp = Blueprint('employees', __name__)

from app.blueprints.employees import routes
