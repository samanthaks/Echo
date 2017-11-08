"""Admin Route"""
from flask import Blueprint, render_template, session

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

