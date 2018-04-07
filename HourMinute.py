class HourMinute:

    def __init__(self, hour: int, minute: int):
        self.__hour = 0
        self.__minute = 0

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

    def _set_hour(self, hour: range(0, 24)):
        self.__hour = hour

    def _get_minute(self):
        return self.__minute

    def _set_minute(self, minute: range(0, 24)):
        self.__minute = minute

    hour = property(_get_hour, _set_hour)
    minute = property(_get_minute, _set_minute)


if __name__ == "__main__":
    a = HourMinute(7, 30)
    b = HourMinute(16, 0)
    c = a-b
    print(c)
