# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:26:04 2019

@author: Lee
"""

""" Goal is to take inputs from the import_geometry module and edit a blockmesh file template"""
import shutil
from shutil import copyfile

"""Moving forward assuming the filepath is known for the Stoveopt master directory
In the future, the path and filename will be an argument for the software provided by user in input file"""
path_StoveOpt_master = "C:/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/"
block_mesh_template_fname = "blockMeshDict_Template_reactionfoam_empty" #No file type
dir_steps = "foamfiles/counterFlowFlame2D/system/"

def locate_blockmesh_template(path_StoveOpt_master,block_mesh_template_fname):
    """the function uses the StoveOpt path and blockmesh template name to open the 
    template version of the blockMeshDict file for editing in the system folder"""
    blockmesh_template = path_StoveOpt_master + dir_steps + block_mesh_template_fname # location and path name of blockmesh template
    print(blockmesh_template)
    f = open(blockmesh_template,"r")
    #print(f.read())
    print("located template file in system folder")
    f.close()
    system_folder = path_StoveOpt_master + dir_steps
    return blockmesh_template, system_folder

def update_blockmesh(blockmesh_template, system_folder):
    """Used to create (but not assign) a new name for the blockmesh file saving name to the blockMeshDict required for running--in the system folder"""
    with open(blockmesh_template,'r') as f:
        # Save file with iterative name here (this is for future development..?)
        saveLocation = system_folder
        saveFileName = "blockMeshDict" # Will need to be updated to save iteratively
        saveName = saveLocation + saveFileName
        f.close()
    return saveName

def rename_blockmesh(saveName, blockmesh_template):
    """Moving the file and renaming--Need to add an existence check"""
    exists = os.path.isfile(saveName) # Will exist if a file named blockMeshDict is already in the location
    if exists:
        # Probably should either delete the current file there, or move it to obselete
        print("blockmeshfile for run already exists--moving to obselete")
        # Still need to put this functionality in
    else:
        os.rename(blockmesh_template, saveName)

import os
def edit_blockmesh_template(saveName, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str):
    """open the blockmeshtemplate for edit, locate the positions needed, and overwrite the vertice lines"""
    # 703  is where  the cursor is immediately before the pt1 string
    with open(saveName, 'r+') as f:
        f.seek(639) #pt1
        f.write(pt0str +'\n')
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
        f.write(pt21str+'\n')
        f.write(pt22str +'\n')
        f.write(pt23str +'\n')
        f.write(pt24str+'\n')
        f.write(pt25str+'\n')
        f.write(pt26str+'\n')
        f.write(pt27str+'\n')
        f.write(pt28str+'\n')
        f.write(pt29str+'\n')
        f.write(pt30str+'\n')
        f.write(pt31str+'\n')
        f.write(pt32str+'\n')
        f.write(pt33str+'\n')
        f.write(pt34str+'\n')
        f.write(pt35str+'\n')
        f.write(pt36str+'\n')
        f.write(pt37str+'\n')
        f.write(pt38str+'\n')
        f.write(pt39str+'\n')
        f.write(pt40str+'\n')
        f.write(pt41str+'\n')
        f.write(pt42str+'\n')
        f.write(pt43str+'\n')
        f.write(pt44str+'\n')
        f.write(pt45str+'\n')
        f.write(pt46str+'\n')
        f.write(pt47str+'\n')
        f.close()
        
# This should be run after the blockmesh and CFD case have been excecuted
def replace_template(path_StoveOpt_master, block_mesh_template_fname, dir_steps):
    """Move the template from the backup folder into the system folder for future edits
    Does not excecute if the template file is already there"""
    templateFile = path_StoveOpt_master + dir_steps + "backup/" + block_mesh_template_fname # template path/name
    print(templateFile)
    newFile = path_StoveOpt_master + dir_steps + block_mesh_template_fname # template path/name minus the backup folder
    print(newFile)
    exists = os.path.isfile(newFile)
    if exists:
        print("template already in location")
    else:
        copyfile(templateFile,newFile)






    
    
    