from flask import render_template
from flask_login import login_required, current_user
from app.blueprints.dashboard import bp
from app.models import Asset, Employee, Department, Maintenance
from sqlalchemy import func
from datetime import datetime, timedelta

@bp.route('/')
@login_required
def index():
    total_assets = Asset.query.count()
    total_employees = Employee.query.filter_by(is_active=True).count()
    total_departments = Department.query.filter_by(is_active=True).count()
    
    assets_by_type = db.session.query(
        Asset.asset_type,
        func.count(Asset.id).label('count')
    ).group_by(Asset.asset_type).all()
    
    assets_by_status = db.session.query(
        Asset.status,
        func.count(Asset.id).label('count')
    ).group_by(Asset.status).all()
    
    assets_by_department = db.session.query(
        Department.name_en,
        func.count(Asset.id).label('count')
    ).join(Asset, Asset.department_id == Department.id)\
     .group_by(Department.name_en).all()
    
    warranty_expiring = Asset.query.filter(
        Asset.warranty_expiry <= datetime.utcnow().date() + timedelta(days=30),
        Asset.warranty_expiry >= datetime.utcnow().date()
    ).count()
    
    recent_maintenance = Maintenance.query.order_by(
        Maintenance.maintenance_date.desc()
    ).limit(5).all()
    
    return render_template('dashboard/index.html',
                         total_assets=total_assets,
                         total_employees=total_employees,
                         total_departments=total_departments,
                         assets_by_type=dict(assets_by_type),
                         assets_by_status=dict(assets_by_status),
                         assets_by_department=dict(assets_by_department),
                         warranty_expiring=warranty_expiring,
                         recent_maintenance=recent_maintenance)

from app import db
