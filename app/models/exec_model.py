"""exec_model.py"""
from app import db
from . import apt_model
from wtforms_alchemy import ModelForm

class Executive(db.Model):
    __tablename__ = 'executive'
    
    EID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False, info={'label':'Executive Name'})
    interest = db.Column(db.String(120), unique=False, nullable=True, info={'label':'Field of Interest'})
    active = db.Column(db.Integer, nullable=False, default=0)
    appointments = db.relationship('Appointment', backref='executive')
    
    def __repr__(self):
        return '<Executive %r>' % self.name

    def __init__(self, name, interest):
        self.name = name
        self.interest = interest

class ExecForm(ModelForm):
    class Meta:
        model = Executive

