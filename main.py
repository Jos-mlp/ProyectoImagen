import numpy as np
import cv2 as cv

def nothing(x):
    pass


img = cv.imread (cv.samples.findFile("cr7.jpg"))
# crea una imagen auxiliar de ceros
img2 = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)

cv.namedWindow('Imagen RGB')


# crea las 4 trackbar
cv.createTrackbar('R','image',0,100,nothing)
cv.createTrackbar('G','image',0,100,nothing)
cv.createTrackbar('B','image',0,100,nothing)
# creamos el switch on/off
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)
while(1):
    cv.imshow('image',img2)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # obtinene la posicion
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img2[:] = img[:]
    else:
        img2[:] = img[:]+[b,g,r]
cv.destroyAllWindows()