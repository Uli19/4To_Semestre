import cv2
for x in dir(cv2): 
    if x.startswith('COLOR_'):
        print(x)
img = cv2.imread("./CUBOREDUCIDO.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('CUBOENGRIS', img2)
cv2.waitKey()