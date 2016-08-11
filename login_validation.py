import os
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
user_logins = client.user_database.user_logins


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

# route for handling the login page logic
@app.route('/frontpage', methods=['GET', 'POST'])
def login():
    '''Tests to see if username is in database. If not found, returns None'''
    username = request.form.get('username')
    password = request.form.get('password')
    error = None
    print('running login')
    if username != None and request.method == 'POST':
        #User exists, checking dict
        print('Text was entered into username')
        user_dict = user_logins.find_one({'Username': username})
        stored_hash = user_dict['Password']
        print(stored_hash)
        user = User(username, password)
        print(user_dict)
        if user_dict is None:
            #return user object to conserve information
            print('within is NONE block, user does not exist')
            error = 'User does not exist. Please Register Below'
            return render_template('index.html', error=error)
        else:
            # Check if password is right
            print('user exists, checking password')
            if check_password_hash(stored_hash, password):
                print('Password correct. Welcome to the site!')
                return redirect(url_for('welcome'))
            else:
                print('incorrect password')
                error = 'Password incorrect'
                return render_template('index.html', error=error)
    if username is None and request.method == 'POST':
        print('redirect to register')
        register()
    return render_template('index.html', error=error)

@app.route('/welcome')
def welcome():
     return render_template('index.html')  # render a template

# adding users
@app.route('/frontpage', methods=['GET', 'POST'])
def register():
    '''Tests to see if username is in database. If not found, returns None'''
    error = None
    print('running register')
    if request.method == 'POST':
        print('register: within if statement')
        username = request.form.get('register_username')
        password = request.form.get('register_password')
        user_inst = User(username, password)
        print('before test_user')
        test_user = user_logins.find_one({'Username': username})
        print('after test user')
        print('credentials:')
        print(username, password)
        print(test_user)
        if test_user is None:
            #return user object to conserve information
            print('within is NONE block, user does not exist')
            print('username, password')
            print(username, password)
            user_logins.insert({
                'Username': username,
                'Password': user_inst.pw_hash
            })
            print('above hash')
            print(user_inst.username)
            print(user_inst.pw_hash)
            print('below hash')
            user_logins.insert_one({'Username': username})
            error = 'User Added'
            print(user_logins.find_one({'Username': username}))
            print('user added to database')
        else:
            print('within else block')
            print('User exists!')
            error = 'Error: User exists'
    return render_template('index.html', error=error)

#start the server with the 'run()' method
if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(port=5000, debug=True, host= '0.0.0.0')
