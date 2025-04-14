import csv
import datetime

crimes = {}

with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if index == 0:
            continue
        try:
            crimeDate = datetime.datetime.strptime(row[2].strip(), "%m/%d/%Y %I:%M:%S %p").date()
            crimeName = row[5]
            # crimeDate = datetime.datetime.strptime("10/01/2002 12:47:08 PM", "%m/%d/%Y %I:%M:%S %p").date()
            if crimeDate.year == 2015:
                if crimes.get(crimeName):
                    crimes[row[5]] += 1
                else:
                    crimes[crimeName] = 1
            # print(crimeDate.year, row[5])
        except ValueError as e:
            print('some error in row with data', row, index)
            break
        # print(row)

print(crimes)
max_key = max(crimes, key=crimes.get)
max_value = crimes[max_key]

print (max_key, max_value)