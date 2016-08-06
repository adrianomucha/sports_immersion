from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from add_user import *
from login_validation import *

app = Flask(__name__)
client = MongoClient()
user_logins = client.user_database.user_logins

@app.route('/add_user', methods=['GET', 'POST'])
def master_add_user():
    error = None
    register()
    return render_template('register_user.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def master_login():
    error = None
    login()
    return render_template('login.html', error=error)

@app.route('/welcome', methods=['GET', 'POST'])
def master_welcome():
     return render_template('welcome.html')  # render a template


if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(port=5000, debug=True, host= '0.0.0.0')
