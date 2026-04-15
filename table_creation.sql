-- to connect to database: 

-- exit the psql shell:

-- to create the empty table in database: 
CREATE TABLE tickets (
    ticket_number VARCHAR(20) PRIMARY KEY,
    short_discription TEXT,
    assignment_group TEXT,
    comments TEXT,
    date_created TIMESTAMP,
    date_closed TIMESTAMP,
    close_notes TEXT,
    business_duration INTERVAL
);

-- or:

psql -U sgaheer -h localhost -p 5432 -d servicenow -c "CREATE TABLE tickets (
    ticket_number VARCHAR(20) PRIMARY KEY,
    short_discription TEXT,
    assignment_group TEXT,
    comments TEXT,
    date_created TIMESTAMP,
    date_closed TIMESTAMP,
    close_notes TEXT,
    business_duration INTERVAL
);"

-- verify!
psql -U sgaheer -h localhost -p 5432 -d servicenow

\dt

\d tickets