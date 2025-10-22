from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.blueprints.assets import bp
from app.models import Asset, Employee, Department, AssetHistory
from app import db
from datetime import datetime

@bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    asset_type = request.args.get('type', '')
    status = request.args.get('status', '')
    department_id = request.args.get('department', '', type=int)
    
    query = Asset.query
    
    if search:
        query = query.filter(
            db.or_(
                Asset.asset_id.like(f'%{search}%'),
                Asset.brand.like(f'%{search}%'),
                Asset.model.like(f'%{search}%'),
                Asset.serial_number.like(f'%{search}%')
            )
        )
    
    if asset_type:
        query = query.filter_by(asset_type=asset_type)
    
    if status:
        query = query.filter_by(status=status)
    
    if department_id:
        query = query.filter_by(department_id=department_id)
    
    assets = query.order_by(Asset.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    departments = Department.query.filter_by(is_active=True).all()
    
    return render_template('assets/index.html',
                         assets=assets,
                         departments=departments,
                         search=search,
                         selected_type=asset_type,
                         selected_status=status,
                         selected_department=department_id)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.has_permission('staff'):
        flash('You do not have permission to add assets.', 'error')
        return redirect(url_for('assets.index'))
    
    if request.method == 'POST':
        asset = Asset(
            asset_id=request.form['asset_id'],
            asset_type=request.form['asset_type'],
            brand=request.form['brand'],
            model=request.form['model'],
            serial_number=request.form['serial_number'],
            status=request.form['status'],
            purchase_date=datetime.strptime(request.form['purchase_date'], '%Y-%m-%d').date() if request.form.get('purchase_date') else None,
            warranty_expiry=datetime.strptime(request.form['warranty_expiry'], '%Y-%m-%d').date() if request.form.get('warranty_expiry') else None,
            location=request.form.get('location'),
            department_id=request.form.get('department_id') if request.form.get('department_id') else None,
            assigned_to=request.form.get('assigned_to') if request.form.get('assigned_to') else None,
            notes=request.form.get('notes')
        )
        
        db.session.add(asset)
        db.session.commit()
        
        history = AssetHistory(
            asset_id=asset.id,
            action_type='created',
            new_value=f'Asset {asset.asset_id} created',
            performed_by=current_user.id,
            notes='Asset created in system'
        )
        db.session.add(history)
        db.session.commit()
        
        flash('Asset added successfully!', 'success')
        return redirect(url_for('assets.index'))
    
    departments = Department.query.filter_by(is_active=True).all()
    employees = Employee.query.filter_by(is_active=True).all()
    
    return render_template('assets/add.html',
                         departments=departments,
                         employees=employees)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    if not current_user.has_permission('staff'):
        flash('You do not have permission to edit assets.', 'error')
        return redirect(url_for('assets.index'))
    
    asset = Asset.query.get_or_404(id)
    
    if request.method == 'POST':
        changes = []
        
        if asset.asset_type != request.form['asset_type']:
            changes.append(f"Type: {asset.asset_type} → {request.form['asset_type']}")
            asset.asset_type = request.form['asset_type']
        
        if asset.status != request.form['status']:
            changes.append(f"Status: {asset.status} → {request.form['status']}")
            asset.status = request.form['status']
        
        asset.brand = request.form['brand']
        asset.model = request.form['model']
        asset.serial_number = request.form['serial_number']
        asset.purchase_date = datetime.strptime(request.form['purchase_date'], '%Y-%m-%d').date() if request.form.get('purchase_date') else None
        asset.warranty_expiry = datetime.strptime(request.form['warranty_expiry'], '%Y-%m-%d').date() if request.form.get('warranty_expiry') else None
        asset.location = request.form.get('location')
        asset.department_id = request.form.get('department_id') if request.form.get('department_id') else None
        asset.assigned_to = request.form.get('assigned_to') if request.form.get('assigned_to') else None
        asset.notes = request.form.get('notes')
        
        db.session.commit()
        
        if changes:
            history = AssetHistory(
                asset_id=asset.id,
                action_type='updated',
                new_value=', '.join(changes),
                performed_by=current_user.id,
                notes='Asset updated'
            )
            db.session.add(history)
            db.session.commit()
        
        flash('Asset updated successfully!', 'success')
        return redirect(url_for('assets.index'))
    
    departments = Department.query.filter_by(is_active=True).all()
    employees = Employee.query.filter_by(is_active=True).all()
    
    return render_template('assets/edit.html',
                         asset=asset,
                         departments=departments,
                         employees=employees)

@bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    if not current_user.has_permission('admin'):
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    asset = Asset.query.get_or_404(id)
    db.session.delete(asset)
    db.session.commit()
    
    flash('Asset deleted successfully!', 'success')
    return redirect(url_for('assets.index'))

@bp.route('/view/<int:id>')
@login_required
def view(id):
    asset = Asset.query.get_or_404(id)
    history = AssetHistory.query.filter_by(asset_id=id).order_by(AssetHistory.timestamp.desc()).all()
    maintenance = asset.maintenance_records.order_by(Maintenance.maintenance_date.desc()).all()
    
    return render_template('assets/view.html',
                         asset=asset,
                         history=history,
                         maintenance=maintenance)
