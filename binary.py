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
cuml = 0
#print(i)
#print(j)

#print(img[0,0])
 
fin_img = img

while (a<i):
    while (b<j):
        val = img[b,a]
        I[0,val] = I[0,val] + 1
        b = b + 1
    a = a + 1
    b = 0

# print(I)
ctr = 0

while (ctr<=255):
    cuml = cuml + I[0,ctr]
    if cuml>=i*j/2:
        break
    ctr = ctr + 1

a = 0
b = 0

print(cuml)
print(ctr)

cv2.imshow('image', img)

blk = 0
wht = 0

while (a<i):
    while (b<j):
        if (img[b,a]<=ctr):
            fin_img[b,a] = 0
            wht = wht + 1
        elif (img[b,a]>ctr):
            fin_img[b,a] = 255
            blk = blk + 1
        b = b + 1
    a = a + 1
    b = 0

cv2.imshow('50-50 image', fin_img)

print(wht)
print(blk)

cv2.waitKey(0)

cv2.imwrite('Prob4_1.png', fin_img)

""" a = 0
img2 = img

while (a<i):
    while (b<j):
        if (img[b,a]<=64 or (img[b,a]>=128 and img[b,a]<192)):
            img2[b,a] = 0
        elif ((img[b,a]>64 and img[b,a]<128) or (img[b,a]>=192 and img[b,a]<=255)):
            img2[b,a] = 255
        b = b + 1
    a = a + 1
    b = 0
 """
cv2.imshow('final image', img2)

cv2.waitKey(0)

#hist = cv2.calcHist([img],[0],None,[256],[0,256])

#plt.hist(img.ravel(),256,[0,256]); plt.show()