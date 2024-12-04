import cv2
import numpy as np
cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print("Error Al leer la camara!!!!")
frame_width = int(cap.get(3))
frame_heigth = int(cap.get(4))
out = cv2.VideoWriter('Video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),70,(frame_width, frame_heigth)) 

while(True):
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('Cuafro',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()