from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.blueprints.employees import bp
from app.models import Employee, Department, Asset, AssetHistory
from app import db
from datetime import datetime

@bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    department_id = request.args.get('department', '', type=int)
    
    query = Employee.query
    
    if search:
        query = query.filter(
            db.or_(
                Employee.employee_id.like(f'%{search}%'),
                Employee.name_en.like(f'%{search}%'),
                Employee.name_ar.like(f'%{search}%'),
                Employee.email.like(f'%{search}%')
            )
        )
    
    if department_id:
        query = query.filter_by(department_id=department_id)
    
    employees = query.order_by(Employee.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    departments = Department.query.filter_by(is_active=True).all()
    
    return render_template('employees/index.html',
                         employees=employees,
                         departments=departments,
                         search=search,
                         selected_department=department_id)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if not current_user.has_permission('staff'):
        flash('You do not have permission to add employees.', 'error')
        return redirect(url_for('employees.index'))
    
    if request.method == 'POST':
        employee = Employee(
            employee_id=request.form['employee_id'],
            name_en=request.form['name_en'],
            name_ar=request.form['name_ar'],
            job_title_en=request.form.get('job_title_en'),
            job_title_ar=request.form.get('job_title_ar'),
            department_id=request.form['department_id'],
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            hire_date=datetime.strptime(request.form['hire_date'], '%Y-%m-%d').date() if request.form.get('hire_date') else None
        )
        
        db.session.add(employee)
        db.session.commit()
        
        flash('Employee added successfully!', 'success')
        return redirect(url_for('employees.index'))
    
    departments = Department.query.filter_by(is_active=True).all()
    return render_template('employees/add.html', departments=departments)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    if not current_user.has_permission('staff'):
        flash('You do not have permission to edit employees.', 'error')
        return redirect(url_for('employees.index'))
    
    employee = Employee.query.get_or_404(id)
    
    if request.method == 'POST':
        employee.name_en = request.form['name_en']
        employee.name_ar = request.form['name_ar']
        employee.job_title_en = request.form.get('job_title_en')
        employee.job_title_ar = request.form.get('job_title_ar')
        employee.department_id = request.form['department_id']
        employee.email = request.form.get('email')
        employee.phone = request.form.get('phone')
        employee.hire_date = datetime.strptime(request.form['hire_date'], '%Y-%m-%d').date() if request.form.get('hire_date') else None
        employee.is_active = 'is_active' in request.form
        
        db.session.commit()
        flash('Employee updated successfully!', 'success')
        return redirect(url_for('employees.index'))
    
    departments = Department.query.filter_by(is_active=True).all()
    return render_template('employees/edit.html',
                         employee=employee,
                         departments=departments)

@bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    if not current_user.has_permission('admin'):
        flash('You do not have permission to delete employees.', 'error')
        return redirect(url_for('employees.index'))
    
    employee = Employee.query.get_or_404(id)
    
    if employee.assigned_assets.count() > 0:
        flash('Cannot delete employee with assigned assets. Please unassign all assets first.', 'error')
        return redirect(url_for('employees.index'))
    
    db.session.delete(employee)
    db.session.commit()
    
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('employees.index'))

@bp.route('/view/<int:id>')
@login_required
def view(id):
    employee = Employee.query.get_or_404(id)
    assigned_assets = employee.assigned_assets.all()
    
    return render_template('employees/view.html',
                         employee=employee,
                         assigned_assets=assigned_assets)
