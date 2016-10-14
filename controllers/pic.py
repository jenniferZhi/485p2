from flask import *
import MySQLdb
import MySQLdb.cursors
from extensions import *
from flask import Flask, session
from flask.ext.session import Session

pic = Blueprint('pic', __name__, template_folder='templates')

@pic.route('/pic', methods = ['GET', 'POST'])
def pic_route():
	
	if request.method != 'POST' and request.method !='GET':
		return abort(404)
	if request.method == 'GET':
		picid = request.args.get('picid', 'default_value')
		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM Photo WHERE picid='%s'" %picid)
		results_search_photo = cur.fetchall()
		flag = 0
		for item in results_search_photo:
			if item['picid'] == picid:
				flag = 1
		if flag == 0:
			return abort(404)

		test_picid = request.args.get('picid', 'default_value')

		db = connect_to_database()
		cur = db.cursor()
		cur.execute("SELECT * FROM Contain WHERE picid='%s'" %test_picid)
		results_search = cur.fetchall()
		caption = results_search[0]['caption']
		cur.execute("SELECT * FROM Photo WHERE picid='%s'" %test_picid)
		results_photo = cur.fetchall()
		format = results_photo[0]['format'] 

		test_albumid = results_search[0]['albumid']

		cur.execute("SELECT * FROM Album WHERE albumid IN (SELECT albumid FROM Contain WHERE picid = '"+test_picid+"')")
		test_album = cur.fetchall()

		flag_1=False
		if 'username' in session:
			username = session['username']
			if(username!=test_album[0]['username'] and test_album[0]['access']== 'private'):
				db = connect_to_database()
				cur = db.cursor()
				cur.execute("SELECT username FROM AlbumAccess WHERE albumid='%s'" %test_albumid)
				results_search_username = cur.fetchall()
				flag_2 = 0
				for item in results_search_username:
					if (item['username'] == username):
						flag_2 = 1
				if flag_2 == 0:
					return abort(403)

			elif(username == test_album[0]['username']):
				flag_1= True

			cur.execute("SELECT * FROM User WHERE username='"+username+"'")
			results_user = cur.fetchall()

		else:
			results_user = None
			if(test_album[0]['access']== 'private'):
				return render_template('login.html')

		cur.execute("SELECT * FROM Contain WHERE albumid='%s'" %test_albumid)
		test_contain_selected = cur.fetchall()

		

		return render_template('pic.html',user = results_user, albumid = test_albumid, picid =test_picid, format = format, Contain = test_contain_selected,caption = caption,flag_1 = flag_1)

	elif request.method == 'POST':
		flag_1=True
		if 'username' in session:
			op = request.form.get('op', 'default_value')
			caption = request.form.get('caption', 'default_value')
			picid = request.form.get('picid', 'default_value')
			if op == 'caption':
				db = connect_to_database()
				cur = db.cursor()
				cur.execute("UPDATE Contain SET caption = '"+caption+"' WHERE picid = '"+picid+"'")
				cur.execute("SELECT * FROM Contain WHERE picid='%s'" %picid)
				results_search = cur.fetchall()
				caption = results_search[0]['caption']
				cur.execute("SELECT * FROM Photo WHERE picid='%s'" %picid)
				results_photo = cur.fetchall()
				format = results_photo[0]['format'] 
				test_albumid = results_search[0]['albumid']
				cur.execute("SELECT * FROM Contain WHERE albumid='%s'" %test_albumid)
				test_contain_selected = cur.fetchall()
			return render_template('pic.html', albumid = test_albumid, picid =picid, format = format, Contain = test_contain_selected,caption = caption,flag_1 = flag_1)


