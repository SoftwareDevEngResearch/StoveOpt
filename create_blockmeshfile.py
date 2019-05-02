# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:26:04 2019

@author: Lee
"""

""" Goal is to take inputs from the import_geometry module and edit a blockmesh file template"""
import shutil
from shutil import copyfile

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
    pt17xstr= str(pt17x)[:5]
    pt17zstr = str(pt17z)[:5]
    pt17ystr = str(pt17y)[:5]
    pt18xstr= str(pt18x)[:5]
    pt18zstr = str(pt18z)[:5]
    pt18ystr = str(pt18y)[:5]
    pt19xstr= str(pt19x)[:5]
    pt19zstr = str(pt19z)[:5]
    pt19ystr = str(pt19y)[:5]
    pt20xstr= str(pt20x)[:5]
    pt20zstr = str(pt20z)[:5]
    pt20ystr = str(pt20y)[:5]
    return pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr


def fuel_vertice_concatenate(pt17xstr, pt18xstr, pt19xstr, pt20xstr, pt17zstr, pt18zstr, pt19zstr, pt20zstr, pt17ystr, pt18ystr, pt19ystr, pt20ystr):
    """Use the same process as the previously written concatenating funciton"""
    pt17str = "(" + pt17xstr + " " + pt17zstr + " " + pt17ystr + ")"
    pt18str = "(" + pt18xstr + " " + pt18zstr + " " + pt18ystr + ")"
    pt19str = "(" + pt19xstr + " " + pt19zstr + " " + pt19ystr + ")"
    pt20str = "(" + pt20xstr + " " + pt20zstr + " " + pt20ystr + ")"
    return pt17str, pt18str, pt19str, pt20str

"""Moving forward assuming the filepath is known for the Stoveopt master directory
In the future, the path and filename will be an argument for the software provided by user in input file"""
path_StoveOpt_master = "C:/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/"
block_mesh_template_fname = "blockMeshDict_Template_reactionfoam_empty.txt"
dir_steps = "foamfiles/counterFlowFlame2D/system/"

def locate_blockmesh_template(path_StoveOpt_master,block_mesh_template_fname):
    """the function uses the StoveOpt path and blockmesh template name to open the blockMeshDict file for editting"""
    blockmeshfile = path_StoveOpt_master + dir_steps + block_mesh_template_fname # location and path name of blockmesh template
    print(blockmeshfile)
    f = open(blockmeshfile,"r")
    print(f.read())
    f.close()
    return blockmeshfile

def update_blockmesh(blockmeshfile,runFolder):
    """Used to rename the blockmesh file, and rellocate to the run folder"""
    with open(blockmeshfile,'r') as f:
        # Save file with iterative name here
        saveLocation = path_StoveOpt_master + dir_steps + runFolder
        saveFileName = "blockMeshDict_01.txt" # Will need to be updated to save iteratively
        saveName = saveLocation + saveFileName
        f.close()
    return saveName

def rename_blockmesh(saveName,blockmeshfile):
    """Moving the file and renaming--Need to add an existence check"""
    exists = os.path.isfile(saveName)
    if exists:
        print("blockmeshfile for run already exists")
    else:
        os.rename(blockmeshfile,saveName)

import os
def edit_blockmesh_template(saveName, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str):
    """open the blockmeshtemplate for edit, locate the positions needed, and overwrite the vertice lines"""
    # 703  is where  the cursor is immediately before the pt1 string
    with open(saveName, 'r+') as f:
        f.seek(649) #pt1
        f.write(pt1str +'\n')
        f.write(pt2str+'\n')
        f.write(pt3str+'\n')
        f.write(pt4str+'\n')
        f.write(pt5str+'\n')
        f.write(pt6str+'\n')
        f.write(pt7str+'\n')
        f.write(pt8str+'\n')
        f.write(pt9str+'\n')
        f.write(pt10str+'\n')
        f.write(pt11str+'\n')
        f.write(pt12str+'\n')
        f.write(pt13str+'\n')
        f.write(pt14str+'\n')
        f.write(pt15str+'\n')
        f.write(pt16str+'\n')
        f.write(pt17str+'\n')
        f.write(pt18str+'\n')
        f.write(pt19str+'\n')
        f.write(pt20str+'\n')
        f.close()


def replace_template(path_StoveOpt_master,block_mesh_template_fname,dir_steps):
    """Move the template from the backup folder into the system folder for future edits"""
    templateFile = path_StoveOpt_master + dir_steps + "backup/" + block_mesh_template_fname # template path/name
    print(templateFile)
    newFile = path_StoveOpt_master + dir_steps + block_mesh_template_fname # template path/name minus the backup folder
    print(newFile)
    exists = os.path.isfile(newFile)
    if exists:
        print("template already in location")
    else:
        copyfile(templateFile,newFile)






    
    
    