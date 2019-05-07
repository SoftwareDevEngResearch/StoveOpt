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
pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt0x, pt0z, pt0y = extract_geometry(file_path) #unformatted list of (x,z,y) vertices

# Create Fuel Blocks
pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y = create_fuel_blocks(pt0x, pt1x)

# Create additional front points
pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y = create_additional_front_points(pt6x, pt14z, pt7x, pt15z, pt14x, pt9z, pt15x, pt8z)

# convert front points to strings
pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr = points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt0x, pt0z, pt0y, pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y)

# concatenate all front point strings
pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt44str, pt46str = vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr)


# Create concatenated strings for the back points
shift = 0.1
pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt45str, pt47str = create_back_points(shift, pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr)

"""
# Create Face points
pt21x, pt21z, pt21y, pt22x, pt22z, pt22y = create_face_points(pt7x, pt15z, pt8x, pt16z)
# vertice to strings
pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt16xstr, pt16zstr, pt16ystr, pt21xstr, pt21zstr, pt21ystr, pt22xstr, pt22zstr, pt22ystr = points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt16x, pt16z, pt16y, pt21x, pt21z,  pt21y, pt22x, pt22z, pt22y)
# String concatenate
pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt21str, pt22str = vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt16xstr, pt16zstr, pt16ystr, pt21xstr, pt21zstr, pt21ystr, pt22xstr, pt22zstr, pt22ystr)
"""

"""Moving to blockmeshfile creation--will edit an existing template for a blockmesh file"""
from create_blockmeshfile import *
"""
# Create fuel blocks
pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y = create_fuel_blocks(pt1x, pt2x)

# Convert wood zone coordinates to strings
pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr = fuel_vertice_strings(pt17x, pt18x, pt19x, pt20x, pt17z, pt18z, pt19z, pt20z, pt17y, pt18y, pt19y, pt20y)

# Concatenate the wood zone vertices
pt17str, pt18str, pt19str, pt20str = fuel_vertice_concatenate(pt17xstr, pt18xstr, pt19xstr, pt20xstr, pt17zstr, pt18zstr, pt19zstr, pt20zstr, pt17ystr, pt18ystr, pt19ystr, pt20ystr)
"""

"""Moving forward assuming the filepath is known for the Stoveopt master directory
In the future, the path and filename will be an argument for the software provided by user in input file"""
path_StoveOpt_master = "C:/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/"
block_mesh_template_fname = "blockMeshDict_Template_reactionfoam_empty"
dir_steps = "foamfiles/counterFlowFlame2D/system/"
saveName = path_StoveOpt_master + dir_steps + "blockMeshDict" # This is what the file needs to be called and where it needs to be placed for meshing

# place template in system location if it doesn't already exist there
replace_template(path_StoveOpt_master, block_mesh_template_fname, dir_steps)

# Pull blockmesh template name
blockmesh_template, system_folder = locate_blockmesh_template(path_StoveOpt_master,block_mesh_template_fname)

# Rename and relocate the blockmeshfile
saveName = update_blockmesh(blockmesh_template, system_folder)

rename_blockmesh(saveName, blockmesh_template)

edit_blockmesh_template(saveName, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str)

replace_template(path_StoveOpt_master, block_mesh_template_fname, dir_steps)
