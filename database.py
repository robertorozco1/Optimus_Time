import abc
import sqlite3
import pymysql


class Database(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        self.database = None
        self.command = None

    @abc.abstractmethod
    def query(self, query):
        ...

    @abc.abstractmethod
    def fetchdata(self):
        ...


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

    def fetchdata(self):
        return self.command.fetchall()


class RemoteDatabase(Database):

    def __init__(self, host='127.0.0.1', user='root', password='', db='dummydata'):
        self.database = pymysql.connect(host, user, password, db)
        self.command = None
        self.cursor = self.database.cursor()

    def query(self, query):
        self.command = self.cursor.execute(query)

    def fetchdata(self):
        return self.cursor.fetchall()
