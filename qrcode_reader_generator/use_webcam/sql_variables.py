import sys 
import pypyodbc as odbc
import time

#database variables
database_var = {
    "DRIVER": 'SQL Server',
    "SERVER_NAME": 'DESKTOP-NDKJAVS\SQLEXPRESSV2',
    "DATABASE_NAME": 'capstone'
}

#connection variables
connection = f"""
    Driver={{{database_var["DRIVER"]}}};
    Server={database_var["SERVER_NAME"]};
    Database={database_var["DATABASE_NAME"]};
    Trust_Connection = yes;
"""

#insert statement to insert to SQL database
#add ? according to the number of element in the record list
insert_statement = """
    INSERT INTO dbo.vaccine_record_v02
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

#function to insert list to SQL database
def insertRecord(connection_string, statement, records):
    connect = odbc.connect(connection_string)
    cursor = connect.cursor()

    #insert the records (as a list) to SQL database
    cursor.execute(statement, records)
    cursor.commit()

    #add time.sleep to ensure the data is added only once
    time.sleep(1)
    cursor.close()

    #if still connect after insert value then close the connection
    if connect.connected == 1:
        print("Connection closed")
        connect.close()
