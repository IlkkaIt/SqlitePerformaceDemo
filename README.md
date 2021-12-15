# SqlitePerformaceDemo
SqlitePerformaceDemo includes Python files for demonstrating/testing effect of transactions and indexing for performance.


DbTableWithIndexCreation.py

Creates 10 000 line 2 column sqlite-database inside your project folder. 
You can easily custom number of lines in the database by changing the count-value in the loop "while(count<10000): ..." .
If you make database very large, say 100 000 lines for example, some of operations described below may take quite a while. 

By commenting/uncommenting lines executing transaction (Begin-Commit) you can observe how transaction affects performance: 
There is a simple timer telling how long it takes to create a database.
Remember to delete, rename or move database file SQlitePerformanceTestDB.db before running DbTableWithIndexCreation.py again.

QuerySpeedTimer.py

In DbTableWithIndexCreation.py you can also comment or uncomment line creating index on column year and observe how indexing affects the speed of queries.

Of course you can create index on column "year" elswhere for example in Sql-Workbench.

After that you can run QuerySpeedTimer.py to check if indexing has any effect for the speed of the query.

