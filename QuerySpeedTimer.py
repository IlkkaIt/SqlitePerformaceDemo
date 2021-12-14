import sqlite3
import random
from timeit import default_timer as timer


db = sqlite3.connect("ElokuvatIndeksiFinal.db")
db.isolation_level = None

count=0
start = timer()
RandomElokuvaVuosi = random.randint(1900, 2000)  

db.execute("SELECT COUNT (*) FROM UNINDEXED_FILMS WHERE vuosi = ?", [RandomElokuvaVuosi]) 
count +=1

end = timer()

print(end - start, "sekuntia") 