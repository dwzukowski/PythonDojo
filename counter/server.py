from flask import Flask, render_template, redirect, session, request
app= Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def counter():
    print "counter OK"

    try: 
        session['count']+=1
    except: 
        session['count']= 1 
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def bonusvisits():
    print "Got Post info"
    session['count']+=1
    print session['count']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetvisits():
    print "Got reset info"
    session['count']= -1
    print session['count']
    return redirect('/')
app.run(debug=True)

"""
Instructor solution:

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/add2', methods=['POST'])
def increment():
    print 'hello again'
    session['counter'] += 1
    return redirect('/')

@app.route('/reset_count', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)

"""