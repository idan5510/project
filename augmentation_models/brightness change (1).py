# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:08:07 2022

@author: Student
"""

from PIL import Image, ImageEnhance

#read the image
im = Image.open('D:\\1.jpg')

#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)
factor = 0.6 #darkens the image
im_output1 = enhancer.enhance(factor)
im_output1.show()

factor = 1.2 #brightens the image
im_output1 = enhancer.enhance(factor)
im_output1.show('D:\\1.jpg')