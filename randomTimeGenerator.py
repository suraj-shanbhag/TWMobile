import random
from datetime import timedelta
import csv
import psycopg2

Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
try:
    connection = psycopg2.connect(database="twmobile", user="surajus", host="localhost", port=5432)
except:
    print "Try again"
cursor = connection.cursor();


def getStations():
    stations=[]
    query = "select * from stations"
    cursor.execute(query)
    station_results = cursor.fetchall()
    for value in station_results:
        stations.append(value[1]);
    return stations


def to_minutes(total_seconds):
    return total_seconds / 60

if __name__ == "__main__":
    stations=getStations()
    start = timedelta(hours=6, minutes=0)
    end = timedelta(hours=23, minutes=55)
    max_seconds = end.seconds - start.seconds
    max_minute = to_minutes(max_seconds)

    count = 0
    with open('data/schedule2.csv', 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["start_code", "end_code", "day", "time_of_arrival","cost","duration"])
        for station_1 in stations:
            for station_2 in stations:
                if (station_1 != station_2):
                    cost=random.randrange(start=100, stop=1000, step=50)
                    duration = timedelta(minutes=(random.randrange(start=90, stop=720, step=5)))
                    for day in Days:
                        for i in range(15):
                            minute = random.randrange(start=0, stop=max_minute, step=5)
                            minute_delta = timedelta(minutes=minute)
                            time = start + minute_delta
                            count += 1
                            cost_delta = random.randrange(start=-40, stop=40, step=5)
                            duration_delta = timedelta(minutes=(random.randrange(start=-20, stop=20, step=2)))
                            writer.writerow([station_1,station_2,day,str(time),str(cost+cost_delta),str(duration+duration_delta)])
        print count