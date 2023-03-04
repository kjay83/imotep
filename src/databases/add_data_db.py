import sqlite3
conn = sqlite3.connect("people.db")
people = [
    "1, 'DE-JARGET_OSCAR',\
        'DE-JARGET', 'Jarget',\
        'Oscar','',\
        'oscar@gmail.com','',\
        'MSF74, pnr','',\
        '05 14 87 59 43','',\
        'F',\
        '2022-10-08 09:15:10'",
    "2, 'KENT_CLARK',\
        'KENT', '',\
        'Clark','Balist',\
        'ckent@gmail.com','ckent2@gmail.com',\
        'MSFKENT, pnr','MSFKENT, paris',\
        '05 14 87 59 47','05 14 87 59 22',\
        'M',\
        '2022-10-08 09:15:23'",
    "3, 'LENNON_JOHN',\
        'LENNON', '',\
        'John','Blinker',\
        'jleonon@gmail.com','',\
        'MSF LENNONG, pnr','',\
        '05 14 87 59 47','05 14 87 59 12',\
        'M',\
        '2022-10-08 09:15:33'",
    "4, 'LENNON_MARTHA',\
        'LENNON', '',\
        'Martha','',\
        'lmartha@gmail.com','',\
        'MSF LENNONG, pnr','',\
        '05 14 87 59 47','05 14 87 59 12',\
        'F',\
        '2022-10-08 09:15:13'",
]

for people_data in people:
    insert_cmd = f"INSERT INTO people VALUES ({people_data})"
    conn.execute(insert_cmd)





conn.commit()
