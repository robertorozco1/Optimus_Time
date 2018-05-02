from Scheduling.Day import Day
INITIALSTATE = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}


class Week(dict):

    def __init__(self, adict=None):
        super(Week, self).__init__(INITIALSTATE)
        if adict is not None:
            self.update(adict)

    def __setitem__(self, key, value: Day):
        if type(value) is not Day:
            raise TypeError("Key must be of type Day")
        if not self.__contains__(key):
            raise KeyError("Keys must be day of week")
        super(Week, self).__setitem__(key, value)

    @staticmethod
    def __delitem__(self):
        raise AttributeError("Week has no attribute __delitem__")

    @staticmethod
    def pop():
        raise AttributeError("Week has no attribute pop")

    @staticmethod
    def popitem():
        raise AttributeError("Week has no attribute popitem")

    def update(self, other):
        if type(other) is not dict:
            other = dict(other)
        if not all(key in self.keys() for key in other.keys()):
            raise KeyError("Keys for week must be 0-6, representing days of the week")
        super(Week, self).update(other)

    @staticmethod
    def fromkeys():
        raise AttributeError("Week has no attribute fromkeys")

    @staticmethod
    def clear():
        raise AttributeError("Week has no attribute clear")

    def copy(self):
        return Week(self.items())

    @property
    def sunday(self):
        return super(Week, self).__getitem__(0)

    @sunday.setter
    def sunday(self, value):
        self.__setitem__(0, value)

    @property
    def monday(self):
        return super(Week, self).__getitem__(1)

    @monday.setter
    def monday(self, value):
        self.__setitem__(1, value)

    @property
    def tuesday(self):
        return super(Week, self).__getitem__(2)

    @tuesday.setter
    def tuesday(self, value):
        self.__setitem__(2, value)

    @property
    def wednesday(self):
        return super(Week, self).__getitem__(3)

    @wednesday.setter
    def wednesday(self, value):
        self.__setitem__(3, value)

    @property
    def thursday(self):
        return super(Week, self).__getitem__(4)

    @thursday.setter
    def thursday(self, value):
        self.__setitem__(4, value)

    @property
    def friday(self):
        return super(Week, self).__getitem__(5)

    @friday.setter
    def friday(self, value):
        self.__setitem__(5, value)

    @property
    def saturday(self):
        return super(Week, self).__getitem__(6)

    @saturday.setter
    def saturday(self, value):
        self.__setitem__(6, value)

    def days(self):
        return self.items()

    def employeeweek(self, employeeid):
        employeeweek = Week()
        for item in self.items():
            employeeweek.update({item[0]: item[1].employeeday(employeeid)})
        return employeeweek


if __name__ == "__main__":
    a = Week()
    a.sunday = Day()
    print(a.items())
    print(a.sunday)
