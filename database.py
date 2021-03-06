import abc
import sqlite3
import pymysql
import Scheduling
import pickle
import sys


class Database(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        self.database = None
        self.command = None

    @abc.abstractmethod
    def query(self, query, params):
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
        query = "SELECT schedule FROM Work_Schedule WHERE week_id=&CHAR"
        print(weekid, sys.stdout)
        self.query(query, (weekid, ))
        blob = self.fetchdata()[0][0]
        schedule = pickle.loads(blob)
        return schedule

    def insertschedule(self, schedule: Scheduling.Schedule):
        blob = pickle.dumps(schedule)
        query = "REPLACE INTO Work_Schedule VALUES (&CHAR,&CHAR)"
        self.query(query, (schedule.weekid, blob))
        self.commit()

    def login(self, uname):
        query = "SELECT employee_id, passwd FROM user WHERE employee_id =&CHAR"
        self.query(query, (uname, ))
        return self.fetchdata()

    def getavailability(self, employeeid, day):
        query = "SELECT `1` FROM Availability WHERE employee_id=&CHAR"
        params = (day, employeeid)
        self.query(query, params)
        return self.fetchdata()

    def insertavailability(self, employeeid, availability):
        # Todo check structure of  availability
        query = "INSERT INTO Availability VALUES (&CHAR,&CHAR,&CHAR,&CHAR,&CHAR,&CHAR,&CHAR,&CHAR)"
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
            query = "UPDATE Availability SET &CHAR='&CHAR' WHERE employee_id='&CHAR'"
            params = (days[index], availability[index], employeeid)
            self.query(query, params)
            self.commit()


class DebugDatabase(Database):

    def __init__(self, file=":memory:"):
        self.database = sqlite3.connect(file, check_same_thread=False)
        self.__generate__()
        self.command = None

    def __generate__(self, script="./OPTSchema.sql"):
        schema = open(script).read()
        self.database.executescript(schema)

    def query(self, query, params=()):
        query = query.replace("&CHAR", "?")
        self.command = self.database.execute(query, params)

    def commit(self):
        self.database.commit()

    def fetchdata(self):
        return self.command.fetchall()

    def close(self):
        self.database.close()


class RemoteDatabase(Database):

    def __init__(self, host='127.0.0.1', user='root', password='', db='OPTSchema'):
        self.database = pymysql.connect(host, user, password, db)
        self.command = None
        self.cursor = self.database.cursor()

    def query(self, query, params):
        query = query.replace("&CHAR", "%s")
        self.command = self.cursor.execute(query, params)

    def commit(self):
        self.database.commit()

    def fetchdata(self):
        return self.cursor.fetchall()

    def close(self):
        self.database.close()


class DatabaseInterface:

    def __init__(self, debug=True):
        self.db = DebugDatabase() if debug else RemoteDatabase()


if __name__ == "__main__":
    interface = DatabaseInterface()
    interface.db.getavailability("`0`", 0)
    print(interface.db.fetchdata())
