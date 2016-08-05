from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
user_logins = client.user_database.user_logins

# # route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    error = None
    print('__TEST_____')
    if request.method == 'POST':
        # if username != 'test' or password != 'test':
        #     error = 'Invalid Credentials. Please try again.'
        # else:
            print(username, password)
            print(type(username), type(password))

            print(user_logins.insert_one({username: password}))
            print(user_logins.find_one({username: password}))
            print(user_logins.find_one({}))
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(port=5000, debug=True, host= '0.0.0.0')
