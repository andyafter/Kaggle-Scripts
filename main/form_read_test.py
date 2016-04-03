from readers.reader import DataReader

a = DataReader()

crime_time= {}
for date in a.train.Dates:
    time = date.split()[1].split(':')[0]
    if time not in crime_time:
        crime_time[time] = 1
    else:
        crime_time[time] += 1
