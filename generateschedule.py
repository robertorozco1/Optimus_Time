import Scheduling
import database
import datetime

def generateschedule(database: database.Database):
    weeknum = str(datetime.date.today().isocalendar()[1])
    year = str(datetime.date.today().isocalendar()[0])
    weekid = int(year + weeknum)
    schedule = Scheduling.Schedule(weekid)
    for dayid in schedule.week:
        day = generateday(dayid, database)
        schedule.week[dayid] = day
    return schedule


def generateday(dayid, database: database.Database):
    day = Scheduling.Day()
    database.query("Select Availability.employee_id, Availability.`{}` From Availability".format(str(dayid)))
    availabilities = database.fetchdata()
    for entry in availabilities:
        shift = generateshift(entry)
        day.shifts.append(shift)
    return day

def generateshift(entry):
    times = tuple(entry[1][1:-1].split(","))
    start = int(times[0][:2]) * 60 + int(times[0][2:])
    end = int(times[1][:2]) * 60 + int(times[1][2:])
    shift = Scheduling.Shift(entry[0], start, end)
    return shift
