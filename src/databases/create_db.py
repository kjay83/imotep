import sqlite3
conn = sqlite3.connect("people.db")
columns = [
     "id INTEGER PRIMARY KEY",
     "unique_reference VARCHAR UNIQUE",
     "lname1 VARCHAR ",
     "lname2 VARCHAR ",
     "fname1 VARCHAR",
     "fname2 VARCHAR",
     "email1 VARCHAR",
     "email2 VARCHAR",
     "address1 VARCHAR",
     "address2 VARCHAR",
     "phone1 VARCHAR",
     "phone2 VARCHAR",
     "sex VARCHAR",
     "timestamp DATETIME",
 ]
create_table_cmd = f"CREATE TABLE people ({','.join(columns)})"
conn.execute(create_table_cmd)