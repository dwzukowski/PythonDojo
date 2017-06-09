from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')
@app.route('/about')
def about_me():
    return render_template('about.html')
@app.route('/projects')
def my_projectes():
    return render_template('projects.html')
app.run(debug=True)
