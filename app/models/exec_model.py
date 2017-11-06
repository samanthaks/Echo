"""exec_model.py"""
from app import db
from wtforms_alchemy import ModelForm

class Executives(db.Model):
    EID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    interest = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Executives %r>' % self.name

class ExecForm(ModelForm):
    class Meta:
        model = Executives

