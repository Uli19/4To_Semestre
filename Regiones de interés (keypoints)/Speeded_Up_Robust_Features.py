import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inicializar el detector SURF
surf = cv2.xfeatures2d.SURF_create()

# Detectar puntos clave SURF
keypoints = surf.detect(gray, None)

# Dibujar puntos clave en la imagen
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# Mostrar la imagen con puntos clave
cv2.imshow('SURF Keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
