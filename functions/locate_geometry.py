# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:34:37 2019

@author: Lee
"""
"""User inputs--what is the directory of the file with stove geometry data, what is the filename"""
file_path = "C:\Oregon_State\Spring_2019\Soft_dev_eng\StoveOpt\stovegeom"
file_name = "Stove_Geometry"

import os
def locate_geometry():
    filelocation = os.path.join(file_path, file_name)
    print(filelocation)
    return filelocation
print(filelocation)


