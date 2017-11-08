"""exec_model.py"""
from app import db
from wtforms_alchemy import ModelForm

class Appointment(db.Model):
    AptID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    SID = db.Column(db.Integer, db.ForeignKey('student.SID'), nullable=False)
    EID = db.Column(db.Integer, db.ForeignKey('executive.EID'), nullable=False)
    room = db.Column(db.String(10), unique=False, nullable=False)
    startTime = db.Column(db.DateTime, unique=False, nullable=False)
    endTime = db.Column(db.DateTime, unique=False, nullable=False)
    state = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Appointment %r>' % self.AptID

class AptForm(ModelForm):
    class Meta:
        model = Appointment

