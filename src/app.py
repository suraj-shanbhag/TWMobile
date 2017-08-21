from flask import Flask, request

from stations import Stations

app = Flask(__name__)
app.debug = True
stations = Stations(path='../data/stations.csv').stations


@app.route('/validate/', methods=['GET'])
def validate_station():
    station_name = request.args['station']
    if station_name in stations:
        return stations[station_name]
    return "Invalid Station"


@app.route('/schedule/', methods=['GET'])
def fetch_schedule():
    search_parameters = request.args
    return "You want to travel from %s to %s on %s" % (
        search_parameters['source'], search_parameters['destination'], search_parameters['day'])


# if __name__ == '__main__':
app.run(host='0.0.0.0', port=8000)
