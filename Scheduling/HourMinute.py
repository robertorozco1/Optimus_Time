MINUTESINHOUR = 60


class HourMinute:

    def __init__(self, hour=None, minute=0):
        self.__hour = None
        self.__minute = None

        if hour is None:
            self._set_totalminutes(minute)
        else:
            self.hour = hour
            self.minute = minute

    def __add__(self, other):
        totalminutes = self.totalminutes + other.totalminutes
        return HourMinute(None, totalminutes)

    def __sub__(self, other):
        totalminutes = abs(self.totalminutes - other.totalminutes)
        return HourMinute(None, totalminutes)

    def __lt__(self, other):
        return self.totalminutes < other.totalminutes

    def __le__(self, other):
        return self.totalminutes <= other.totalminutes

    def __gt__(self, other):
        return self.totalminutes > other.totalminutes

    def __ge__(self, other):
        return self.totalminutes >= other.totalminutes

    def __eq__(self, other):
        return self.totalminutes == other.totalminutes

    def __ne__(self, other):
        return self.totalminutes != other.totalminutes

    def __repr__(self):
        return str((self.hour, self.minute))

    def __str__(self):
        return str(self.hour) + ":" + str(self.minute)

    def _get_hour(self):
        return self.__hour

    def _set_hour(self, hour):
        if hour < 0:
            raise ValueError("Cannot have negative hours")
        self.__hour = hour

    def _get_minute(self):
        return self.__minute

    def _set_minute(self, minute):
        if minute not in range(0, MINUTESINHOUR):
            raise ValueError("Minute value should be in the range of 0 to 60")
        self.__minute = minute

    def _get_totalminutes(self):
        return (self.hour * MINUTESINHOUR) + self.minute

    def _set_totalminutes(self, minutes):
        self.hour = minutes // MINUTESINHOUR
        self.minute = minutes % MINUTESINHOUR

    hour = property(_get_hour, _set_hour)
    minute = property(_get_minute, _set_minute)
    totalminutes = property(_get_totalminutes, _set_totalminutes)


if __name__ == "__main__":
    a = HourMinute(7, 30)
    b = HourMinute(16, 45)
    print(b)
    c = a-b
    print(c)
