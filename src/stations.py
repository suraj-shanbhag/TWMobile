import csv


class Stations(object):
    def __init__(self, path):
        self.path = path
        self.stations = self.get_stations()

    def get_stations(self):
        with open(self.path, 'rb') as f:
            reader = csv.reader(f)
            stations = {}
            for line in reader:
                stations[line[0]] = line[1]
            return stations
