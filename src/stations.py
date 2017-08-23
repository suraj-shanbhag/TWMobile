class Stations(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.stations = self.get_stations()

    def get_stations(self):
        self.cursor.execute('SELECT * FROM stations')
        result = self.cursor.fetchall()
        stations = {}
        for line in result:
            stations[line[0]] = line[1]
        return stations
