from datetime import datetime
from app import db

class Department(db.Model):
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(100), nullable=False)
    name_ar = db.Column(db.String(100), nullable=False)
    description_en = db.Column(db.Text)
    description_ar = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    employees = db.relationship('Employee', backref='department', lazy='dynamic')
    assets = db.relationship('Asset', backref='department', lazy='dynamic')
    
    def __repr__(self):
        return f'<Department {self.name_en}>'
