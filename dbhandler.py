from sqlite3 import dbapi2 as sqlite3
from flask import g

DATABASE = 'CAPTION.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

#
def tag_query_db(all_tags):
    tags = all_tags
    length = len(tags)
    if length > 5:
        tags = tags[:5]
    cur = get_db();
    for t in tags:
        query_sub = "select caption from captions where subcategory='" + t +"'"
        query_cat = "select caption from captions where category='" + t +"'" 
        print ("QUERY STRING:" + query_sub)
        result = cur.execute(query_sub)
        rv = result.fetchall()
        if (len(rv)) != 0:
            return rv[0][0]
        print ("QUERY STRING:" + query_cat)
        result = cur.execute(query_cat)
        rv = result.fetchall() 
        if (len(rv)) != 0:
            return rv[0][0]
    return "send help, i'm tired"