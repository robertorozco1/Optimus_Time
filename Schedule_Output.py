from flask import Flask, render_template
import pymysql
app = Flask(__name__)

def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='dummydata')
    c = conn.cursor()
    return conn, c

@app.route('/')
def show_tables():
    conn, c = connect()
    query = "SELECT concat(lname, ', ', fname)AS name, sunday, monday, tuesday, wednesday, thursday, friday, saturday FROM user, individual_availability WHERE user.employee_id=individual_availability.employee_id"
    
    c.execute(query)

    data=c.fetchall()
    conn.close()
    
    return render_template('index.html', the_data=data)
    
if __name__ == "__main__":
    app.run(debug = True)
