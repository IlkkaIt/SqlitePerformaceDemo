import sqlite3
import random
from timeit import default_timer as timer
from sqlite3.dbapi2 import Cursor


db = sqlite3.connect("SQlitePerformanceTestDB.db")
db.isolation_level = None
cursor = db.cursor()

RandomFilmYear = random.randint(1900, 2000) 

start = timer() 

db.execute("SELECT * FROM FILMS WHERE year = ?", [RandomFilmYear]) 

end = timer()


SelectedFilmList = db.execute("SELECT * FROM FILMS WHERE year = ?", [RandomFilmYear]).fetchall()

cursor.execute("SELECT COUNT (*) FROM FILMS WHERE year = ?", [RandomFilmYear])
TupleFilmsCount = cursor.fetchone()                     
IntFilmsCount = int(''.join(map(str, TupleFilmsCount))) #Python cursor returns tuple like "(188)," that needs to be stylized to "188"

print(SelectedFilmList)
print(IntFilmsCount, "films published",  RandomFilmYear) 
print("query took", end - start, "seconds") 