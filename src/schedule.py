class Schedule(object):
    def __init__(self, cursor):
        self.cursor = cursor

    def get_schedule(self, parameters, limit):
        self.cursor.execute(
            "SELECT * FROM SCHEDULE WHERE start_code='%s' and end_code='%s' and day='%s' and time_of_arrival>='%s' order by time_of_arrival limit %s" \
            % (parameters['source'], parameters['destination'], parameters['day'], parameters['time'], limit))
        return self._dicnarify(self.cursor.fetchall())

    def _dicnarify(self, results):
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
