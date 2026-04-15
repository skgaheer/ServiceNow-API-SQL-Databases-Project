This project was just me exploring how to pull data from an API (ServiceNow) and how to put that data into a database. 
There are three important files that I have written throughout this process that is important to me. 

1. API_Call_JSON.py

This file basically pulls the data from ServiceNow, using pagination, because the API limits pulls to a certain number of 
records at a time. This process taught me a couple of things (1) how to pull data from API requests, and (2) how to handle it if it's 
a lot of data. It also gave me my first exposure to how JSON files are used in data handling.  

2. postgresql.py

This file taught me how to put data into a Postgres database. It also taught me that SQL and Python can be used together in such 
interesting ways!

3. table_creation.sql

This file gave me first-hand exposure to making my own SQL table and the various ways I could work with the table. 

5. Write-Up.ipynb

This file is a write-up of how to interact with the SQL table.


