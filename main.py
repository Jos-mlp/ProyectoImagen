import cv2
import numpy as np
import matplotlib.pyplot as plt

def voltearY(Matriz):
    f, c, p = Matriz.shape
    reflejar = np.zeros((f, c, p), int)
    for capa in range(0,p):
        for fila in range(0,f):
            reflejar[fila,:,capa] = Matriz[fila,::-1,capa]
    return reflejar
    

def voltearAH(Matriz):
    f, c, p = Matriz.shape
    rotar = np.zeros((c, f, p), int)
    reflejada = voltearY(Matriz)
    for capa in range(0, p):
        rotar[:,:,capa] = reflejada[:,:,capa].T
    return rotar

def voltear360(Matriz):
    f, c, p = Matriz.shape
    rotar = np.zeros((c, f, p), int)
    reflejada = voltearAH(Matriz)
    for capa in range(0, p):
        rotar[:,:,capa] = reflejada[:,::-1,capa].T
    return rotar

def recortar(Matriz,x,y):
    cortada = Matriz
    cortada = Matriz[y:,x:,:]
    return cortada

def dividir(Matriz,opcion=0):
    if (opcion==0):       
        a1,a2=np.split(Matriz,2)
    if (opcion==1):
       a1,a2=np.split(img,2,axis=1) 
    return a1,a2

def cambiarRGB():
    img = cv2.imread ( 'dj.jpg')
    # crea una imagen auxiliar de ceros
    img2 = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
    cv2.namedWindow('Imagen RGB')

    # crea las 4 trackbar
    cv2.createTrackbar('R','image',0,100,nothing)
    cv2.createTrackbar('G','image',0,100,nothing)
    cv2.createTrackbar('B','image',0,100,nothing)
    # creamos el switch on/off
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)
    while(1):
        cv2.imshow('image',img2)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        # obtinene la posicion
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')
        if s == 0:
            img2[:] = img[:]
        else:
            img2[:] = img[:]+[b,g,r]
    cv2.destroyAllWindows()


def sumarImagenes():
    img1 = cv2.imread ( 'dj.jpg')
    img2 = cv2.imread ( 'tigre.jpg')
    cv2.imshow('imagen1',img1)
    cv2.imshow('imagen2',img2)
    for i in range (0,600):
        for j in range (0,600):
            r=(int(img1[i][j][0]) + int(img2[i][j][0]))
            if(r>=255):
                img1[i][j][0] = 255
            else:
                img1[i][j][0] = r
            
            g = (int(img1[i][j][1]) + int(img2[i][j][1]))
            if(g>=255):
                img1[i][j][1] = 255
            else:
                img1[i][j][1] = g
            
            b=(int(img1[i][j][2]) + int(img2[i][j][2]))
            if(b>=255):
                img1[i][j][2] = 255
            else:
                img1[i][j][2] = b
           
    cv2.imshow('imagenes sumadas',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img = cv2.imread("tigre.jpg")
img2 = cv2.imread("dj.jpg")
#plt.axis([0, 600, 0, 600])


def nothing(x):
    pass





#Muestra los datos de la imagen
print(img.shape)
print(type(img))

#Imprime la imagen normal
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()


#Recorta la imagen
#(matriz,x,y)
recor = recortar(img,400,100)
plt.imshow(recor)
plt.show()


#(img,opcion)
#opcion=1 -> vertical
#opcion=vacio -> horizontal
#Imprime la imagen dividida a la mitad horizontal
a1,a2=dividir(img)
plt.imshow(a1)
plt.show()
plt.imshow(a2)
plt.show()
#Imprime la imagen dividida a la mitad vertical
a1,a2=dividir(img,1)
plt.imshow(a1)
plt.show()
plt.imshow(a2)
plt.show()


b1 = voltearY(img)
b2 = voltearAH(img)
b3 = voltear360(img)
plt.imshow(b1)
plt.show()
plt.imshow(b2)
plt.show()
plt.imshow(b3)
plt.show()

sumarImagenes()

cambiarRGB()