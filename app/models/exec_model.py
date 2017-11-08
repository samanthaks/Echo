"""exec_model.py"""
from app import db
from . import apt_model
from wtforms_alchemy import ModelForm

class Executive(db.Model):
    EID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    interest = db.Column(db.String(120), unique=False, nullable=True)
    appointments = db.relationship('Appointment', backref='executive', lazy=True)
    
    def __repr__(self):
        return '<Executive %r>' % self.name

class ExecForm(ModelForm):
    class Meta:
        model = Executive

