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
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import etc

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
        data = db.login(uname)
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
#View all current employee availability based on Availability table
def viewavail():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
        db = get_db()
        db.query("SELECT lname, fname, `0`, `1`, `2`, `3`, `4`, `5`, `6` FROM user, availability WHERE user.employee_id=availability.employee_id")
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

@app.route('/rto/submit', methods=['GET','POST'])
def submitTimeOff():
    db = get_db()
    if request.method == 'POST':
        print (session.get('uname'))
        db.query('INSERT into TimeOff (`employee_id`.`start_date`,`end_date`,`Reason`,`Status`) VALUES (?,?,?,?,NULL)',
        [int(session.get('uname')),
        request.form['start_date'],
        request.form['end_date'],
        request.form['reason']])
    return redirect(url_for('/rto'))

@app.route('/viewworkschedule', methods=['GET','POST'])
def viewschedule():
    db = get_db()
    if request.method == 'POST':
        #weekid = int(request.form['weekid'])
        schedule = db.getschedule(request.form['weekid`'])
        for employee in schedule.employeelist():
            aweek = schedule.week.employeeweek(employee)
            data.append(aweek.values())
        employeelist = schedule.employeelist()
        return render_template('workscheduleview.html', employee_list=employeelist, the_data=data)
    return render_template('selectschedule.html')

@app.route('/newworkschedule', methods=['GET','POST'])
def genschedule():
    db = get_db()
    data = []
    schedule = generateschedule.generateschedule(db)

    for employee in schedule.employeelist():
        aweek = schedule.week.employeeweek(employee)
        data.append(aweek.values())
    employeelist = schedule.employeelist()

    if request.method == 'POST':
            db.insertschedule(schedule)
            return redirect(url_for('viewschedule'))

    return render_template('generateschedule.html', employee_list=employeelist, the_data=data)

@app.route('/makeasch')
def makeasch():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
        return render_template('makeasch.html')

@app.route('/makeasch/submit/', methods=['GET','POST'])
def submitsch():
    db = get_db()
    if request.method == 'POST':
        print (type(session.get('uname')))

        #check to see if the employee already has an availability Schedule
        db.query("SELECT * FROM Availability WHERE employee_id=?",[int(session.get('uname'))])

        if len(db.fetchdata()) < 0:
            db.query("INSERT into Availability (`employee_id`,`0`,`1`,`2`,`3`,`4`,`5`,`6`) VALUES (?,?,?,?,?,?,?,?)",
            [int(session.get('uname')),
            str((request.form['starttime_sunday'],request.form['endtime_sunday'])),
            str((request.form['starttime_monday'],request.form['endtime_monday'])),
            str((request.form['starttime_tuesday'],request.form['endtime_tuesday'])),
            str((request.form['starttime_wednesday'],request.form['endtime_wednesday'])),
            str((request.form['starttime_thursday'],request.form['endtime_thursday'])),
            str((request.form['starttime_friday'],request.form['endtime_friday'])),
            str((request.form['starttime_saturday'],request.form['endtime_saturday']))])
            print("insert")
            flash('Schedule Updated')
        else:
            db.query("UPDATE Availability SET `0` = ?, `1` = ?, `2` = ?, `3` = ?, `4` = ?, `5` = ?, `6` = ? WHERE employee_id = ?",
            [str((request.form['starttime_sunday'],request.form['endtime_sunday'])),
            str((request.form['starttime_monday'],request.form['endtime_monday'])),
            str((request.form['starttime_tuesday'],request.form['endtime_tuesday'])),
            str((request.form['starttime_wednesday'],request.form['endtime_wednesday'])),
            str((request.form['starttime_thursday'],request.form['endtime_thursday'])),
            str((request.form['starttime_friday'],request.form['endtime_friday'])),
            str((request.form['starttime_saturday'],request.form['endtime_saturday'])),
            int(session.get('uname'))])
            print("update")
            flash('Schedule Updated')

        return redirect(url_for('makeasch'))

@app.route('/hoursworked')
def hoursworked():
    if not session.get('logged_in'):
        flash('Please Log in')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            ...
        else:
            return render_template('hoursworked.html',
                                   weeknum=etc.weeknum(),
                                   schedule=get_db().getschedule(session.get("uname")))


@app.route('/logout')
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
