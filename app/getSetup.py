import urllib.parse
import pyodbc 

hostName = "http://localhost:8000/gdsdggda?sfggs=sgsg"
currentUuid = "e03e5d14709911eb998b0242ac110002"


parsed_url = urllib.parse.urlparse(hostName)

print(parsed_url.netloc)




cursor = conn.cursor()
cursor.execute('SELECT * FROM t_domains')

for row in cursor:
    print(row)
