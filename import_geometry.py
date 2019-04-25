# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:39:27 2019

@author: Lee
"""
import numpy
import tkinter as tk
from tkinter import filedialog
def locate_geometry():
    """ output the file location of stove geometry as a string"""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path == None:
        print("file path is not defined---null. Please retry")
    else: 
        print("File path successfully located")
        print(file_path)
    return file_path
       
import xlrd
def extract_geometry(file_path):
    """Pulling Data from excel workbook"""
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name('Outputs')
    pt1x = worksheet.cell(1,2).value
    pt1z = worksheet.cell(1,3).value
    pt1y = worksheet.cell(1,4).value
    pt2x = worksheet.cell(2,2).value
    pt2z = worksheet.cell(2,3).value
    pt2y = worksheet.cell(2,4).value
    pt3x = worksheet.cell(3,2).value
    pt3z = worksheet.cell(3,3).value
    pt3y = worksheet.cell(3,4).value
    pt4x = worksheet.cell(4,2).value
    pt4z = worksheet.cell(4,3).value
    pt4y = worksheet.cell(4,4).value
    pt5x = worksheet.cell(5,2).value
    pt5z = worksheet.cell(5,3).value
    pt5y = worksheet.cell(5,4).value
    pt6x = worksheet.cell(6,2).value
    pt6z = worksheet.cell(6,3).value
    pt6y = worksheet.cell(6,4).value
    pt7x = worksheet.cell(7,2).value
    pt7z = worksheet.cell(7,3).value
    pt7y = worksheet.cell(7,4).value
    pt8x = worksheet.cell(8,2).value
    pt8z = worksheet.cell(8,3).value
    pt8y = worksheet.cell(8,4).value
    pt9x = worksheet.cell(9,2).value
    pt9z = worksheet.cell(9,3).value
    pt9y = worksheet.cell(9,4).value
    pt10x = worksheet.cell(10,2).value
    pt10z = worksheet.cell(10,3).value
    pt10y = worksheet.cell(10,4).value
    pt11x = worksheet.cell(11,2).value
    pt11z = worksheet.cell(11,3).value
    pt11y = worksheet.cell(11,4).value
    pt12x = worksheet.cell(12,2).value
    pt12z = worksheet.cell(12,3).value
    pt12y = worksheet.cell(12,4).value
    pt13x = worksheet.cell(13,2).value
    pt13z = worksheet.cell(13,3).value
    pt13y = worksheet.cell(13,4).value
    pt14x = worksheet.cell(14,2).value
    pt14z = worksheet.cell(14,3).value
    pt14y = worksheet.cell(14,4).value
    pt15x = worksheet.cell(15,2).value
    pt15z = worksheet.cell(15,3).value
    pt15y = worksheet.cell(15,4).value
    pt16x = worksheet.cell(16,2).value
    pt16z = worksheet.cell(16,3).value
    pt16y = worksheet.cell(16,4).value
    if pt16z == 0:
        print("Top point has a 0 height value--error in data import")
    return pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt16x, pt16z, pt16y

def points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt16x, pt16z, pt16y):
    """ Take in the raw vertice information from spreadsheet, and format the floats into strings"""
    pt1xstr= str(pt1x)
    pt1zstr = str(pt1z)
    pt1ystr = str(pt1y)
    pt2xstr= str(pt2x)
    pt2zstr = str(pt2z)
    pt2ystr = str(pt2y)
    pt3xstr= str(pt3x)
    pt3zstr = str(pt3z)
    pt3ystr = str(pt3y)
    pt4xstr= str(pt4x)
    pt4zstr = str(pt4z)
    pt4ystr = str(pt4y)
    pt5xstr= str(pt5x)
    pt5zstr = str(pt5z)
    pt5ystr = str(pt5y)
    pt6xstr= str(pt6x)
    pt6zstr = str(pt6z)
    pt6ystr = str(pt6y)
    pt7xstr= str(pt7x)
    pt7zstr = str(pt7z)
    pt7ystr = str(pt7y)
    pt8xstr= str(pt8x)
    pt8zstr = str(pt8z)
    pt8ystr = str(pt8y)
    pt9xstr= str(pt9x)
    pt9zstr = str(pt9z)
    pt9ystr = str(pt9y)
    pt10xstr= str(pt10x)
    pt10zstr = str(pt10z)
    pt10ystr = str(pt10y)
    pt11xstr= str(pt11x)
    pt11zstr = str(pt11z)
    pt11ystr = str(pt11y)
    pt12xstr= str(pt12x)
    pt12zstr = str(pt12z)
    pt12ystr = str(pt12y)
    pt13xstr= str(pt13x)
    pt13zstr = str(pt13z)
    pt13ystr = str(pt13y)
    pt14xstr= str(pt14x)
    pt14zstr = str(pt14z)
    pt14ystr = str(pt14y)
    pt15xstr= str(pt15x)
    pt15zstr = str(pt15z)
    pt15ystr = str(pt15y)
    pt16xstr= str(pt16x)
    pt16zstr = str(pt16z)
    pt16ystr = str(pt16y)
    return pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt16xstr, pt16zstr, pt16ystr

def vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt16xstr, pt16zstr, pt16ystr): 
    """convert the individual vertex strings and concatenate to the format required for blockmeshdict file"""
    pt1str = "(" + pt1xstr + " " + pt1zstr + " " + pt1ystr + ")"
    pt2str = "(" + pt2xstr + " " + pt2zstr + " " + pt2ystr + ")"
    pt3str = "(" + pt3xstr + " " + pt3zstr + " " + pt3ystr + ")"
    pt4str = "(" + pt4xstr + " " + pt4zstr + " " + pt4ystr + ")"
    pt5str = "(" + pt5xstr + " " + pt5zstr + " " + pt5ystr + ")"
    pt6str = "(" + pt6xstr + " " + pt6zstr + " " + pt6ystr + ")"
    pt7str = "(" + pt7xstr + " " + pt7zstr + " " + pt7ystr + ")"
    pt8str = "(" + pt8xstr + " " + pt8zstr + " " + pt8ystr + ")"
    pt9str = "(" + pt9xstr + " " + pt9zstr + " " + pt9ystr + ")"
    pt10str = "(" + pt10xstr + " " + pt10zstr + " " + pt10ystr + ")"
    pt11str = "(" + pt11xstr + " " + pt11zstr + " " + pt11ystr + ")"
    pt12str = "(" + pt12xstr + " " + pt12zstr + " " + pt12ystr + ")"
    pt13str = "(" + pt13xstr + " " + pt13zstr + " " + pt13ystr + ")"
    pt14str = "(" + pt14xstr + " " + pt14zstr + " " + pt14ystr + ")"
    pt15str = "(" + pt15xstr + " " + pt15zstr + " " + pt15ystr + ")"
    pt16str = "(" + pt16xstr + " " + pt16zstr + " " + pt16ystr + ")"
    return pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str

def assign_geomvars(pt1z, pt16z, pt2x, pt1x):
    """pull required values, and assign locations for the wood combusiton zones (circles 2D)"""
    

        
    



    
    
    
