import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
user_logins = client.user_database.user_logins

# route for handling the login page logic
@app.route('/frontpage', methods=['GET', 'POST'])
def login():
    '''Tests to see if username is in database. If not found, returns None'''
    username = request.form.get('username')
    password = request.form.get('password')
    error = None
    print('outside first if statement')
    if request.method == 'POST':
        print('within if statement')
        print(username, password)
        if user_logins.find_one({username: password}) is None:
            print('within is NONE block')
            print('username, password')
            print(username, password)
            print(user_logins.find_one({username: password}))
            print(type(user_logins.find_one({username: password})))
            error = 'Invalid Credentials. Please try again.'
        else:
            print('within else block')
            print(user_logins.find_one({username: password}))
            print(type(user_logins.find_one({username: password})))
            print('Welcome to the site!')
            return redirect(url_for('welcome'))
    return render_template('index.html', error=error)

# @app.route('/welcome')
# def welcome():
#     return render_template('index.html')  # render a template

#adding users
# @app.route('/add_user', methods=['GET', 'POST'])
# def register():
#     '''Tests to see if username is in database. If not found, returns None'''
#     username = request.form.get('username')
#     password = request.form.get('password')
#     error = None
#     print('start of if statement')
#     if request.method == 'POST':
#         print('this is the login cred')
#         if user_logins.find_one({username: password}) is None:
#             user_logins.insert_one({username: password})
#             print('New Login added')
#             # check to ensure new login was added to database
#             if user_logins.find_one({username: password}) is None:
#                 error = 'Database error, try again'
#         elif user_logins.insert_one({username: password}) != None:
#             error = 'Username already exists, try again'
#     return render_template('index.html', error=error)


#start the server with the 'run()' method
if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(port=5000, debug=True, host= '0.0.0.0')
