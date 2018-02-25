import os
from sqlite3 import dbapi2 as sqlite3

from flask import Flask 
from flask import render_template
app = Flask(__name__)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)

@app.route('/')
def hello_world():
    user= {'username' : 'Aimee' }
    return render_template('index.html', title='Home', user=user)    
    
@app.route('/test')
def test_page_output():
    conn = sqlite3.connect('CAPTION.db')
    return 'test page'

##### DB SETUP #####

