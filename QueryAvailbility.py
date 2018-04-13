import sqlite3

db = sqlite3.connect(":memory:")

a = open("./dummydata.sql").read()

db.executescript(a)

query = ""

out = db.execute(query)

print(out)
