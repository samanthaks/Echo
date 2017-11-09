"""Admin Route"""
from flask import Blueprint, render_template, session, request, flash, redirect, url_for, jsonify
from ..models.verification_mock_login import VerificationMockForm
from ..CBSLogin.CBSLogin import CBSLogin
admin = Blueprint('admin', __name__, template_folder='../templates')


@admin.route('/adminHome')
def admin_homepage():
    """The home page."""
    # if 'Username' in session:
    #     return render_template('user_index.html')
    return render_template('admin_home.html')

@admin.route('/manageCalendars')
def manage_calendars():
    """The home page."""
    # if 'Username' in session:
    #     return render_template('user_index.html')
    return render_template('admin_calendars.html')

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
		
	