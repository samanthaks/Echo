"""exec_model.py"""
from app import db
from wtforms_alchemy import ModelForm

class Student(db.Model):
    SID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    passwordHash = db.Column(db.String(200), unique=True, nullable=False)
    lifetimeID = db.Column(db.String(20), unique=True, nullable=False)
    program = db.Column(db.String(10), unique=False, nullable=False)
    interest = db.Column(db.String(120), unique=False, nullable=True)
    appointments = db.relationship('Appointment', backref='student', lazy=True)

    def __repr__(self):
        return '<Student %r>' % self.name

class StudentForm(ModelForm):
    class Meta:
        model = Student

