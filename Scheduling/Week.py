from Scheduling.Day import Day
INITIALSTATE = [
    (0, None),
    (1, None),
    (2, None),
    (3, None),
    (4, None),
    (5, None),
    (6, None)
]


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
        if value.weekday != key:
            raise ValueError("Weekday must be same value of ")
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
        if other.keys() == self.keys():
            super(Week, self).update(other)

    @staticmethod
    def fromkeys():
        raise AttributeError("Week has no attribute fromkeys")

    @staticmethod
    def clear():
        raise AttributeError("Week has no attribute clear")

    def copy(self):
        return Week(self.items())


if __name__ == "__main__":
    a = Week()
    a[0] = Day(0)
    print(a.items())
    print(a.copy())