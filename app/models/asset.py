from datetime import datetime
from app import db

class Asset(db.Model):
    __tablename__ = 'assets'
    
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.String(50), unique=True, nullable=False, index=True)
    asset_type = db.Column(db.String(50), nullable=False, index=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), unique=True, index=True)
    status = db.Column(db.String(50), nullable=False, default='available', index=True)
    purchase_date = db.Column(db.Date)
    warranty_expiry = db.Column(db.Date)
    location = db.Column(db.String(200))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('employees.id'))
    notes = db.Column(db.Text)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    maintenance_records = db.relationship('Maintenance', backref='asset', lazy='dynamic', cascade='all, delete-orphan')
    history_records = db.relationship('AssetHistory', backref='asset', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Asset {self.asset_id} - {self.asset_type}>'
    
    @property
    def is_warranty_valid(self):
        if self.warranty_expiry:
            return self.warranty_expiry > datetime.utcnow().date()
        return False
