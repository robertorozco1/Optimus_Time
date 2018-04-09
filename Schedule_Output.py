import pymysql

def main():
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='dummydata')
    c = db.cursor()
    c.execute("SELECT lname, fname, sunday, monday, tuesday, wednesday, thursday, friday, saturday FROM user, individual_availability WHERE user.employee_id=individual_availability.employee_id")
    
    for row in c.fetchall():
        for column
        print (row[i])
main()
