import psycopg2, os
from flask import Flask, request, json

from src.schedule import Schedule
from src.stations import Stations

try:
    database = os.environ.get('DATABASE')
    user = os.environ.get('USER')
    host = os.environ.get('HOST')
    port = os.environ.get('PORT')
    password = os.environ.get('PASSWORD')
    connection = psycopg2.connect(database=database, user=user,
                                  host=host, port=port,
                                  password=password)
except:
    print ('Cannot connect to Database')

cursor = connection.cursor()
stations = Stations(cursor=cursor).stations
schedule = Schedule(cursor=cursor)

app = Flask(__name__)
app.debug = True


@app.route('/stations/', methods=['GET'])
def get_all_stations():
    return json.jsonify(stations)


@app.route('/book/', methods=['GET'])
def book_results():
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
