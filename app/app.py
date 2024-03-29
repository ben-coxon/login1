from flask import Flask, Markup
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os


app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		print ("wrong password")
		flash(Markup('<h2>wrong password!</h2>'))
	return home()

@app.route('/logout')
def logout():
	session['logged_in'] = False
	return home()

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)