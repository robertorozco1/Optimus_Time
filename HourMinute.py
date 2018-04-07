class HourMinute:

    def __init__(self, hour: int, minute: int):
        self.__hour = None
        self.__minute = None

        self.hour = hour
        self.minute = minute

    def __sub__(self, other):
        minutes1 = (self.hour * 60) + self.minute
        minutes2 = (other.hour * 60) + other.minute
        totalminutes = abs(minutes1 - minutes2)
        return HourMinute(totalminutes // 60, totalminutes % 60)

    def __repr__(self):
        return str(self.hour) + ":" + str(self.minute)

    def _get_hour(self):
        return self.__hour

    def _set_hour(self, hour):
        if hour not in range(0, 24):
            raise ValueError("Hour value should be in the range of 0 to 24")
        self.__hour = hour

    def _get_minute(self):
        return self.__minute

    def _set_minute(self, minute):
        if minute not in range(0, 60):
            raise ValueError("Minute value should be in the range of 0 to 60")
        self.__minute = minute

    hour = property(_get_hour, _set_hour)
    minute = property(_get_minute, _set_minute)


if __name__ == "__main__":
    a = HourMinute(7, 30)
    b = HourMinute(16, 45)
    print(b)
    c = a-b
    print(c)
