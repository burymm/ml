import datetime

year, month, day = map(int, input("Date ").split())
days = int(input("Days: "))
date = datetime.date(year, month, day)
endDate = date + datetime.timedelta(days)


print(endDate.year, endDate.month, endDate.day)