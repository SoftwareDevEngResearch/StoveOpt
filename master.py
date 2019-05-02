# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:52:06 2019

@author: Lee
"""
"""Last test successful 4/26 12:19"""

"""The purpose of master.py is to call the functions in sequence from the varipus modules"""
from import_geometry import *
import os
import fileinput

""" Command line arguments:"""
# Import necessary packages
import sys
import argparse

# Construct the argument parse and parse the arguments
parser = argparse.ArgumentParser(description='Stove Optimization')
# File directory argument
parser.add_argument('-i', '--inputfile', required=True, help='path and filename for input.yaml')

args = parser.parse_args(sys.argv[1:])
print(args)
# Pull filename from args

# extract the excel filename and path from the input file--pass to locate geometry module
file_path = locate_geometry(args)
print("Here is your filepath!")
print(file_path)

# Extract geometry
pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt16x, pt16z, pt16y = extract_geometry(file_path) #unformatted list of (x,z,y) vertices

# vertice to strings
pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt16xstr, pt16zstr, pt16ystr = points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt16x, pt16z, pt16y)

# String concatenate
pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str = vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt16xstr, pt16zstr, pt16ystr)

"""Moving to blockmeshfile creation--will edit an existing template for a blockmesh file"""

from create_blockmeshfile import *

# Create fuel blocks
pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y = create_fuel_blocks(pt1x, pt2x)

# Convert wood zone coordinates to strings
pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr = fuel_vertice_strings(pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y)

# Concatenate the wood zone vertices
pt17str, pt18str, pt19str, pt20str = fuel_vertice_concatenate(pt17xstr, pt18xstr, pt19xstr, pt20xstr, pt17zstr, pt18zstr, pt19zstr, pt20zstr, pt17ystr, pt18ystr, pt19ystr, pt20ystr)

"""Moving forward assuming the filepath is known for the Stoveopt master directory
In the future, the path and filename will be an argument for the software provided by user in input file"""
path_StoveOpt_master = "C:/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/"
block_mesh_template_fname = "blockMeshDict_Template_reactionfoam_empty.txt"
dir_steps = "foamfiles/counterFlowFlame2D/system/"
runFolder = "run/"

# place template in system location if it doesn't already exist there
replace_template(path_StoveOpt_master,block_mesh_template_fname,dir_steps)

# Pull blockmesh template name
blockmeshfile = locate_blockmesh_template(path_StoveOpt_master,block_mesh_template_fname)

# Rename and relocate the blockmeshfile
saveName = update_blockmesh(blockmeshfile,runFolder)

rename_blockmesh(saveName,blockmeshfile)

edit_blockmesh_template(saveName, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str)

replace_template(path_StoveOpt_master,block_mesh_template_fname,dir_steps)
