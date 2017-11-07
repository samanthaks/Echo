"""Student Functions"""
from flask import Blueprint, request, redirect, render_template, url_for, \
                    flash, session
from werkzeug.security import generate_password_hash


student = Blueprint('students', __name__, template_folder='../templates')

@student.route('/studentHome')
def student_homepage():
    return render_template('student_home.html')

@student.route('/studentProfile')
def student_profile():
    return render_template('student_profile.html')
