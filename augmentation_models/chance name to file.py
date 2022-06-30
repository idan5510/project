# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:25:38 2022

@author: Student
"""
import os
#chance name to files:

os.getcwd()
collection = r"D:\car project"
for i, filename in enumerate(os.listdir(collection)):    
    number_str = str(i)
    zero_filled_number = number_str.zfill(6)
    os.rename(r"D:\car project\\" + filename, r"D:\car project\\" + zero_filled_number + ".jpg")











