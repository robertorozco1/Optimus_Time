from Scheduling.Week import Week
from Scheduling.HourMinute import HourMinute


class Schedule:

    def __init__(self, weekid: int, week=None):
        self.__weeknumber = None
        self.__week = None

        week = Week(week)
        self.weekid = weekid
        self.week = week

    def __repr__(self):
        return str((self.weekid, self.week))

    def employeeschedule(self, employeeid):
        return Schedule(self.weekid, self.week.employeeweek(employeeid))

    def employeelist(self):
        employeelist = []
        for day in self.week.values():
            employeelist.append(day.employeelist())
        return employeelist

    def totaltime(self):
        time = HourMinute()
        for day in self.week.values():
            time += day.totaltime()
        return time

    def _set_weekid(self, weekid: int):
        if type(weekid) is not int:
            raise TypeError("weekid must be of type int")
        self.__weekid = weekid

    def _get_weekid(self):
        return self.__weekid

    def _set_week(self, week: Week):
        if type(week) is not Week:
            raise TypeError("week must be of type Week")
        self.__week = week

    def _get_week(self):
        return self.__week
