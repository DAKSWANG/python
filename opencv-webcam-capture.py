# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:12:55 2017

@author: DAKS
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
   # Capture frame-by-frame
   ret, frame = cap.read()
   
   # 轉灰階
   #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
   # 上下倒轉
   #frame = cv2.flip(frame, 0)
   
   # 顯示影像，按 q 結束
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()