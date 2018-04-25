# all the imports
import os
import sqlite3
import pymysql
import sys
import hashlib
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


app.config.from_envvar('FLASKR_SETTINGS', silent=True)
class ReusableForm(Form):
    email = TextField('Employee :', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password :', validators=[validators.required(), validators.Length(min=3, max=35)])

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
	
def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='dummydata')
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

@app.route("/", methods=['GET', 'POST'])
def login():
    conn, c = connect()
    form = ReusableForm(request.form)
 
    if request.method == 'POST':
        pword=request.form['password']
        uname=request.form['uname']

        query = "SELECT employee_id, passwd FROM user WHERE employee_id =" + uname + " && passwd='" + str(hashlib.sha256(pword.encode()).hexdigest())+"'"

        data = c.execute(query)
        if data == 1:
            # Save the comment here.
            conn.close()
            flash('Sucess!')
            return redirect(url_for("viewsch"))
        else:
            flash('Username and password does not match ')
 
    return render_template('Welcome.html', form=form)

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

def time_off(employee_id):
    conn, c = connect()
    query = ("SELECT status FROM timeoff WHERE employee_id = " + employee_id)
    c.execute(query)
    status = c.fetchall()
    if status == "NULL":
        return "Pending"
    elif status == "TRUE":
        return "Approved"
    elif status == "FALSE":
        return "Denied"
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5005, debug=True)
