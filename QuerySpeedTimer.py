import sqlite3
import random
from timeit import default_timer as timer


db = sqlite3.connect("SQlitePerformanceTestDB.db")
db.isolation_level = None

count=0
start = timer()
RandomFilmYear = random.randint(1900, 2000)  

db.execute("SELECT COUNT (*) FROM FILMS WHERE year = ?", [RandomFilmYear]) 
count +=1

end = timer()

print(end - start, "seconds") 