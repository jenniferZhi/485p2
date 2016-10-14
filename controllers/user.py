from flask import *
import MySQLdb
import MySQLdb.cursors
from extensions import *
from flask import Flask, session
from flask.ext.session import Session
import hashlib
import uuid
import re

user = Blueprint('user', __name__, template_folder='templates')

def passwordCreated(password):
	algorithm = 'sha512'
	salt = uuid.uuid4().hex

	m = hashlib.new(algorithm)

	m.update(salt + password)
	password_hash = m.hexdigest()
	return "$".join([algorithm, salt, password_hash])

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/user', methods = ['GET', 'POST'])
def user_route():
	if "username" in session:
		
		username = session['username']

		db =connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM User WHERE username = '"+username+"' ")
		result_user = cur.fetchall()

		return render_template("userEdit.html", user = result_user)
	else:
		if (request.method == 'GET'):
			return render_template("user.html")   
		elif (request.method == 'POST'):
			username = request.form.get('username', 'default_value')
			firstname = request.form.get('firstname', 'default_value')
			lastname = request.form.get('lastname', 'default_value')
			password1 = request.form.get('password1', 'default_value')
			password2 = request.form.get('password2', 'default_value')
			email = request.form.get('email', 'default_value')
			
			
			errors = {
				"error" : False,
				"usernameBlank" : False,
				"usernameMaxLength" : False,
				"usernameMinLength" : False,
				"usernameUnique" : False,
				"usernamePattern" : False,
				"firstnameBlank" : False,
				"firstnameMaxLength" : False,
				"lastnameBlank" : False,
				"lastnameMaxLength" : False,
				"password1Blank" : False,
				"password1MinLength" : False,
				"password1Pattern1" : False,
				"password1Pattern2" : False,
				"passwordMatch" : False,
				"emailBlank" : False,
				"emailValid" : False,
				"emailMaxLength": False,	
			}

			if username == "":
				errors['error'] = True
				errors['usernameBlank'] = True
			if len(username) > 20:
				errors['error'] = True
				errors['usernameMaxLength'] = True
				
			if len(username) < 3:
				errors['error'] = True
				errors['usernameMinLength'] = True
			
			db = connect_to_database()
			cur = db.cursor()
			cur.execute("SELECT * FROM User WHERE username = '"+username+"'")
			result_search = cur.fetchall()
			if result_search != ():
				errors['error'] = True
				errors['usernameUnique'] = True

			if not re.match("^[a-zA-Z0-9_]+$", username):
				errors['error'] = True
				errors['usernamePattern'] = True
			if firstname == "":
				errors['error'] = True
				errors['firstnameBlank'] = True
			if len(firstname) > 20:
				errors['error'] = True
				errors['firstnameMaxLength'] = True
			if lastname == "":
				errors['error'] = True
				errors['lastnameBlank'] = True
			if len(lastname) > 20:
				errors['error'] = True
				errors['lastnameMaxLength'] = True
			if password1 == "":
				errors['error'] = True
				errors['password1Blank'] = True
			if len(password1) < 8:
				errors['error'] = True
				errors['password1MinLength'] = True

			if not re.match('^[0-9a-zA-Z_]*$', password1):
				errors['error'] = True
				errors['password1Pattern1'] = True

			if re.match('^[0-9]*$', password1) or re.match('^[a-zA-Z]*$', password1):
				errors['error'] = True
				errors['password1Pattern2'] = True
			
			if password1 != password2:
				errors['error'] = True
				errors['passwordMatch'] = True
			if email == "":
				errors['error'] = True
				errors['emailBlank'] = True
			if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
				errors['error'] = True
				errors['emailValid'] = "don't fill requirement"
			if len(email) > 40:
				errors['error'] = True
				errors['emailMaxLength'] = True

			if errors['error']:
				return render_template('user.html', **errors)
			
			else:

				db = connect_to_database()
				cur = db.cursor()
				password = passwordCreated(password1)
				cur.execute("INSERT INTO User VALUES ('"+username+"', '"+firstname+"', '"+lastname+"', '"+password+"', '"+email+"')")

				return render_template('login.html')
		
