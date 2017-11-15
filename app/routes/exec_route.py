"""Exec Routes"""
from flask import Blueprint, render_template, redirect, url_for, request,\
                  session, flash, abort
from app.models.models import ExecForm


execs = Blueprint('execs', __name__, template_folder='../templates')

