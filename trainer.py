import cv2
import numpy as np
import os
from PIL import Image
recognizer=cv2.createLBPHFaceRecognizer()
#recognizer = cv2.face.createLBPHFaceRecognizer()
path='Resource'

def getImagePath(path):
    imagepath=[os.path.join(path, i) for i in os.listdir(path)]
    faces=[]
    ids=[]
    for image in imagepath:
        faceImg=Image.open(image)
        faceNp=np.array(faceImg,'uint8')
        id=int(os.path.split(image)[-1].split('.')[1])
       
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow('training',faceNp)
        cv2.waitKey(10)
    return ids,faces    
ids,faces=getImagePath(path)    
recognizer.train(faces,np.array(ids))
recognizer.save('trainingdata.yml')
cv2.destroyAllWindows()