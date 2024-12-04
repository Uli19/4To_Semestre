import cv2
import numpy as np

face_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

if face_cascade.empty():
    raise IOError('No se pudo cargar el filtro')
if eye_cascade.empty():
    raise IOError('No se pudo cargar el filtro')

cap = cv2.VideoCapture(0)
ds_factor = 0.5

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (x_eye, y_eye, w_eye, h_eye) in eyes:
            center = (int(x_eye + 0.5 * w_eye),int(y_eye + 0.5 * h_eye))
            radius = int(0.3*(w_eye + h_eye))
            color = (0,0,255)
            thickness = 2
            cv2.circle(roi_color, center, radius, color, thickness)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('Detector de rostros y ojos', frame)
    c = cv2.waitKey(1)
    if  c == 27:
        break

cap.release()
cv2.destroyAllWindows()
