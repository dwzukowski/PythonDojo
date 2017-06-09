from flask import Flask, render_template, request, redirect
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<room>')
def show_user_profile(room):
    #room = room
    return render_template(room+".html",number="another room...")
app.run(debug=True)


'''@app.route('/room1')
def room1():
    return render_template('room1.html',number="the Kitchen")
@app.route('/room2')
def room2():
    return render_template('room2.html',number="the Cellar")
@app.route('/room3')
def room3():
    return render_template('room3.html',number="the Hallway")
@app.route('/room4')
def room4():
    return render_template('room4.html',number="TRAP DOOR!!!")
@app.route('/room5')
def room5():
    return render_template('room5.html',number="small bedroom")
@app.route('/room6')
def room6():
    return render_template('room6.html',number="bathroom")
@app.route('/room7')
def room7():
    return render_template('room7.html',number="a giant pile of leaves!")'''
app.run(debug=True)
