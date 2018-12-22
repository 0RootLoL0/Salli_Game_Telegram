import sys
import json
import psycopg2

conn = psycopg2.connect(dbname='ddsn9cpuvta6n6', user='ishjjypgrfjrlt', password='36d2511ed5ed0f50e436d37db05e690ed3499ce7168d9a12965cc264942b2fbd', host='ec2-107-20-237-78.compute-1.amazonaws.com')
cursor = conn.cursor()


if sys.argv[1] == "0":
    try:
        cursor.execute(sys.argv[2])
        print(200)
    except psycopg2.OperationalError:
        print(500)

elif sys.argv[1] == "1":
    try:
        cursor.execute(sys.argv[2])
        results = cursor.fetchall()
        print(json.dumps(results))
    except psycopg2.OperationalError:
        print(500)

conn.commit()
conn.close()