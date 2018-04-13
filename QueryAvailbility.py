import sqlite3
import Scheduling

DAYS = {0: 'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday'}

db = sqlite3.connect(":memory:")
script = open("./dummydata.sql").read()
db.executescript(script)

aweek = Scheduling.ScheduleWeek(0)

for item in DAYS.items():
    query = "Select Availability.employee_id, Availability.{0} From Availability Where employee_id=3".format(item[1])
    out = db.execute(query)
    shifts = out.fetchall()
    aday = Scheduling.Day(item[0])
    for shift in shifts:
        id = shift[0]
        times = shift[1].split('-')
        ashift = Scheduling.Shift(id, (int(times[0]), 0), (int(times[1]), 0))
        aday.shifts.add(ashift)
    aweek.week[item[0]] = aday

for day in aweek.week.values():
    print(day)

