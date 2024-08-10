import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #video = cv2.resize(frame,(0,0),fx=0.5,fy=0.5);
        #video2 = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Camara', frame)#video2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break    
    else:
        break
cap.release()
cv2.destroyAllWindows