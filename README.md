# SqlitePerformaceDemo
DbTableWithIndexCreation.py

Creates sqlite-database containing 10 000 line 2 column table inside your project folder. 
You can custom the number of lines in the database table by changing the count-value in the loop "while(count<10000): ..." .
If you make table larger, say 100 000 lines for example, operation described below may take quite a while (at least with regular home pc). 

By commenting/uncommenting lines executing transaction (Begin-Commit) you can observe how transaction affects performance: 
There is a simple timer telling how long it takes to create a database table.
Remember to delete, rename or remove database file SQlitePerformanceTestDB.db before running DbTableWithIndexCreation.py again.

QuerySpeedTimer.py

In DbTableWithIndexCreation.py you can also comment or uncomment line creating index on column year.
Of course you can create index on column "year" elsewhere for example in SQL-Workbench.
After that you can run QuerySpeedTimer.py to check if indexing has any effect to the speed of the query.

