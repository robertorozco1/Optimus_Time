# all the imports
import os
import sqlite3
import pymysql
import sys
import hashlib
import database
import generateschedule
import Scheduling
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'



app.config.from_envvar('FLASKR_SETTINGS', silent=True)
class ReusableForm(Form):
    email = TextField('Employee :', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password :', validators=[validators.required(), validators.Length(min=3, max=35)])

def get_db():
    g.sqlite_db = database.DebugDatabase()
    return g.sqlite_db

@app.route('/register')
def register():
    return render_template('welcome.html')

@app.route("/", methods=['GET', 'POST'])
def login():
    session['logged_in'] = False
    form = ReusableForm(request.form)
    db = get_db()
    if request.method == 'POST':
        pword=request.form['password']
        uname=request.form['uname']
        db.query("SELECT employee_id, passwd FROM user WHERE employee_id = " + uname)
        data = db.fetchdata()
        if not data:
            flash("Invalid username")
        else:
            data = data[0]
            if str(hashlib.sha256(pword.encode()).hexdigest()) == data[1]:
                # Save the comment here.
                #Query for relevant employee info (first name, last name, role id) for verification
                db.query("SELECT fname, lname, role_id FROM user WHERE employee_id = " + uname )
                session_data = db.fetchdata()[0]
                #assign user info to session variables
                session['logged_in'] = True
                session['uname'] = uname
                session['fname'] = session_data[0]
                session['lname'] = session_data[1]
                session['role_id'] = session_data[2]
                return redirect(url_for("makeasch"))
            else:
                flash("Invalid password")

    return render_template('Welcome.html', form=form)

@app.route('/viewavail')
def viewavail():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
        db = get_db()
        data = db.fetchdata()
        print(data)
        return render_template('availabilityview.html', the_data=data)

@app.route('/admin')
def admin():
    role = session.get('role_id')
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    elif role != 30 or role != 20:
        flash ('Unauthorized Access: Please Contact an Administrator')
        return redirect(url_for('login'))
    else:
        return render_template('admin.html')

@app.route('/rto')
def timeoff():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
        return render_template('timeoff.html')

@app.route('/makeasch')
def makeasch():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
        return render_template('makeasch.html')

@app.route('/makeasch/submit/', methods=['GET','POST'])
def submitsch():
    if request.method == 'POST':
        emp_avail = request.form['starttime_sunday']
        return redirect(url_for('makeasch'))

@app.route('/hoursworked')
def hoursworked():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
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
@app.route ('/logout')
def logout():
    #pop all session variables and redirect to login
    session.pop('logged_in', None)
    session.pop('uname', None)
    session.pop('fname', None)
    session.pop('lname', None)
    session.pop('role_id', None)
    flash('Sucessfuly Logged Out!')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5005, debug=True)
