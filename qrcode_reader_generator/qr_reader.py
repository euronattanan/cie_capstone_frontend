import cv2
from pyzbar.pyzbar import decode
from json_to_excel import json_to_excel
from json_to_excel import json_to_excel                                           

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3,480)
    cap.set(4,480)
    camera = True 
    while camera == True:
        _, frame = cap.read()
        for code in decode(frame):
            data = code.data.decode('utf-8')
            json_to_excel('test.csv', data)
            # print(data)
        cv2.imshow('Input',frame)

        if cv2.waitKey(1) == 27:
            break
if __name__== '__main__':
    main()
    