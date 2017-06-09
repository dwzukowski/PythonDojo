from flask import Flask, render_template, redirect, session, request
import random
app= Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def main():
    print "main OK" 
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processtasks():
    if request.form['action'] == 'farm':
        #do farm process
        print "clicked farm"
        session['bank']+= random.randint(10,20)
    if request.form['action'] == 'cave':
        #do cave process
        print "clicked cave"
        session['bank']+= random.randint(5,10)
    if request.form['action'] == 'house':
        #do house process
        print "clicked house"
        session['bank']+= random.randint(2,5)
    if request.form['action'] == 'casino':
        #do casion process
        print "clicked casino"
        session['bank']+= random.randint(-50,50)
    return redirect('/')

app.run(debug=True)