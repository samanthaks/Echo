"""Admin Route"""
from flask import Blueprint, render_template, session, request, flash, session, redirect, url_for, jsonify
from app.models.models import Appointment, AptForm, Executive, ExecForm, Admin, AdminForm
from app import db
from app.models.verification_mock_login import VerificationMockForm
from app.CBSLogin.CBSLogin import CBSLogin
from datetime import datetime

admin = Blueprint('admin', __name__, template_folder='../templates')
global CBSUser

@admin.route('/adminHome')
def admin_homepage():
    return render_template('admin_home.html')

@admin.route('/adminLogin', methods=['GET', 'POST'])
def admin_login():
    form = AdminForm(request.form)
    if request.method == 'POST':
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and admin.validate_login(admin.password, form.password.data):
            session['email'] = admin.email
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get('next') or url_for("admin.admin_homepage"))
        flash("Wrong password!", category='error')
        return render_template('admin_login.html', form=form)
    else:
        return render_template('admin_login.html', form=form)

@admin.route('/manageCalendars')
def manage_calendars():
    """The home page."""
    # if 'Username' in session:
    #     return render_template('user_index.html')
    return render_template('admin_calendars.html')

@admin.route('/createMeeting_v1', methods=['GET', 'POST'])
def create_meeting_v1():
    form = AptForm(request.form)
    if request.method == 'GET':
        form.EID.choices = [(Exec.EID, Exec.name) for Exec in Executive.query.order_by(Executive.name).filter_by(active=1).all()]
        return render_template('create_meeting_v1.html', form=form)
    if request.method == 'POST':
        appointment = Appointment()
        form.populate_obj(appointment)
        appointment.startTime = datetime.strptime(form.startTime._value(), "%Y-%m-%dT%H:%M")
        appointment.endTime = datetime.strptime(form.endTime._value(), "%Y-%m-%dT%H:%M")
        db.session.add(appointment)
        db.session.commit()
        flash("Appointments Made!", category='success')
        return redirect(url_for('admin.manage_calendars'))

@admin.route('/addExec', methods=['GET', 'POST'])
def add_exec():
    form = ExecForm(request.form)
    if request.method == 'GET':
        return render_template('add_exec.html', form=form)
    if request.method == 'POST' and form.validate():
        executive = Executive()
        form.populate_obj(executive)
        db.session.add(executive)
        db.session.commit()
        flash("Executive successfully added!", category="success")
        return redirect(url_for('admin.manage_calendars'))

@admin.route('/viewExec')
def view_exec():
    execs = Executive.query.order_by(Executive.name).filter_by(active=0).all()
    return render_template('view_execs.html', execs=execs)

@admin.route('/verificationMockLogin', methods=['GET','POST'])
def verification_mock_login():
    form = VerificationMockForm(request.form)
    if request.method == 'GET':
        return render_template('verification_mock_login.html', form=form)   
    elif request.method == 'POST' and form.validate():
        global CBSUser 
        CBSUser = CBSLogin(form.username.data, form.password.data)
        return redirect(url_for('admin.verification_mock'))

@admin.route('/verificationMock', methods=['GET','POST'])
def verification_mock():
    form = VerificationMockForm(request.form)
    if request.method == 'GET':
        return render_template('verification_mock.html', form=form)
    elif request.method == 'POST' and form.validate():
        name, program, entry_term, cluster, email = CBSUser.getInfo(form.username.data)
        data = {'lifetimeID': form.username.data, 'name': name, 'program': program, 'entry_term': entry_term, 'cluster': cluster, 'email': email}
        return render_template('verification_mock.html', form=form, data=data)

@admin.route('/createMeeting_v2', methods=['GET', 'POST'])
def create_meeting_v2():
    form = AptForm(request.form)
    if request.method == 'GET':
        execs = Executive.query.order_by(Executive.name).filter_by(active=1).all()

        return render_template('create_meeting_v2.html', form=form, execs=execs)
    if request.method == 'POST':
        flash("Appointments Made!", category='success')
        return redirect(url_for('admin.manage_calendars'))

@admin.route('/waitlists')
def manage_waitlists():
    return render_template('admin_waitlists.html')

@admin.route('/meetings')
def manage_appts():
    appts = Appointment.query.order_by(Appointment.startTime).all()
    execs = Executive.query.order_by(Executive.EID).filter_by(active=1).all() 
    return render_template('admin_appts.html', appts=appts, execs=execs)

@admin.route('/meeting/<int:id>')
def manage_appt(id):
    # appt_id = request.args.get('id')
    appt = Appointment.query.filter_by(AptID=id).all()
    return render_template('admin_appt_manage.html', appt=appt[0])

@admin.route('/logout')
def logout():
    """User Logout"""
    session.clear()
    flash("You were logged out!", category='success')
    return redirect(url_for('home.home_page'))