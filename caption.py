#from sqlite3 import dbapi2 as sqlite3

from flask import Flask 
from flask import render_template, g, request

import os, urllib, cv2
import numpy as np
from dbhandler import get_db, query_db, tag_query_db
from cogvision import cogv_get_info
#import custvision

#database access code


app = Flask(__name__)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)

  
    ### ROUTES ###
@app.route('/')    
def home {     
    return render_template('index.html', title='Home')      
}
    
@app.route('/gen')
@app.route('/gen', methods=['POST'])
def gen_caption( image_url='https://raw.githubusercontent.com/hailix/caption.me/master/static/athena_owl.png'):

    if request.method == 'POST':
        print ("POSTING")
        image_url = request.form['image_url']
        print (image_url)
    #return json.dumps(request.json)
    cog_caption, tags = cogv_get_info(image_url)
    db_caption = tag_query_db(tags)
    
    tag_string = "#AthenaHacks2018 "
    length = len(tags)
    if length > 5:
        tags = tags[:5]    
    for t in tags:
        tag_string+="#"+t+" "
    
    return render_template('cap_generator.html', title='Home', caption=cog_caption, image_url=image_url, query=db_caption, tags=tag_string)    
    
@app.route('/test')
def test_page_output():
    return 'test page'


@app.teardown_appcontext
def close_connection(exception):
    print("Closing Connection")
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    
