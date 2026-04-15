# post json files into postgresql 

# https://www.geeksforgeeks.org/psycopg2-insert-dictionary-as-json/

import json
import psycopg2
from datetime import datetime

# connect to postgresql
#conn = psycopg2.connect(
    #dbname="",
    #user="",
    #password="",
    #host="",
    #port=""
#)
cursor = conn.cursor()

# loop through json files
for i in range(1, 22):  # 21 json files 
    file_name = f"/Users/sgaheer/Downloads/ServiceNow/tickets/tickets_part_{i}.json"
    with open(file_name, 'r') as file:
        datalist = json.load(file)
        
        # loop through data because list is array
        
        for data in datalist:
        
        # Extract the relevant fields
            ticket_number = data.get("number") # ticket number is always going to be there
            short_discription = data.get("short_description", "") or None
            assignment_group = data.get("assignment_group", {}).get("display_value", "") or None
            comments = data.get("comments", "") or None
            date_created = data.get("sys_created_on", "") or None
            date_closed = data.get("closed_at", "") or None
            close_notes = data.get("close_notes", "") or None
            business_duration = data.get("business_duration", "") or None
        
            ### Convert the dates to a PostgreSQL-friendly format ###
            if date_created and date_created != "": # check if there is an empty string ("")
                try:
                    date_created = datetime.strptime(date_created, '%m-%d-%Y %I:%M %p')
                except ValueError:
                    date_created = None # date is empty
            else:
                date_created = None 
            
            if date_closed and date_closed != "":
                try:
                    date_closed = datetime.strptime(date_closed, '%m-%d-%Y %I:%M %p')
                except ValueError:
                    date_closed = None # date is empty
            else:
                date_closed = None
                            
            print(f"About to insert ticket #:{ticket_number}")
                              
            try: 
            # inserton of data
                cursor.execute(
                    "INSERT INTO tickets (ticket_number, short_discription, assignment_group, comments, date_created, date_closed, business_duration) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (ticket_number, short_discription, assignment_group, comments, date_created, date_closed, business_duration)
                )
            
            except psycopg2.Error as e:
                # Log the error and the problematic ticket number
                print(f"Error inserting ticket #: {ticket_number}")
                print(f"Error details: {e}")
            
    # commit and close
            conn.commit()
cursor.close()
conn.close()

# data is weird <- look at ticket number when having issue