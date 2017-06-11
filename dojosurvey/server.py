from flask import Flask, render_template, request, redirect, session, flash
app= Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def index():
    print "main page OK"
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def surveyinput():
    print "Got Post info"
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form['info']) > 120:
        flash("Comments are limited to 120 characters")
        return redirect('/')
    if len(request.form['info']) < 1:
        flash("Comments cannot be blank")
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['info'] = request.form['info']

    print session['name']
    print session['location']
    print session['language']
    print session['info']
    return redirect('/results')
@app.route('/results')
def thanks():
    return render_template('results.html')
app.run(debug=True)
