import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inicializar el detector FAST
fast = cv2.FastFeatureDetector_create()

# Detectar puntos clave FAST
keypoints = fast.detect(gray, None)

# Dibujar puntos clave en la imagen
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# Mostrar la imagen con puntos clave
cv2.imshow('FAST Keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
