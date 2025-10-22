from datetime import datetime
from app import db

class AssetHistory(db.Model):
    __tablename__ = 'asset_history'
    
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.id'), nullable=False)
    action_type = db.Column(db.String(50), nullable=False)
    old_value = db.Column(db.Text)
    new_value = db.Column(db.Text)
    field_changed = db.Column(db.String(100))
    performed_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    
    user = db.relationship('User', backref='asset_changes')
    
    def __repr__(self):
        return f'<AssetHistory {self.action_type} on Asset {self.asset_id}>'
