from flask import render_template, redirect, url_for, session, request
from app.blueprints.main import bp

@bp.route('/')
def index():
    return redirect(url_for('dashboard.index'))

@bp.route('/set_language/<language>')
def set_language(language):
    session['language'] = language
    return redirect(request.referrer or url_for('dashboard.index'))
