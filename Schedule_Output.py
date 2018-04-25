from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

def connect():
    db = sqlite3.connect(":memory:")
    script = open("./dummydata.sql").read()
    db.executescript(script)
    return db

@app.route('/')
def show_tables():
    c = connect()
    query = "Select Availability.* From Availability"
    out = c.execute(query)

    data = out.fetchall()
    
    return render_template('index.html', the_data=data)
    
if __name__ == "__main__":
    app.run(debug = True)
