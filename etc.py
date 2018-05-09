import datetime

def weeknum():
    weeknum = str(datetime.date.today().isocalendar()[1])
    year = str(datetime.date.today().isocalendar()[0])
    return int(year + weeknum)