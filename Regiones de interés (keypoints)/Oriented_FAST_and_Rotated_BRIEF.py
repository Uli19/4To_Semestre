import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inicializar el detector ORB
orb = cv2.ORB_create()

# Detectar puntos clave ORB
keypoints = orb.detect(gray, None)

# Calcular descriptores ORB
keypoints, descriptors = orb.compute(gray, keypoints)

# Dibujar puntos clave en la imagen
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# Mostrar la imagen con puntos clave
cv2.imshow('ORB Keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
