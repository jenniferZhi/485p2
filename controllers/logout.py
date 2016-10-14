from flask import *
import MySQLdb
import MySQLdb.cursors
from extensions import *
import os
from flask import Flask, session
from flask.ext.session import Session


logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/logout', methods = ['GET', 'POST'])
def logout_route():
	session.pop('username', None)
	return redirect(url_for('main.main_route'))