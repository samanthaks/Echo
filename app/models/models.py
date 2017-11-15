from app import db
from werkzeug.security import check_password_hash
from wtforms_alchemy import ModelForm

class Appointment(db.Model):
    __tablename__ = 'appointment'
    AptID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    SID = db.Column(db.Integer, db.ForeignKey('student.SID'), nullable=True)
    EID = db.Column(db.Integer, db.ForeignKey('executive.EID'), nullable=False, info={'label':'Executive'})
    room = db.Column(db.String(10), unique=False, nullable=False, info={'label':'Location'})
    startTime = db.Column(db.DateTime, unique=False, nullable=False, info={'label':'Start Time'})
    endTime = db.Column(db.DateTime, unique=False, nullable=False, info={'label':'End Time'})
    state = db.Column(db.Integer, unique=False, nullable=False, default=0)

    def __repr__(self):
        return '<Appointment %r>' % self.AptID


class AptForm(ModelForm):
    class Meta:
        include = ['EID']
        model = Appointment

class Student(db.Model):
    __tablename__ = 'student'
    
    SID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    passwordHash = db.Column(db.String(200), unique=True, nullable=False)
    lifetimeID = db.Column(db.String(20), unique=True, nullable=False)
    program = db.Column(db.String(10), unique=False, nullable=False)
    interest = db.Column(db.String(120), unique=False, nullable=True)
    appointments = db.relationship('Appointment', backref='student')

    def __repr__(self):
        return '<Student %r>' % self.name

class StudentForm(ModelForm):
    class Meta:
        model = Student


class Executive(db.Model):
    __tablename__ = 'executive'
    
    EID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False, info={'label':'Executive Name'})
    interest = db.Column(db.String(120), unique=False, nullable=True, info={'label':'Field of Interest'})
    active = db.Column(db.Integer, nullable=False, default=0)
    appointments = db.relationship('Appointment', backref='executive')
    
    def __repr__(self):
        return '<Executive %r>' % self.name

class ExecForm(ModelForm):
    class Meta:
        model = Executive


class Admin(db.Model):
    __tablename__ = 'admin'
    
    email = db.Column(db.String(120), primary_key = True, nullable=False, info={'label':'Email'})
    password = db.Column(db.String(50), unique=True, nullable=False, info={'label':'Password'})
    active = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return '<Admin %r>' % self.email

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def validate_login(password_hash, password):
        """validate password"""
        return check_password_hash(password_hash, password)

class AdminForm(ModelForm):
    class Meta:
        include = ['email']
        model = Admin

