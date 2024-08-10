import cv2

# Cargar la imagen
image = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inicializar el detector FAST para encontrar puntos clave
fast = cv2.FastFeatureDetector_create()
keypoints = fast.detect(gray, None)

# Inicializar el extractor BRIEF para describir los puntos clave
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# Calcular descriptores BRIEF
keypoints, descriptors = brief.compute(gray, keypoints)

# Dibujar puntos clave en la imagen
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# Mostrar la imagen con puntos clave
cv2.imshow('BRIEF Keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
