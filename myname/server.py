from flask import Flask, render_template, request, redirect
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def processform():
    print "Got Post info"
    name = request.form['name']
    email = request.form['email']
    print name
    print email
    #print type(email)
    return redirect('/')
    #return render_template('index.html') failing to redirect breaks your page by resubmitting the form everytime you try to reload 
app.run(debug=True)
