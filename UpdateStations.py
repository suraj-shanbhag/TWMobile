import psycopg2
import csv
try:
    connection = psycopg2.connect(database="twmobile", user="surajus", host="localhost", port=5432)
except:
    print "Try again"

cursor = connection.cursor()
def read_csv_to_db(file_obj):
    reader = csv.reader(file_obj)
    headers=reader.next()
    print headers
    for row in reader:
        print row[0],row[1]
        query = "INSERT INTO stations (" + headers[0] + "," + headers[1] + ") VALUES ('" + row[0] + "','" + row[1] + "');"
        print query;
        cursor.execute(query)
    connection.commit()
    connection.close()
if __name__ == "__main__":
    with open("data/stations.csv") as f_obj:
        read_csv_to_db(f_obj)