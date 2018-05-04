from flask import Flask, render_template
import database
import generateschedule
import sys
import Scheduling
import pickle
app = Flask(__name__)

db = None

@app.before_first_request
def initializedb():
    global db
    db = database.DebugDatabase()


@app.route('/')
def show_tables():
    global db
    schedule = generateschedule.generateschedule(db)
    a = pickle.dumps(schedule)
    b = pickle.loads(a)
    data = []
    for employee in b.employeelist():
        aweek = b.week.employeeweek(employee)
        data.append(aweek.values())
    
    return render_template('index.html', the_data=data)


if __name__ == "__main__":
    app.run(debug=True)
