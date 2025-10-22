from datetime import datetime
from app import db

class Maintenance(db.Model):
    __tablename__ = 'maintenance_records'
    
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'), nullable=False)
    maintenance_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    issue_description_en = db.Column(db.Text, nullable=False)
    issue_description_ar = db.Column(db.Text)
    action_taken_en = db.Column(db.Text)
    action_taken_ar = db.Column(db.Text)
    technician_name = db.Column(db.String(100))
    cost = db.Column(db.Numeric(10, 2))
    status = db.Column(db.String(50), default='completed')
    completed_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    creator = db.relationship('User', backref='maintenance_records')
    
    def __repr__(self):
        return f'<Maintenance {self.id} for Asset {self.asset_id}>'
