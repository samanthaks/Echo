"""exec_model.py"""
from app import db
from wtforms_alchemy import ModelForm

class Appointment(db.Model):
    __tablename__ = 'appointment'
    AptID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    SID = db.Column(db.Integer, db.ForeignKey('student.SID'), nullable=True)
    EID = db.Column(db.Integer, db.ForeignKey('executive.EID'), nullable=False, info={'label':'Executive'})
    room = db.Column(db.String(10), unique=False, nullable=False, info={'label':'Room'})
    startTime = db.Column(db.DateTime, unique=False, nullable=False, info={'label':'Start Time'})
    endTime = db.Column(db.DateTime, unique=False, nullable=False, info={'label':'End Time'})
    state = db.Column(db.Integer, unique=False, nullable=False, default=0)

    def __repr__(self):
        return '<Appointment %r>' % self.AptID

class AptForm(ModelForm):
    class Meta:
        include = ['EID']
        model = Appointment

