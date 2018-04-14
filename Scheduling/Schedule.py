from Scheduling.Week import Week


class Schedule:

    def __init__(self, weekid: int, week=None):
        self.__weeknumber = None
        self.__week = None

        week = Week(week)
        self.weekid = weekid
        self.week = week

    def __repr__(self):
        return str((self.weekid, self.week))

    def employeeweek(self, employeeid):
        employeeweek = Week()
        for item in self.week.items():
            employeeweek.update({item[0]: item[1].employeeday(employeeid)})
        return employeeweek

    def employeelist(self):
        employeelist = []
        for day in self.week.values():
            employeelist.append(day.employeelist())
        return employeelist

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
