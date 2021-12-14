import sqlite3
import random
import string
import os 
from timeit import default_timer as timer



db = sqlite3.connect("SQlitePerformanceTestDB.db")
db.isolation_level = None

try:
  db.execute("CREATE TABLE FILMS (id INTEGER PRIMARY KEY, name TEXT, year INTEGER)")
except:
   print("Table already exists")

count=0
start = timer()


db.execute("BEGIN") #You can disable transaction by commenting this line altogether with "db.execute("COMMIT")" -line

db.execute("CREATE INDEX idxYear ON FILMS (year)") #Comment this line if Yuo dont want to create index on column "year"
while(count<10000):  
    RandomFilmName = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(5))
    RandomFilmYear = random.randint(1900, 2000)  
    db.execute("INSERT INTO FILMS (name, year) VALUES (  ? , ? )",[RandomFilmName, RandomFilmYear])
    count +=1

db.execute("COMMIT") #You can disable transaction by commenting this line altogether with "db.execute("BEGIN")" -line


end = timer()  

tuloste = db.execute("SELECT * FROM INDEXED_FILMS").fetchall()
print(tuloste)
print(end - start, "seconds") 
db.close
