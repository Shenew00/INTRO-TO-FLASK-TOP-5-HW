from app import app
from flask import render_template

@app.route('/')
def Home():
    return render_template('index.html')
        
@app.route('/MyTop5')
def Top5():
    Fave = ['Caribbean', 'Japanese', 'Mexican', 'Korean', 'Mediterranean']
    return render_template('Base.html', Fave_food = Fave)

@app.route('/MyFaves')
def MyFaves():
    Fave = ['Caribbean', 'Japanese', 'Mexican', 'Korean', 'Mediterranean']
    return render_template('myfaves.html', Fave_food = Fave)
        
        