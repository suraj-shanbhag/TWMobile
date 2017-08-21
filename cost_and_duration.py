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
