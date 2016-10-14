from flask import *
import MySQLdb
import MySQLdb.cursors
from extensions import *
import hashlib
import uuid
from flask import Flask, session
from flask.ext.session import Session

def passwordCreated(password):
	algorithm = 'sha512'
	salt = uuid.uuid4().hex
	print salt

	m = hashlib.new(algorithm)
	m.update(salt + password)
	password_hash = m.hexdigest()

	return "$".join([algorithm, salt, password_hash])

login = Blueprint('login', __name__, template_folder='templates')

def passwordCheck(salt, password):
	algorithm = 'sha512'
	m = hashlib.new(algorithm)
	m.update(salt + password)
	password_hash = m.hexdigest()

	return "$".join([algorithm, salt, password_hash])

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods = ['GET', 'POST'])
def login_route():
	if (request.method == 'GET'):
		return render_template("login.html")   
	elif (request.method == 'POST'):
		username = request.form.get('username', 'default_value')
		password = request.form.get('password', 'default_value')

		errors = {
			"error" : False,
			"usernameBlank" : False,
			"passwordBlank" : False,
			"usernameDoesNotExist" : False,
			"passwordIncorrect" : False
		}

		if username == "":
			errors['error'] = True
			errors['usernameBlank'] = True
		if password == "":
			errors['error'] = True
			errors['passwordBlank'] = True

		if username != "":
			db = connect_to_database()
			cur = db.cursor()
			cur.execute("SELECT password FROM User WHERE username='"+username+"'")
			results_password = cur.fetchall()
			if results_password == ():
				errors['error'] = True
				errors['usernameDoesNotExist'] = True
			else:
				salt = results_password[0]['password'].rsplit('$', 2)[1]
				password = passwordCheck(salt, password)

				if password != results_password[0]['password']:
					errors['error'] = True
					errors['passwordIncorrect'] = True
				else:
					session['username'] = username
		if errors['error']:
			return render_template('login.html', **errors)
		else:			
			return redirect(url_for('main.main_route', username = username))

