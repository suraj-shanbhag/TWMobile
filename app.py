import psycopg2
from flask import Flask, request, json

from src.schedule import Schedule
from src.stations import Stations

try:
    connection = psycopg2.connect(database="d641qm9k3ulc1o", user="qjsyryvmvxwmol",
                                  host="ec2-107-22-167-179.compute-1.amazonaws.com", port=5432,
                                  password="6f388937e1b6ecd4f1ee16eca44048295fc1a6e8aa31a269d0730d4de6571c47")
except:
    print "Try again"

app = Flask(__name__)
app.debug = True
cursor = connection.cursor()
stations = Stations(cursor=cursor).stations
schedule = Schedule(cursor=cursor)


@app.route('/stations/', methods=['GET'])
def get_all_stations():
    return json.jsonify(stations)

@app.route('/book/', methods=['GET'])
def get_all_stations():
    return "Your ticket has been booked \nThanks For your interest have a safe journey"


@app.route('/', methods=['GET'])
def welcome():
    return "Server is Hot"


@app.route('/validate/', methods=['GET'])
def validate_station():
    station_name = request.args['station']
    if station_name in stations:
        return stations[station_name]
    return "Invalid Station"


@app.route('/schedule/', methods=['GET'])
def fetch_schedule():
    search_parameters = request.args
    limit = 5
    obtained_schedule = schedule.get_schedule(search_parameters, limit)
    return json.jsonify(obtained_schedule)

if __name__ == '__main__':
    app.run(use_reloader=True)
