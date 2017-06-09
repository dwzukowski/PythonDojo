from flask import Flask, render_template, redirect, request
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/users')
def users():
    return render_template('users.html')
@app.route('/users/<username>/<id>') #defining varibles in route
def show_user_profile(username, id):
    print username #print arguments provided by user
    print id
    return render_template("users.html")
app.run(debug=True)