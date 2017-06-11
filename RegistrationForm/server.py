from flask import Flask, render_template, request, redirect, session, flash
import re
app= Flask(__name__)
app.secret_key= "ThisIsSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    print "main page OK"
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def surveyinput():
    print "Got Post info"
    if len(request.form['fname']) < 1 or len(request.form['lname']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1:
        print "Field missing data"
        flash("All fields are mandatory")
        return redirect('/')
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        return redirect('/')
    if request.form['password'] != request.form['confirmpass']:
        flash("Confirm password did not match password")
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
        return redirect('/')   
    if not request.form['fname'].isalpha() or not request.form['lname'].isalpha():
        flash("First and Last name fields can only contain letters")
        return redirect('/')   
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirmpass'] = request.form['confirmpass']
    print session['fname']
    print session['lname']
    print session['email']
    print session['password']
    print session['confirmpass']
    return redirect('/')
app.run(debug=True)
