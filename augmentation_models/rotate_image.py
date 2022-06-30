# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:43:59 2022

@author: dina
"""

import cv2

image_resized = cv2.imread(r'C:\Users\idan\Desktop\resized_roze.jpg')
h, w, c = image_resized.shape
print("resized Height and Width:", h,"x", w)


#rotate matrix from the center of the image size
rotate_matrix = cv2.getRotationMatrix2D(center=(h//2, w//2), angle = 15, scale = 1)
#rotate the image using cv2.warpAffine
image_rotated_15_angle = cv2.warpAffine(src = image_resized,
                                        M = rotate_matrix, 
                                        dsize = (w, h))
#image_rotated_arranged = cv2.resize(image_rotated_45_angle, (w, h), interpolation=cv2.INTER_LINEAR_EXACT)

cv2.imshow("image resized", image_resized)
cv2.imshow("image rotated 15 angles", image_rotated_15_angle)

cv2.waitKey(0)

cv2.imwrite(r'C:\Users\dina\Desktop\rotated.jpg',image_rotated_15_angle)


