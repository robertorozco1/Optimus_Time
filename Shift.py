from HourMinute import HourMinute


class Shift:

    def __init__(self, employeeid: int, start, end):

        self.__employeeid = None
        self.__start = None
        self.__end = None

        self.employeeid = employeeid
        start = self.__validateshift__(start)
        end = self.__validateshift__(end)
        if start > end:
            raise ValueError("Shift start time must be less than shift end time")
        self.start = start
        self.end = end

    def __repr__(self):
        return str((self.employeeid, (self.start, self.end)))

    @staticmethod
    def __validateshift__(shift):
        if shift is not HourMinute:
            if len(shift) != 2:
                raise TypeError("End must be of type HourMinute or length of 2")
            shift = HourMinute(shift[0], shift[1])
        if shift.hour > 24:
            raise ValueError("A day cannot have more than 24 hours")
        return shift

    def _get_duration(self) -> HourMinute:
        return self.end - self.start

    def _set_employeeid(self, employeeid: int):
        self.__employeeid = employeeid

    def _get_employeeid(self):
        return self.__employeeid

    def _set_start(self, start: HourMinute):
        self.__start = start

    def _get_start(self):
        return self.__start

    def _set_end(self, end: HourMinute):
        self.__end = end

    def _get_end(self):
        return self.__end

    employeeid = property(_get_employeeid, _set_employeeid)
    start = property(_get_start, _set_start)
    end = property(_get_end, _set_end)
    duration = property(_get_duration)


if __name__ == "__main__":
    a = Shift(0, (5, 30), (14, 45))
    print(a.duration)
