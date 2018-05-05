import cv2
import numpy

id=raw_input('Enter ID:')
face=cv2.CascadeClassifier('face.xml')
cap=cv2.VideoCapture(0)
cv2.waitKey(2000)
num=0
while True:
    ret, frame = cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
        faces=face.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3);
            cv2.imwrite('Resource/dataset.'+str(id)+'.'+str(num)+'.jpg',gray[y:y+h,x:x+h])
            cv2.waitKey(50)
            num+=1
        cv2.imshow('Frame',frame)
        if(num>30):
            break
    else:
        print('Cannot start the camera')    