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
        query = "INSERT INTO schedule (" + headers[0] + "," + headers[1] +"," + headers[2] + "," + headers[3] + "," + headers[4] +"," + headers[5] +") VALUES ('" + row[0] + "','" + row[1] + "','" + row[2] + "','" + row[3] +"','" + row[4] +"','" + row[5] + "');"
        print query;
        cursor.execute(query)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    with open("data/schedule2.csv") as f_obj:
        read_csv_to_db(f_obj)