import cv2
import numpy as np

# img = cv2.imread("flor.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("flor.jpg")
cv2.imshow("Flor Original", img)
print(img.shape)

img_crop = img[80:280, 150:330]
cv2.imshow("Imagen Recortada", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()