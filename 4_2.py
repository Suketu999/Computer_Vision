import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("cv_ss_0.png",0)

#dimensions = img.shape
I = np.zeros((1,255))

a = 0
b = 0

i = img.shape[1]
j = img.shape[0]

#cv2.imshow('image', img)

#cv2.waitKey(0)

############################### EXPLANATION ######################################
### THE ENTIRE RANGE OF VALUES OF THE HISTOGAM, FROM 0 TO 255 IS DIVIDED INTO
### 4 CLASSES - 0 TO 64, 64 TO 128, 129 TO 192 AND 193 TO 255. THE PIXEL FALLING
### IN EITHER OF THE 1ST OR 3RD CLASS ARE ASSIGNED TO BE BLACK (0) AND THE PIXELS
### FALLING IN 2ND OR 4TH CLASS ARE ASSIGNED TO BE WHITE (255).
###################################################################################

while (a<i):
    while (b<j):
        if (img[b,a]<=64 or (img[b,a]>128 and img[b,a]<=192)):
            img[b,a] = 0
        elif ((img[b,a]>64 and img[b,a]<=128) or (img[b,a]>128 and img[b,a]<=255)):
            img[b,a] = 255
        b = b+1
    b = 0
    a=a+1

cv2.imshow('image', img)

cv2.imwrite('Prob4_2.png', img)

cv2.waitKey(0)
