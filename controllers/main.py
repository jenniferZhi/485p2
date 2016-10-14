from flask import *
import MySQLdb
import MySQLdb.cursors
from extensions import *
from flask import Flask, session
from flask.ext.session import Session


main = Blueprint('main', __name__, template_folder='templates')



@main.route('/')
def main_route():

	if 'username' in session:
		username = session['username']

		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM User WHERE username ='"+username+"'")
		results_user = cur.fetchall()

		cur.execute("SELECT * FROM Album WHERE username = '"+username+"'")
		results_albums = cur.fetchall()


		cur.execute("SELECT * FROM Album WHERE access = 'public'")
		results_albums_public = cur.fetchall()

		cur.execute("SELECT * FROM Album WHERE albumid in (SELECT albumid FROM AlbumAccess WHERE username = '"+username+"')")
		results_albums_other = cur.fetchall()

		

		return render_template("logedin_home.html", user = results_user, Albums = results_albums, other_albums = results_albums_other, AlbumPublic = results_albums_public)

		'''
		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM User WHERE username ='"+username+"'")
		results_user = cur.fetchall()

		return render_template("logedin_home.html", user = results_user)
		'''
	else:
		#username = request.args.get('username', 'default_value')
		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT username FROM User")
		results_username = cur.fetchall()
		cur.execute("SELECT * FROM Album WHERE access = 'public'")
		results_album = cur.fetchall()
    
		return render_template("home.html", user = results_username, album = results_album)

