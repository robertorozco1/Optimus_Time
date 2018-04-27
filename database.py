import abc
import sqlite3
import pymysql
import Scheduling


class Database(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        self.database = None
        self.command = None

    @abc.abstractmethod
    def query(self, query):
        ...

    @abc.abstractmethod
    def commit(self):
        ...

    @abc.abstractmethod
    def fetchdata(self):
        ...

    @abc.abstractmethod
    def close(self):
        ...

    def getschedule(self, weekid):
        query = "FROM Work_Schedule SELECT schedule WHERE weekid=?"
        params = (weekid)
        self.query(query, params)
        return self.fetchdata()

    def insertschedule(self, schedule: Scheduling.Schedule):
        query = "INSERT INTO Work_Schedule VALUES '(?,?)'"
        params = (schedule.weekid, schedule)
        self.query(query, params)
        self.commit()

    def updateschedule(self, schedule):
        query = "UPDATE Work_Schedule SET schedule='?' WHERE weekid='?'"
        params = (schedule, schedule.weekid)
        self.query(query, params)
        self.commit()

    def getavailability(self, employeeid, day):
        if day is not int:
            raise TypeError("day must be type int")
        if day not in range(0, 7):
            raise ValueError("day must be in range of 1 to 6")
        query = "FROM Availability SELECT ? WHERE employee_id=?"
        params = (day, employeeid)
        self.query(query, params)
        return self.fetchdata()

    def insertavailability(self, employeeid, availability):
        # Todo check structure of  availability
        query = "INSERT INTO Availability VALUES '(?,?,?,?,?,?,?,?)'"
        params = (employeeid, *availability)
        self.query(query, params)
        self.commit()

    def updateavailability(self, employeeid, days, availability):
        # Todo Check structure of availability
        if len(days) != len(availability):
            raise ValueError("Number of availability entries must match the amount of days")
        if any(days) not in range(0, 7):
            raise ValueError("Days must be in range of 0 to 6")
        for index in range(len(days)):
            query = "UPDATE Availability SET ?='?' WHERE employee_id='?'"
            params = (days[index], availability[index], employeeid)
            self.query(query, params)
            self.commit()


class DebugDatabase(Database):

    def __init__(self, file=":memory:"):
        self.database = sqlite3.connect(file)
        self.__generate__()
        self.command = None

    def __generate__(self, script="./dummydata.sql"):
        schema = open(script).read()
        self.database.executescript(schema)

    def query(self, query):
        self.command = self.database.execute(query)

    def commit(self):
        self.database.commit()

    def fetchdata(self):
        return self.command.fetchall()

    def close(self):
        self.database.close()


class RemoteDatabase(Database):

    def __init__(self, host='127.0.0.1', user='root', password='', db='dummydata'):
        self.database = pymysql.connect(host, user, password, db)
        self.command = None
        self.cursor = self.database.cursor()

    def query(self, query):
        self.command = self.cursor.execute(query)

    def commit(self):
        self.database.commit()

    def fetchdata(self):
        return self.cursor.fetchall()

    def close(self):
        self.database.close()
