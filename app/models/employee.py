from datetime import datetime
from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name_en = db.Column(db.String(120), nullable=False)
    name_ar = db.Column(db.String(120), nullable=False)
    job_title_en = db.Column(db.String(100))
    job_title_ar = db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    email = db.Column(db.String(120), unique=True, index=True)
    phone = db.Column(db.String(20))
    is_active = db.Column(db.Boolean, default=True)
    hire_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    assigned_assets = db.relationship('Asset', backref='assigned_employee', lazy='dynamic')
    
    def __repr__(self):
        return f'<Employee {self.employee_id} - {self.name_en}>'
