import datetime


class Schedule(object):
    def __init__(self, cursor, stations):
        self.stations = stations
        self.cursor = cursor

    def get_schedule(self, parameters, limit):
        day = datetime.datetime.strptime(parameters['day'], '%Y-%m-%d').strftime('%a')
        query = "SELECT * FROM SCHEDULE WHERE start_code='%s' and end_code='%s' and day='%s' and time_of_arrival>='%s' order by time_of_arrival limit %s" % (
            parameters['source'], parameters['destination'], day, parameters['time'], limit)
        self.cursor.execute(query)
        return self._dicnarify(self.cursor.fetchall(), parameters)

    def _dicnarify(self, results, parameters):
        station_names = self.stations.keys()
        station_codes = self.stations.values()
        source = station_names[station_codes.index(parameters['source'])]
        destination = station_names[station_codes.index(parameters['destination'])]
        result = {"source": source,
                  "destination": destination,
                  "day": parameters['day'],
                  "time": parameters['time']}
        schedule = []
        for row in results:
            item = {'time': str(row[3]), 'cost': row[4], 'duration': str(row[5])}
            schedule.append(item)
        result["schedule"] = schedule
        return result
