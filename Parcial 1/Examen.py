#Examen Procesamiento de Imagenes
# 
# Usando el código python que despliegue video de la cámara (visto en clase), modifiquelo para que permita entrada del teclado y realice las sig. acciones:
# 
#1.- Si presionas la letra ‘g’, el video deberá cambiar a escala de grises, si presionas ‘y’ el video cambiará al espacio de color YUV y si presionas ‘h’ el video cambiará al espacio de color HSV.
#2.- Para regresar al modo normal (BGR) presionar 'n'.
#3.- Para salir debe presionar ‘q’ o ‘x’.

import cv2
    
cap = cv2.VideoCapture(0)

color_mode = 'bgr' 

while True:

    ret, frame = cap.read()

    if color_mode == 'gray':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif color_mode == 'yuv':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    elif color_mode == 'hsv':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    cv2.imshow('Camara', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('g'):
        color_mode = 'gray'
    elif key == ord('y'):
        color_mode = 'yuv'
    elif key == ord('h'):
        color_mode = 'hsv'
    elif key == ord('n'):
        color_mode = 'bgr'
    elif key == ord('q') or key == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()