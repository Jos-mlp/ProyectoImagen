
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("tigre.jpg",1)
#plt.axis([0, 600, 0, 600])

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()