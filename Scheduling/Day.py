from Scheduling.Shift import Shift
from Scheduling.HourMinute import HourMinute


class Day:

    def __init__(self, *shifts):
        self.__shifts = None

        shifts = set(shifts)
        self.shifts = shifts

    def __repr__(self):
        return str(self.shifts)

    def employeelist(self):
        employeeset = set()
        for shift in self.shifts:
            employeeset.add(shift.employeeid)
        return list(employeeset)

    def employeeday(self, employeeid):
        employeeshifts = []
        for shift in self.shifts:
            if shift.employeeid == employeeid:
                employeeshifts.append(shift)
        return Day(self.weekday, *employeeshifts)

    def totaltime(self):
        totaltime = HourMinute()
        for shift in self.shifts:
            totaltime = totaltime + shift.duration()
        return totaltime

    def _set_shifts(self, shifts):
        if type(shifts) is not set:
            raise TypeError("Shifts must be in a set")
        if any(not isinstance(shift, Shift) for shift in shifts):
            raise TypeError("All values must be of type Shift")
        self.__shifts = shifts

    def _get_shifts(self):
        return self.__shifts

    shifts = property(_get_shifts, _set_shifts)


if __name__ == "__main__":
    a = Shift(0, (5, 45), (12, 45))
    b = Shift(0, (17, 0), (23, 59))
    c = Shift(1, (7, 00), (17, 00))
    d = Shift(2, (0, 0), (9, 0))
    e = Shift(2, (6, 0), (23, 59))

    aday = Day(0, a, b, c, d, e)
    print(aday.employeelist())
