# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:26:04 2019

@author: Lee
"""

""" Goal is to take inputs from the import_geometry module and edit a blockmesh file template"""

def create_fuel_blocks(pt1x, pt2x):
    """Uses the geometric variables computed in assign_geomvars to create zones for the wood fuel zone:
       1) Rectangular fuel source
       2) centered along the flow axis of combustion chamber
       3) Half the width of the bottom of the chamber
       4) Assumed fuel wood height of 3 inches (0.0762 m)
       5) Assumed the bottom of the wood is 3 inches off of the ground (0.0762 m)
       6) pt17 is bottom left, pt18 is bottom right, pt19 is top right, pt20 is top left"""
    fuel_width = (pt2x - pt1x)/2
    fuel_x_center = fuel_width
    fuel_x_left_coord = fuel_x_center - (fuel_width)/2
    fuel_x_right_coord = fuel_x_center + (fuel_width)/2
    fuel_height = 0.0762 # [m]
    fuel_bottom_coords = 0.0762
    fuel_top_coords = fuel_bottom_coords + fuel_height
    pt17x = fuel_x_left_coord
    pt18x = fuel_x_right_coord
    pt19x = fuel_x_right_coord
    pt20x = fuel_x_left_coord
    pt17z = fuel_bottom_coords
    pt18z = fuel_bottom_coords
    pt19z = fuel_top_coords
    pt20z = fuel_top_coords
    pt17y = 0
    pt18y = 0
    pt19y = 0
    pt20y = 0
    return pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y


def fuel_vertice_strings(pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y):
    pt17xstr= str(pt17x)
    pt17zstr = str(pt17z)
    pt17ystr = str(pt17y)
    pt18xstr= str(pt18x)
    pt18zstr = str(pt18z)
    pt18ystr = str(pt18y)
    pt19xstr= str(pt19x)
    pt19zstr = str(pt19z)
    pt19ystr = str(pt19y)
    pt20xstr= str(pt20x)
    pt20zstr = str(pt20z)
    pt20ystr = str(pt20y)
    return pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr


def fuel_vertice_concatenate(pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y):
    """Use the same process as the previously written concatenating funciton"""
    pt17str = "(" + pt17xstr + " " + pt17zstr + " " + pt17ystr + ")"
    pt18str = "(" + pt18xstr + " " + pt18zstr + " " + pt18ystr + ")"
    pt19str = "(" + pt19xstr + " " + pt19zstr + " " + pt19ystr + ")"
    pt20str = "(" + pt20xstr + " " + pt20zstr + " " + pt20ystr + ")"
    return pt17str, pt18str, pt19str, pt20str

    
    
    