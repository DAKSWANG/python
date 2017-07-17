# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
img = cv2.imread('pic.jpg', 3)
cv2.imshow('pic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = np.zeros((512,512), np.uint8) #生成一个空灰度图像
cv2.line(img,(0,0),(511,511),255,5)
plt.imshow(img,'gray')
'''

#img = np.zeros((512,512,3),np.uint8)#生成一个空彩色图像
#img = cv2.imread('pic.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = plt.imread('pic.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

cv2.line(img,(0,0),(511,511),(0,255,0),5)

cv2.imshow('RGB',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img,'brg')