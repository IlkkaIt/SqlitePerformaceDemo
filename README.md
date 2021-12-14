# SqlitePerformaceDemo
SqlitePerformaceDemo includes Python files for demonstrating/testing performance effect of transactions and indexing.


DbTableWithIndexCreation.py

Creates 10 000 line 2 column sqlite-database inside your project folder. 
You can easily custom number of lines in the database by changing value in the loop "while(count<10000): ..." .

By commenting/uncommenting lines executing transaction (Begin-Commit) you can observe how transaction affects performance. 
There is a simple timer telling how long it takes to create database with or without the transaction.
Remember to delete or rename database file SQlitePerformanceTestDB.db before running DbTableWithIndexCreation.py again.
 
You can also comment or uncomment line creating index on column year and observe how indexing affects speed of queries by running QuerySpeedTimer.py
