import cv2
from pyzbar.pyzbar import decode
from json_to_excel import json_to_excel
from json_to_sql import json_to_list                                       
from sql_variables import database_var, connection, insert_statement, insertRecord
import sys
import pypyodbc as odbc

#main function use to scan qr code
def main():
    #camera settings videocapture(0) means using webcam
    cap = cv2.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,480)
    camera = True 
    while camera == True:
        _, frame = cap.read()
        for code in decode(frame):
            #save the decoded data
            data = code.data.decode('utf-8')
            
            #insert the decoded data into SQL database
            insertRecord(connection, insert_statement, json_to_list(data))

        #this part shows the webcam footage    
        cv2.imshow('Input',frame)

        #if press "esc" key then the program will terminate
        if cv2.waitKey(1) == 27:
            break
        
if __name__== '__main__':
    main()
    