@user.route('/user/edit', methods = ['GET', 'POST'])
def user_edit_route():
	if 'username' in session:
		username = session['username']

		if (request.method == 'GET'):
			'''
			if request.method != 'POST' and request.method !='GET':
				return abort(404)
			url_username = request.args.get('username', 'default_value')
			print url_username
			db = connect_to_database()
			cur = db.cursor()
			cur.execute("SELECT * FROM User WHERE username='%s'" %url_username)
			results_search_user = cur.fetchall()
			flag = 0
			for item in results_search_user:
				if (item['username'] == url_username) and (url_username == username):
					flag = 1
			if flag == 0:
				return abort(404)
			'''
			db =connect_to_database()
			cur = db.cursor()
			cur.execute("SELECT * FROM User WHERE username = '"+username+"' ")
			result_user = cur.fetchall()

			#print result_user
			return render_template("userEdit.html",user = result_user)


		if (request.method == 'POST'):
			#username = request.form.get('username', 'default_value')
			firstname = request.form.get('firstname', 'default_value')
			lastname = request.form.get('lastname', 'default_value')
			email = request.form.get('email', 'default_value')
			password1 = request.form.get('password1', 'default_value')
			password2 = request.form.get('password2', 'default_value')


			
			db =connect_to_database()
			cur = db.cursor()
			cur.execute("SELECT * FROM User WHERE username = '"+username+"' ")
			result_user = cur.fetchall()


			errors = {
				"error" : False,
				"firstnameMaxLength" : False,
				"lastnameMaxLength" : False,
				"passwordMaxLength" : False,
				"password1Pattern1" : False,
				"password1Pattern2" : False,
				"passwordMatch" : False,
				"emailValid" : False,
				"emailMaxLength": False,	
			}
			if (firstname != 'default_value'):

				if len(firstname) > 20:
					errors['error'] = True
					errors['firstnameMaxLength'] = True
					
				if errors['error']:
					return render_template('userEdit.html', user = result_user, **errors)
				else:
					db = connect_to_database()
					cur = db.cursor()
					cur.execute("UPDATE User SET firstname = '"+firstname+"' WHERE username = '"+username+"'")
					return redirect(request.url)
					#return redirect(url_for('main.main_route', username = username))

			if (lastname != 'default_value'):

				if len(lastname) > 20:
					errors['error'] = True
					errors['lastnameMaxLength'] = True

				if errors['error']:
					return render_template('userEdit.html', user = result_user, **errors)
				else:
					db = connect_to_database()
					cur = db.cursor()
					cur.execute("UPDATE User SET lastname = '"+lastname+"' WHERE username = '"+username+"'")
					return redirect(request.url)
					#return redirect(url_for('main.main_route', username = username))

			if (password1 != 'default_value'):

				#print password_1
				#print password_2
				#print "orange"
				#print len(password_1)
			
				if len(password1) < 8:
					errors['error'] = True
					errors['passwordMinLength'] = True

				if not re.match('^[0-9a-zA-Z_]+$', password1):
					errors['error'] = True
					errors['password1Pattern1'] = True
				'''
				print (re.findall('[0-9]+', password_1) != [])
				print (re.findall('[a-zA-Z]+', password_1) != [])
				print re.findall('[0-9]+', password_1)
				print re.findall('[a-zA-Z]+', password_1)
				
				if re.findall('[0-9]+', password_1) == [] or re.findall('[a-zA-Z]+', password_1) == []:
					print re.findall('[0-9]+', password_1)
					print re.findall('[a-zA-Z]+', password_1)
					errors['error'] = True
					errors['password1Pattern2'] = True
				'''
				if re.match('^[0-9]*$', password1) or re.match('^[a-zA-Z]*$', password1):
					errors['error'] = True
					errors['password1Pattern2'] = True
				
				if password1 != password2:
					errors['error'] = True
					errors['passwordMatch'] = True

				if errors['error']:
					return render_template('userEdit.html', user = result_user, **errors)
				else:

					password1 = passwordCreated(password1)
					#print password1
					db = connect_to_database()
					cur = db.cursor()
					cur.execute("UPDATE User SET password = '"+password1+"' WHERE username = '"+username+"'")
					return redirect(request.url)
					#return redirect(url_for('main.main_route', username = username))

			if (email != 'default_value:'):

				if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
					errors['error'] = True
					errors['emailValid'] = True

				if len(email) > 40:
					errors['error'] = True
					errors['emailMaxLength'] = True

				if errors['error']:
					return render_template('userEdit.html', user = result_user, **errors)
				else:
					db = connect_to_database()
					cur = db.cursor()
					cur.execute("UPDATE User SET email = '"+email+"' WHERE username = '"+username+"'")
					return redirect(request.url)
					#return redirect(url_for('main.main_route', username = username))

	else:
		return abort(404)

		
