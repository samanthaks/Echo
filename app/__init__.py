""" run using "python app.py" """
from flask import Flask
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

def create_app(
                TESTING=True,
               CSRF_ENABLED=False,
               WTF_CSRF_ENABLED=False):
    """Create app using config variables"""
    app = Flask(__name__)

    app.config["DEBUG"] = False
    # app.config["TESTING"] = TESTING
    app.config['CSRF_ENABLED'] = True
    app.config['WTF_CSRF_ENABLED'] = True 
    app.config['SECRET_KEY'] = 'X{WC3JsG6m7m4o8W3DwrrgJ0[Np,!O'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Setup the database.
    db.init_app(app)

    from app.routes.home_route import home
    from app.routes.exec_route import execs
    from app.routes.student_route import student
    from app.routes.admin_route import admin

    app.register_blueprint(home)
    app.register_blueprint(execs)
    app.register_blueprint(student)
    app.register_blueprint(admin)

    return app
