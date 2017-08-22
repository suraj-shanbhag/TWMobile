from flask import Flask, request, json

import psycopg2
from stations import Stations

try:
    connection = psycopg2.connect(database="twmobile", user="surajus", host="localhost", port=5432)
except:
    print "Try again"

app = Flask(__name__)
app.debug = True
stations = Stations(path='../data/stations.csv').stations
cursor = connection.cursor()


@app.route('/getAllStations/', methods=['GET'])
def get_all_stations():
    return json.jsonify(stations)


@app.route('/validate/', methods=['GET'])
def validate_station():
    station_name = request.args['station']
    if station_name in stations:
        return stations[station_name]
    return "Invalid Station"


def fetchschedule(parameters, limit):
    cursor.execute(
        "SELECT * FROM SCHEDULE WHERE start_code='%s' and end_code='%s' and day='%s' and time_of_arrival>='%s' order by time_of_arrival limit %s" \
        % (parameters['source'], parameters['destination'], parameters['day'], parameters['time'], limit))
    return json.jsonify(dicnarify(cursor.fetchall()))


def dicnarify(results):
    result = {"source": results[0][0], "destination": results[0][1]}
    schedule = []
    for row in results:
        item = {}
        item['time'] = str(row[3])
        item['cost'] = row[4]
        item['duration'] = str(row[5])
        schedule.append(item)

    result["schedule"] = schedule
    return result


@app.route('/schedule/', methods=['GET'])
def fetch_schedule():
    search_parameters = request.args
    limit = 5
    return fetchschedule(search_parameters, limit)


# if __name__ == '__main__':
app.run(host='0.0.0.0', port=8000)
