import psycopg2, os
from flask import Flask, request, json, render_template

from src.schedule import Schedule
from src.stations import Stations

try:
    database = os.environ.get('DATABASE')
    user = os.environ.get('USER')
    host = os.environ.get('HOST')
    port = 5432
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
    return render_template('ticket.html', booking=request.args)


@app.route('/', methods=['GET'])
def welcome():
    return render_template('home.html', stations=stations)


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


@app.route('/search/', methods=['GET'])
def search():
    search_parameters = request.args
    limit = 5
    obtained_schedule = schedule.get_schedule(search_parameters, limit)
    return render_template('search.html', result=obtained_schedule)


if __name__ == '__main__':
    app.run(use_reloader=True)
