import sys
import pypyodbc as odbc

records = [
    ["Euro","Nattanan","0957395770","Moderna","Moderna","NULL","NULL",1,"NULL"],
    ["Earn","Pinyanun","0957395770","Moderna","Moderna","NULL","NULL",1,"NULL"]
]

DRIVER = 'SQL Server'
SERVER_NAME = 'DESKTOP-NDKJAVS\SQLEXPRESSV2'
DATABASE_NAME = 'capstone'

conn_string = f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trust_Connection=yes;
"""

try:
    conn = odbc.connect(conn_string)
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:
    cursor = conn.cursor()


insert_statement = """
    INSERT INTO dbo.vaccine_record_v02
    VALUES (?, ?, ?, ?)
"""

try:
    for record in records:
        print(record)
        cursor.execute(insert_statement, record)        
except Exception as e:
    cursor.rollback()
    print(e.value)
    print('transaction rolled back')
else:
    print('records inserted successfully')
    cursor.commit()
    cursor.close()
finally:
    if conn.connected == 1:
        print('connection closed')
        conn.close()