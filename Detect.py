import cv2
import numpy
from database_conn import database
db=database()


face=cv2.CascadeClassifier('face.xml')
cap=cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer()
rec.load('trainingdata.yml')

font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
id=0
while True:
    ret, frame = cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
        faces=face.detectMultiScale(gray,1.2,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3);
            id, conf=rec.predict(gray[y:y+h,x:x+w]);
            rows=db.display(id)
            id_ , name, age=rows[0]
            cv2.cv.PutText(cv2.cv.fromarray(frame),str('Name:'+name),(x,y+h+20),font,(0,0,255))
            cv2.cv.PutText(cv2.cv.fromarray(frame),str('Age:'+str(age)),(x,y+h+40),font,(0,0,255))

        cv2.imshow('Frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        print('Cannot start the camera')    