from HourMinute import HourMinute


class Shift:

    def __init__(self, employeeid: int, start, end):

        self.__employeeid = None
        self.__start = None
        self.__end = None

        self.employeeid = employeeid

        if start is not HourMinute:
            if len(start) != 2:
                raise ValueError("Start must be of type HourMinute or length of 2")
            self.start = HourMinute(start[0], start[1])
        else:
            self.start = start

        if end is not HourMinute:
            if len(end) != 2:
                raise ValueError("End must be of type HourMinute or length of 2")
            self.end = HourMinute(end[0], end[1])
        else:
            self.end = end

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

    employeeid = property(_get_employeeid,_set_employeeid)
    start = property(_get_start, _set_start)
    end = property(_get_end, _set_end)
    duration = property(_get_duration)


if __name__ == "__main__":
    a = Shift(0, (5, 30), (14, 45))
    print(a.duration)
