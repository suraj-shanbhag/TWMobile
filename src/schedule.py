import datetime


class Schedule(object):
    def __init__(self, cursor):
        self.cursor = cursor

    def get_schedule(self, parameters, limit):
        day = datetime.datetime.strptime(parameters['day'], '%Y-%m-%d').strftime('%a')
        query = "SELECT * FROM SCHEDULE WHERE start_code='%s' and end_code='%s' and day='%s' and time_of_arrival>='%s' order by time_of_arrival limit %s" % (
            parameters['source'], parameters['destination'], day, parameters['time'], limit)
        self.cursor.execute(query)
        return self._dicnarify(self.cursor.fetchall(), parameters)

    def _dicnarify(self, results, parameters):
        result = {"source": parameters['source'],
                  "destination": parameters['destination'],
                  "day": parameters['day']}
        schedule = []
        for row in results:
            item = {}
            item['time'] = str(row[3])
            item['cost'] = row[4]
            item['duration'] = str(row[5])
            schedule.append(item)
        result["schedule"] = schedule
        return result
