
import cv2
import imageio
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

img = cv2.imread("tigre.jpg",1)
#plt.axis([0, 600, 0, 600])

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

#Imprime 
# crea una imagen en negro
imgNegra = np.zeros((512,512,3), np.uint8)
#Agrega un rectangulo a la imagen(cordenada 1 superior)(cordenada 2 superior)(Color rgb)(borde)
cv2.rectangle(imgNegra,(384,0),(510,128),(0,255,0),-1)
plt.imshow(imgNegra)
plt.show()