from flask import Flask, render_template, request, redirect
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post info"
    name = request.form['name']
    email = request.form['email']
    #print name
    #print email
    #print type(email)
    return redirect('/projects')
    #return render_template('index.html') failing to redirect breaks your page by resubmitting the form everytime you try to reload 
@app.route('/projects')
def thanks():
    return render_template('projects.html')
app.run(debug=True)
