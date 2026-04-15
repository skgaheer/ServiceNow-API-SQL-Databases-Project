# This script DOWNLOADED tickets from ServiceNow

import requests
import json

url = 'add url here'
filter_str = 'check API documentation here'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
limit = 1000  # Batch size for each API request
offset = 0
batch_size = 2000  # Number of tickets per file
file_count = 1  # File counter for naming

all_tickets = []  # Temporary list to store batches before writing

while True:
    request_url = f'{url}?sysparm_limit={limit}&sysparm_offset={offset}&{filter_str}'
    response = requests.get(request_url, auth=('user', 'password'), headers=headers)

    if response.status_code != 200:
        raise ConnectionError(f'Error getting tickets, received status code: {response.status_code}')
    
    try:
        tickets = response.json().get('result', [])  # Get the 'result'
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(f"Response text: {response.text[:1000]}")  # Print first 1000 characters for review
        break

    if not tickets:
        break  # Exit the loop if no more tickets

    all_tickets.extend(tickets)  # Add the tickets to the list

    # If we reach the batch size, write to a new JSON file
    if len(all_tickets) >= batch_size:
        file_name = f'tickets_part_{file_count}.json'
        with open(file_name, 'w') as f:
            json.dump(all_tickets, f, indent=4)  # Write the batch to a JSON file
        print(f'Wrote {len(all_tickets)} tickets to {file_name}')
        
        # Clear the list and increment the file counter
        all_tickets = []
        file_count += 1

    offset += limit  # Move to the next batch

# Write any remaining tickets that didn't fill up to the batch size
if all_tickets:
    file_name = f'tickets_part_{file_count}.json'
    with open(file_name, 'w') as f:
        json.dump(all_tickets, f, indent=4)
    print(f'Wrote {len(all_tickets)} remaining tickets to {file_name}')
    
# The code below counts the number of tickets all together. 
import json
total_tickets = 0

for i in range(1, 22):  # Loop through 22 json files 
    file_name = f"/Users/sgaheer/Downloads/ServiceNow/tickets/tickets_part_{i}.json"
    with open(file_name, 'r') as file:
        datalist = json.load(file)
        ticket_count = len(datalist)  # Count tickets in this file
        total_tickets += ticket_count
        print(f"File {file_name} contains {ticket_count} tickets.")

print(f"Total number of tickets across all files: {total_tickets}")
