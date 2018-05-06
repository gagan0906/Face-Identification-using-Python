import cv2
import numpy
from database_conn import database

db=database()

id=raw_input('Enter ID:')
if(db.checkid(id)!=[]):
    print('This ID already exits')
    exit()

name=raw_input('\nEnter Name')
age=int(raw_input('\nEnter Age'))
face=cv2.CascadeClassifier('face.xml')
cap=cv2.VideoCapture(0)
cv2.waitKey(4000)
num=0
while True:
    ret, frame = cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
        faces=face.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3);
            cv2.imwrite('Resource/dataset.'+str(id)+'.'+str(num)+'.jpg',gray[y:y+h,x:x+h])
            cv2.waitKey(100)
            num+=1
        cv2.imshow('Frame',frame)
        if(num>50):
            db.insert(id,name,age)
            print('Inserted Successfully')
            break
    else:
        print('Cannot start the camera')    