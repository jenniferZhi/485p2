from flask import *
import MySQLdb
import MySQLdb.cursors
from extensions import *
import os
from flask import Flask, session
from flask.ext.session import Session

albums = Blueprint('albums', __name__, template_folder='templates')

@albums.route('/albums/edit', methods=['GET', 'POST'])
def albums_edit_route():
	options = {
		"edit": True
	}
	if 'username' in session:
		
		username = session['username']
		
		if request.method != 'POST' and request.method !='GET':
			return abort(404)
		
		'''
		url_username = request.args.get('username', 'default_value')
		if(url_username != username):
			return abort(404)
		'''
		db = connect_to_database()
		cur = db.cursor()
			
		
		#username = session['username']

		if request.method == 'POST':
			op = request.form['op']
			if op == 'add':
				title = request.form['title']
				username = request.form['username']
				#createalbum = request.form['createalbum']
				cur.execute("INSERT INTO Album (title, username) Values ('%s', '%s')" %(title, username))
			elif op == 'delete':
				albumid = request.form['albumid']
				cur.execute("SELECT picid FROM Contain WHERE albumid = '%s'" %albumid)
				results_search = cur.fetchall()
				for item in results_search:
					cur.execute("DELETE FROM Photo WHERE picid = '%s'" %item['picid'])
					filename = item['picid']
					filename = filename + '.jpg'
					targetFile = os.path.join('./static/images/', filename)
					os.remove(targetFile)

				cur.execute("DELETE FROM Album WHERE albumid = '%s'" %albumid)
		
		cur.execute("SELECT * FROM Album WHERE username = '%s'" %username)

		results_albums = cur.fetchall()
		cur.execute("SELECT * FROM User WHERE username='"+username+"'")
		results_user = cur.fetchall()
		
		return render_template("albums.html",user = results_user, Albums = results_albums, username = username, **options)
	else:
		return render_template('login.html')


@albums.route('/albums', methods=['GET', 'POST'])
def albums_route():
	options = {
		"edit": False
	}

	if 'username' in session:

		username = session['username']
		
				
		db = connect_to_database()
		cur = db.cursor()
			
		cur.execute("SELECT * FROM Album WHERE username = '"+username+"'")
		results_albums = cur.fetchall()
		cur.execute("SELECT * FROM Album WHERE albumid in (SELECT albumid FROM AlbumAccess WHERE username = '"+username+"')")
		other_albums = cur.fetchall()
		cur.execute("SELECT * FROM User WHERE username = '"+username+"'")
		results_user = cur.fetchall()

		return render_template('albums.html',user = results_user, username = username, Albums = results_albums, other_albums = other_albums, **options)

	else:
		if request.method != 'POST' and request.method !='GET':
			return abort(404)
		username = request.args.get('username', 'default_value')

		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM User WHERE username='%s'" %username)
		results_search_user = cur.fetchall()
		flag = 0
		for item in results_search_user:
			if item['username'] == username:
				flag = 1
		if flag == 0:
			return abort(404)


		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM Album WHERE access = 'public' AND username = '"+username+"'")
		results_albums = cur.fetchall()
		return render_template('albums_public.html', Albums = results_albums, username = username, **options)


