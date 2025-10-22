from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, current_user
from app.blueprints.auth import bp
from app.models import User
from app import db
from datetime import datetime

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            if not user.is_active:
                flash('Your account has been deactivated. Please contact the administrator.', 'error')
                return redirect(url_for('auth.login'))
            
            user.last_login = datetime.utcnow()
            db.session.commit()
            login_user(user, remember=remember)
            
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard.index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
