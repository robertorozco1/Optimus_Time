from flask import Flask, render_template
import database
import generateschedule
import sys
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
    data = schedule.week.tuesday.employeelist()
    print(data, file=sys.stdout)
    
    return render_template('index.html', the_data=[data])


if __name__ == "__main__":
    app.run(debug=True)
