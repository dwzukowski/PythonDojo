#import Flask to allow us to create an app; render_template allows us to render html documents
from flask import Flask, render_template  
app = Flask(__name__) 

@app.route('/') 
def hello_world():
    return render_template('index.html',name='Zuk')
@app.route('/success')
def success():
    return render_template('success.html')
@app.route('/home')
def home():
    return render_template('home.html')
app.run(debug=True)


#global variable name tells Flask whether or not we are running the file directly or importing it as a module
# the @ symbol is a decorator which attaches the following function the '/' route.  This means that when we send a request to localhost:5000/ we will run "hello_world"run the app in debug mode 