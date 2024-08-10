import cv2
import numpy as np

left_ear_cascade = \
    cv2.CascadeClassifier\
        ('haarcascade_mcs_leftear.xml')
right_ear_cascade = \
    cv2.CascadeClassifier\
        ('haarcascade_mcs_rightear.xml')
if left_ear_cascade.empty():
    raise IOError('No se pudo cargar el archivo xml')
img = cv2.imread('foto.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

left_ear = left_ear_cascade.detectMultiScale(gray, 1.3,5)
right_ear = right_ear_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h) in left_ear:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3)
for(x,y,w,h) in right_ear:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),3)
    
cv2.imshow('Deteccion de orejas', img)
cv2.waitKey()
cv2.destroyAllWindows()