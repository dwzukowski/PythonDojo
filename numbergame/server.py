from flask import Flask, render_template, redirect, session, request
import random
app= Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def main():
    #print "mainpage OK"
    session['randnumber']= random.randint(1,10)
    #print session['randnumber']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def submitguess():
    session['guess']= request.form['guess']
    #print session['guess']
    #print type(session['guess'])
    #print type(session['randnumber'])
    if session['guess'] == str(session['randnumber']):
        #print "correct"
        return render_template('index.html',response="YOU GOT IT!",color="green")
    else:
        return render_template('index.html',response="Guess again...",color="red")
    return redirect('/')

app.run(debug=True)

"""
adding onscreen functionality nvm, I used x="you gained {} gold!".format(session['gold'])
"""
