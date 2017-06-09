from flask import Flask, render_template, redirect, request  
app = Flask(__name__) 
@app.route('/') 
def homepage():
    print "Homepage OK"
    return render_template('index.html',name='Zuk')
@app.route('/ninjas')
def ninjainfo():
    print "Ninjas info OK"
    return render_template('ninjas.html')
@app.route('/dojos/new')
def home():
    return render_template('dojos.html')
app.run(debug=True)

