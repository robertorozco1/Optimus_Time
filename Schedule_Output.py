from flask import Flask, render_template
import database
app = Flask(__name__)


@app.route('/')
def show_tables():
    db = database.DebugDatabase()
    db.query("Select Availability.* From Availability")
    data = db.fetchdata()
    
    return render_template('index.html', the_data=data)


if __name__ == "__main__":
    app.run(debug=True)
