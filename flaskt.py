# all the imports
import os
import sqlite3
import pymysql
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
	
def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='dummydata')
    c = conn.cursor()
    return conn, c
	

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqllite_db_db = connect_db()
    return g.sqllite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqllite_db.close()

#initizle db       
def init_db():
    db = get_db()
    with app.open_resource('dummydata.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')
 
 
@app.route('/register')
def register():	
    return render_template('welcome.html')

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/viewsch')
def viewsch():
	conn, c = connect()
	query = "SELECT concat(lname, ', ', fname)AS name, sunday, monday, tuesday, wednesday, thursday, friday, saturday FROM user, individual_availability WHERE user.employee_id=individual_availability.employee_id"

	c.execute(query)

	data=c.fetchall()
	conn.close()
	return render_template('scheduleoutput.html', the_data=data)
@app.route('/admin')	
def admin():
	return render_template('admin.html')

@app.route('/rto')
def timeoff():
    return render_template('timeoff.html')

@app.route('/makesch')
def makeasch():
	return render_template('makeasch.html')

@app.route('/hoursworked')
def hoursworked():
    return render_template('hoursworked.html')


if __name__ == "__main__":
    app.run(debug=True)