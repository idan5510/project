# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:21:59 2022

@author: Student
"""

import os
import cv2
os.getcwd()
collection = r"D:\car project\\"
for i, filename in enumerate(os.listdir(collection)):
    image = cv2.imread(r"D:\car project\\" + filename) 
    print(r"D:\car project\\" + filename) 
    h,w,c = image.shape
    new_size = (500,500)
    new_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR_EXACT)
    cv2.imwrite(r"D:\car project\ " + filename , new_image)
 