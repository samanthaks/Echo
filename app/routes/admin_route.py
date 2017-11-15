"""Admin Route"""
from flask import Blueprint, render_template, session, request, flash, session, redirect, url_for, jsonify
from app.models.models import Appointment, AptForm, Executive, ExecForm, Admin, AdminForm
from app import db
from app.models.verification_mock_login import VerificationMockForm
from app.CBSLogin.CBSLogin import CBSLogin

admin = Blueprint('admin', __name__, template_folder='../templates')


@admin.route('/adminHome')
def admin_homepage():
    return render_template('admin_home.html')

@admin.route('/adminLogin', methods=['GET', 'POST'])
def admin_login():
    form = AdminForm(request.form)
    if request.method == 'POST':
        admins = Admin.query.order_by(Admin.name).filter_by(active=1).all()

    else:
        return render_template('admin_login.html', form=form)

@admin.route('/manageCalendars')
def manage_calendars():
    """The home page."""
    # if 'Username' in session:
    #     return render_template('user_index.html')
    return render_template('admin_calendars.html')

@admin.route('/createMeeting', methods=['GET', 'POST'])
def create_meeting():
    form = AptForm(request.form)
    if request.method == 'GET':
        execs = Executive.query.order_by(Executive.name).filter_by(active=0).all()
        return render_template('create_meeting.html', form=form, execs=execs)
    return render_template('create_meeting.html')

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
		session['username'] = form.username.data
		session['password'] = form.password.data
		return redirect(url_for('admin.verification_mock'))

@admin.route('/verificationMock', methods=['GET','POST'])
def verification_mock():
	form = VerificationMockForm(request.form)
	if request.method == 'GET':
		return render_template('verification_mock.html', form=form)
	elif request.method == 'POST' and form.validate():
		username = session['username']
		password = session['password']
		login = CBSLogin(username,password)
		name, program, entry_term, cluster, email = login.getInfo(form.username.data)
		# name, program, entry_term, cluster, email = 1,2,3,4,5
		data = {'lifetimeID': form.username.data, 'name': name, 'program': program, 'entry_term': entry_term, 'cluster': cluster, 'email': email}
		return render_template('verification_mock.html', form=form, data=data)
		
	
