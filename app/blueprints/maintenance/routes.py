from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.blueprints.maintenance import bp
from app.models import Maintenance, Asset
from app import db
from datetime import datetime

@bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    asset_id = request.args.get('asset_id', '', type=int)
    
    query = Maintenance.query
    
    if asset_id:
        query = query.filter_by(asset_id=asset_id)
    
    maintenance_records = query.order_by(Maintenance.maintenance_date.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('maintenance/index.html',
                         maintenance_records=maintenance_records,
                         selected_asset=asset_id)

@bp.route('/add', methods=['GET', 'POST'])
@bp.route('/add/<int:asset_id>', methods=['GET', 'POST'])
@login_required
def add(asset_id=None):
    if not current_user.has_permission('staff'):
        flash('You do not have permission to add maintenance records.', 'error')
        return redirect(url_for('maintenance.index'))
    
    if request.method == 'POST':
        maintenance = Maintenance(
            asset_id=request.form['asset_id'],
            maintenance_date=datetime.strptime(request.form['maintenance_date'], '%Y-%m-%dT%H:%M') if request.form.get('maintenance_date') else datetime.utcnow(),
            issue_description_en=request.form['issue_description_en'],
            issue_description_ar=request.form.get('issue_description_ar'),
            action_taken_en=request.form.get('action_taken_en'),
            action_taken_ar=request.form.get('action_taken_ar'),
            technician_name=request.form.get('technician_name'),
            cost=request.form.get('cost') if request.form.get('cost') else None,
            status=request.form.get('status', 'completed'),
            completed_date=datetime.strptime(request.form['completed_date'], '%Y-%m-%dT%H:%M') if request.form.get('completed_date') else None,
            created_by=current_user.id
        )
        
        db.session.add(maintenance)
        db.session.commit()
        
        flash('Maintenance record added successfully!', 'success')
        return redirect(url_for('maintenance.index'))
    
    assets = Asset.query.order_by(Asset.asset_id).all()
    selected_asset = Asset.query.get(asset_id) if asset_id else None
    
    return render_template('maintenance/add.html',
                         assets=assets,
                         selected_asset=selected_asset)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    if not current_user.has_permission('staff'):
        flash('You do not have permission to edit maintenance records.', 'error')
        return redirect(url_for('maintenance.index'))
    
    maintenance = Maintenance.query.get_or_404(id)
    
    if request.method == 'POST':
        maintenance.asset_id = request.form['asset_id']
        maintenance.maintenance_date = datetime.strptime(request.form['maintenance_date'], '%Y-%m-%dT%H:%M')
        maintenance.issue_description_en = request.form['issue_description_en']
        maintenance.issue_description_ar = request.form.get('issue_description_ar')
        maintenance.action_taken_en = request.form.get('action_taken_en')
        maintenance.action_taken_ar = request.form.get('action_taken_ar')
        maintenance.technician_name = request.form.get('technician_name')
        maintenance.cost = request.form.get('cost') if request.form.get('cost') else None
        maintenance.status = request.form.get('status', 'completed')
        maintenance.completed_date = datetime.strptime(request.form['completed_date'], '%Y-%m-%dT%H:%M') if request.form.get('completed_date') else None
        
        db.session.commit()
        flash('Maintenance record updated successfully!', 'success')
        return redirect(url_for('maintenance.index'))
    
    assets = Asset.query.order_by(Asset.asset_id).all()
    
    return render_template('maintenance/edit.html',
                         maintenance=maintenance,
                         assets=assets)

@bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    if not current_user.has_permission('admin'):
        flash('You do not have permission to delete maintenance records.', 'error')
        return redirect(url_for('maintenance.index'))
    
    maintenance = Maintenance.query.get_or_404(id)
    db.session.delete(maintenance)
    db.session.commit()
    
    flash('Maintenance record deleted successfully!', 'success')
    return redirect(url_for('maintenance.index'))
