# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:26:04 2019

@author: Lee
"""

""" Goal is to take inputs from the import_geometry module and edit a blockmesh file template"""
import shutil
from shutil import copyfile
from shutil import copy
import os


def locate_blockmesh_template():
    """the function uses the StoveOpt path and blockmesh template name to open the
    template version of the blockMeshDict file for editing in the system folder

    Args:
    None

    Returns:
    blockmesh_template (str): full file path where blockmesh template lives


    """
    # Current working dir for stove opt master
    path_StoveOpt_master = os.getcwd()
    # Steps to system folder
    dir_steps = "//blockMeshDict_foamfile//template//blockMeshDict_template"
    blockmesh_template = path_StoveOpt_master + dir_steps # location and path name of blockmesh template
    print("blockmesh template located at:")
    print(blockmesh_template)
    return blockmesh_template

#blockmesh_template = locate_blockmesh_template()



def compute_num_cells(max_delta_x, pt_0_y, pt_1_y):
    """compute the number of blocks associated with the max_delta_x for the largest spatial step (combustion chamber)

    Args:
    max_delta_x (double): User defined maximum grid spacing.
    pt0x (double): x-coordinate of bottom LHS cookstove combustion chamber
    pt1x (double): x-coordinate of bottom RHS cookstove combustion chamber


    Returns:
    num_cells_int (int): number of cells to be written to the openfoam blockmesh file for entire domain
    num_cells_double (double): number of cells to be written to the openfoam blockmesh file for entire domain BEFORE INT ROUNDING
    num_cells_int_str (str): number of cells to be written to the openfoam blockmesh file for entire domain, converted to string type for f.write
    num_cells_int_str_concat (str): cells formatted for OF
    """

    max_space = abs(pt_1_y-pt_0_y) # maximum spatial step in domain defined by coordinates
    num_cells_double = max_space/max_delta_x # unrounded number of cells per block
    num_cells_int = int(round(num_cells_double)) # round to integer value
    num_cells_int_str = str(num_cells_int)
    num_cells_int_str_concat = "(" + num_cells_int_str + " " + num_cells_int_str + " " + num_cells_int_str + ")"

    print("num cells int")
    print(num_cells_int)

    print("num cells int converted to str")
    print(num_cells_int_str)

    print("num cells int str concat")
    print(num_cells_int_str_concat)
    return num_cells_int, num_cells_double, num_cells_int_str, num_cells_int_str_concat

#num_cells_int, num_cells_double, num_cells_int_str, num_cells_int_str_concat = compute_num_cells(max_delta_x, pt0x, pt1x)



def write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str, pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str, pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str):
    """Open the blockmesh template, edit and move to the Run folder
    Args:
    vertices defined as strings
    blockmesh_template (str): full file path where blockmesh template lives

    Returns:
    block_mesh_run_path (str): file path with the blockmesh file saved for running cases
    """
    with open(blockmesh_template,'r+') as f:
            f.seek(602) #where writing begins
            f.write("convertToMeters 1;"+"\n")
            f.write("\n")
            f.write("vertices"+"\n")
            f.write("("+"\n")

            # Write vertice strings
            f.write(pt_0_str +'\n')
            f.write(pt_1_str +'\n')
            f.write(pt_2_str+'\n')
            f.write(pt_3_str+'\n')
            f.write(pt_4_str+'\n')
            f.write(pt_5_str+'\n')
            f.write(pt_6_str+'\n')
            f.write(pt_7_str+'\n')
            f.write(pt_8_str+'\n')
            f.write(pt_9_str+'\n')
            f.write(pt_10_str+'\n')
            f.write(pt_11_str+'\n')
            f.write(pt_12_str+'\n')
            f.write(pt_13_str+'\n')
            f.write(pt_14_str+'\n')
            f.write(pt_15_str+'\n')
            f.write(pt_16_str+'\n')
            f.write(pt_17_str+'\n')
            f.write(pt_18_str+'\n')
            f.write(pt_19_str+'\n')
            f.write(pt_20_str+'\n')
            f.write(pt_21_str+'\n')
            f.write(pt_22_str+'\n')
            f.write(pt_23_str+'\n')
            f.write(pt_24_str+'\n')
            f.write(pt_25_str+'\n')
            f.write(pt_26_str+'\n')
            f.write(pt_27_str+'\n')
            f.write(pt_28_str+'\n')
            f.write(pt_29_str+'\n')
            f.write(pt_30_str+'\n')
            f.write(pt_31_str+'\n')
            f.write(pt_32_str+'\n')
            f.write(pt_33_str+'\n')
            f.write(pt_34_str+'\n')
            f.write(pt_35_str+'\n')
            f.write(pt_36_str+'\n')
            f.write(pt_37_str+'\n')
            f.write(pt_38_str+'\n')
            f.write(pt_39_str+'\n')
            f.write(pt_40_str+'\n')
            f.write(pt_41_str+'\n')
            f.write(pt_42_str+'\n')
            f.write(pt_43_str+'\n')
            f.write(pt_44_str+'\n')
            f.write(pt_45_str+'\n')
            f.write(pt_46_str+'\n')
            f.write(pt_47_str+'\n')
            f.write(pt_48_str+'\n')
            f.write(pt_49_str+'\n')
            f.write(pt_50_str+'\n')
            f.write(pt_51_str+'\n')
            f.write(pt_52_str+'\n')
            f.write(pt_53_str+'\n')
            f.write(pt_54_str+'\n')
            f.write(pt_55_str+'\n')
            f.write(pt_56_str+'\n')
            f.write(pt_57_str+'\n')
            f.write(pt_58_str+'\n')
            f.write(pt_59_str+'\n')
            f.write(pt_60_str+'\n')
            f.write(pt_61_str+'\n')
            f.write(pt_62_str+'\n')
            f.write(pt_63_str+'\n')
            f.write(pt_64_str+'\n')
            f.write(pt_65_str+'\n')
            f.write(pt_66_str+'\n')
            f.write(pt_67_str+'\n')
            f.write(pt_68_str+'\n')
            f.write(pt_69_str+'\n')
            f.write(pt_70_str+'\n')
            f.write(pt_71_str+'\n')
            f.write(pt_72_str+'\n')
            f.write(pt_73_str+'\n')
            f.write(pt_74_str+'\n')
            f.write(pt_75_str+'\n')
            f.write(pt_76_str+'\n')
            f.write(pt_77_str+'\n')
            f.write(pt_78_str+'\n')
            f.write(pt_79_str+'\n')
            f.write(pt_80_str+'\n')
            f.write(pt_81_str+'\n')
            f.write(pt_82_str+'\n')
            f.write(pt_83_str+'\n')
            f.write(pt_84_str+'\n')
            f.write(pt_85_str+'\n')
            f.write(pt_86_str+'\n')
            f.write(pt_87_str+'\n')
            f.write(pt_88_str+'\n')
            f.write(pt_89_str+'\n')
            f.write(pt_90_str+'\n')
            f.write(pt_91_str+'\n')
            f.write(pt_92_str+'\n')
            f.write(pt_93_str+'\n')
            f.write(pt_94_str+'\n')
            f.write(pt_95_str+'\n')
            f.write(pt_96_str+'\n')
            f.write(pt_97_str+'\n')
            f.write(pt_98_str+'\n')
            f.write(pt_99_str+'\n')
            f.write(pt_100_str+'\n')
            f.write(pt_101_str+'\n')
            f.write(pt_102_str+'\n')
            f.write(pt_103_str+'\n')
            f.write(pt_104_str+'\n')
            f.write(pt_105_str+'\n')
            f.write(pt_106_str+'\n')
            f.write(pt_107_str+'\n')
            f.write(pt_108_str+'\n')
            f.write(pt_109_str+'\n')
            f.write(pt_110_str+'\n')
            f.write(pt_111_str+'\n')
            f.write(pt_112_str+'\n')
            f.write(pt_113_str+'\n')
            f.write(pt_114_str+'\n')
            f.write(pt_115_str+'\n')
            f.write(pt_116_str+'\n')
            f.write(pt_117_str+'\n')
            f.write(pt_118_str+'\n')
            f.write(pt_119_str+'\n')
            f.write(pt_120_str+'\n')
            f.write(pt_121_str+'\n')
            f.write(pt_122_str+'\n')
            f.write(pt_123_str+'\n')
            f.write(pt_124_str+'\n')
            f.write(pt_125_str+'\n')
            f.write(pt_126_str+'\n')
            f.write(pt_127_str+'\n')
    	    f.write(pt_128_str+'\n')
            f.write(pt_129_str+'\n')
            f.write(pt_130_str+'\n')
            f.write(pt_131_str+'\n')
            f.write(pt_132_str+'\n')
            f.write(pt_133_str+'\n')
            f.write(pt_134_str+'\n')
            f.write(pt_135_str+'\n')
            f.write(pt_136_str+'\n')
            f.write(pt_137_str+'\n')
            f.write(pt_138_str+'\n')
            f.write(pt_139_str+'\n')
            f.write(pt_140_str+'\n')
            f.write(pt_141_str+'\n')
            f.write(pt_142_str+'\n')
            f.write(pt_143_str+'\n')
            f.write(pt_144_str+'\n')
            f.write(pt_145_str+'\n')
            f.write(pt_146_str+'\n')
            f.write(pt_147_str+'\n')
            f.write(pt_148_str+'\n')
    	    f.write(pt_149_str+'\n')
            f.write(pt_150_str+'\n')
            f.write(pt_151_str+'\n')
            f.write(pt_152_str+'\n')
            f.write(pt_153_str+'\n')
            f.write(pt_154_str+'\n')
            f.write(pt_155_str+'\n')
            f.write(pt_156_str+'\n')
            f.write(pt_157_str+'\n')
            f.write(pt_158_str+'\n')
            f.write(pt_159_str+'\n')


            f.write("\n")
            f.write(");"+"\n")
            f.write("\n")
            f.write("blocks"+"\n")
            f.write("(")
            f.write("\n")

            # write the blocks, with
            #f.write("hex (16 17 39 38 19 18 40 41) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (0 26 32 22 44 70 76 66) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (26 27 142 140 70 71 143 141) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (27 28 34 33 71 72 78 77) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (28 29 150 148 72 73 151 149) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (29 30 36 35 73 74 80 79) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (30 31 158 156 74 75 159 157) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (31 1 23 37 75 45 67 81) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (22 140 136 24 66 141 137 68) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (32 33 39 38 76 77 83 82) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (142 148 144 138 143 149 145 139) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (34 35 41 40 78 79 85 84) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (150 156 152 146 151 157 153 147) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (36 37 43 42 80 81 87 86) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (158 23 25 154 159 67 69 155) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (24 38 88 2 68 82 112 46) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (136 138 89 88 137 139 113 112) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (39 40 90 89 83 84 114 113) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (144 146 91 90 145 147 115 114) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (41 42 92 91 85 86 116 115) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (152 154 93 92 153 155 117 116) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (43 25 3 93 87 69 47 117) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (2 88 94 4 46 112 118 48) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")

            f.write("hex (88 89 95 94 112 113 119 118) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (89 90 96 95 113 114 120 119) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (90 91 97 96 114 115 121 120) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (91 92 98 97 115 116 122 121) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (92 93 99 98 116 117 123 122) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (93 3 5 99 117 47 49 123) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (4 94 100 6 48 118 124 50) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (94 95 101 100 118 119 125 124) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (95 96 102 101 119 120 126 125) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (96 97 103 102 120 121 127 126) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (97 98 104 103 121 122 128 127) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (98 99 105 104 122 123 129 128) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (99 5 7 105 123 49 51 129) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (16 14 18 20 60 58 62 64) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (10 8 14 16 54 52 58 60) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (8 6 12 14 52 50 56 58) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (6 100 106 12 50 124 130 56) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (100 101 107 106 124 125 131 130) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (101 102 108 107 125 126 132 131) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (102 103 109 108 126 127 133 132) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (103 104 110 109 127 128 134 133) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (104 105 111 110 128 129 135 134) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (105 7 13 111 129 51 57 135) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (7 9 15 13 51 53 59 57) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (9 11 17 15 53 55 61 59) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (15 17 21 19 59 61 65 63) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")

            f.write(");" + "\n")
            f.write("\n")

            # edges
            f.write("edges" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("\n")

            #Boundaries
            # Fuel
            f.write("boundary" + "\n")
            f.write("(" + "\n")

            # LHS outlet
            f.write("outlet_LHS" + "\n")
            f.write("{" + "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(20 18 62 64)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # RHS outlet
            f.write("outlet_RHS" + "\n")
            f.write("{" + "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(19 21 65 63)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air RHS
            f.write("secondary_air_RHS"+ "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(3 47 49 5)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air LHS
            f.write("secondary_air_LHS" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(2 46 48 4)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")


            # Top faces of fuel
            f.write("top_fuel" + "\n")
            f.write("{"+  "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(38 39 83 82)" + "\n")
            f.write("(40 41 85 84)" + "\n")
            f.write("(42 43 87 86)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # left faces of fuel
            f.write("L_fuel" + "\n")
            f.write("{"+  "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(32 76 82 38)" + "\n")
            f.write("(34 78 84 40)" + "\n")
            f.write("(36 80 86 42)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # Right faces of fuel
            f.write("R_fuel" + "\n")
            f.write("{"+  "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(33 77 83 39)" + "\n")
            f.write("(35 79 85 41)" + "\n")
            f.write("(37 81 87 43)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # bottom faces of fuel
            f.write("bottom_fuel" + "\n")
            f.write("{"+  "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(32 33 77 76)" + "\n")
            f.write("(34 35 79 78)" + "\n")
            f.write("(36 37 81 80)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")



            # Primary air inlets
            f.write("primary_inlets"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 26 70 44)" + "\n")
            f.write("(26 27 71 70)" + "\n")
            f.write("(27 28 72 71)" + "\n")
            f.write("(28 29 73 72)" + "\n")
            f.write("(29 30 74 73)" + "\n")
            f.write("(30 31 75 74)" + "\n")
            f.write("(31 1 45 75)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Stove Body
            f.write("stove_body" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 44 66 22)" + "\n")
            f.write("(22 66 68 24)" + "\n")
            f.write("(24 68 46 2)" + "\n")
            f.write("(4 48 50 6)" + "\n")
            f.write("(8 6 50 52)" + "\n")
            f.write("(10 8 52 54)" + "\n")
            f.write("(10 54 60 16)" + "\n")
            f.write("(16 60 64 20)" + "\n")
            f.write("(14 58 62 18)" + "\n")
            f.write("(14 12 56 58)" + "\n")
            f.write("(12 106 130 56)" + "\n")
            f.write("(106 107 131 130)" + "\n")
            f.write("(107 108 132 131)" + "\n")
            f.write("(108 109 133 132)" + "\n")
            f.write("(109 110 134 133)" + "\n")
            f.write("(110 111 135 134)" + "\n")
            f.write("(111 13 57 135)" + "\n")
            f.write("(13 15 59 57)" + "\n")
            f.write("(15 59 63 19)" + "\n")
            f.write("(17 61 65 21)" + "\n")
            f.write("(11 55 61 17)" + "\n")
            f.write("(9 11 55 53)" + "\n")
            f.write("(7 9 53 51)" + "\n")
            f.write("(5 49 51 7)" + "\n")
            f.write("(25 69 47 3)" + "\n")
            f.write("(23 67 69 25)" + "\n")
            f.write("(1 45 67 23)" +"\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Empty front and back faces
            f.write("\n")
            f.write("frontAndBack" + "\n")
            f.write("{" + "\n")
            f.write("type empty;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 26 32 22)" + "\n")
            f.write("(44 70 76 66)" + "\n")
            f.write("(26 27 142 140)" + "\n")
            f.write("(70 71 143 141)" + "\n")
            f.write("(27 28 34 33)" + "\n")
            f.write("(71 72 78 77)" + "\n")
            f.write("(28 29 150 148)" + "\n")
            f.write("(72 73 151 149)" + "\n")
            f.write("(29 30 36 35)" + "\n")
            f.write("(73 74 80 79)" + "\n")
            f.write("(30 31 158 156)" + "\n")
            f.write("(74 75 159 157)" + "\n")
            f.write("(31 1 23 37)" + "\n")
            f.write("(75 45 67 81)" + "\n")
            f.write("(22 140 136 24)" + "\n")
            f.write("(66 141 137 68)" + "\n")
            f.write("(32 33 39 38)" + "\n")
            f.write("(76 77 83 82)" + "\n")
            f.write("(142 148 144 138)" + "\n")
            f.write("(143 149 145 139)" + "\n")
            f.write("(34 35 41 40)" + "\n")
            f.write("(78 79 85 84)" + "\n")
            f.write("(150 156 152 146)" + "\n")
            f.write("(151 157 153 147)" + "\n")
            f.write("(36 37 43 42)" + "\n")
            f.write("(80 81 87 86)" + "\n")
            f.write("(158 23 25 154)" + "\n")
            f.write("(159 67 69 155)" + "\n")
            f.write("(24 38 88 2)" + "\n")
            f.write("(68 82 112 46)" + "\n")
            f.write("(136 138 89 88)" + "\n")
            f.write("(137 139 113 112)" + "\n")
            f.write("(39 40 90 89)" + "\n")
            f.write("(83 84 114 113)" + "\n")
            f.write("(144 146 91 90)" + "\n")
            f.write("(145 147 115 114)" + "\n")
            f.write("(41 42 92 91)" + "\n")
            f.write("(85 86 116 115)" + "\n")
            f.write("(152 154 93 92)" + "\n")
            f.write("(153 155 117 116)" + "\n")
            f.write("(43 25 3 93)" + "\n")
            f.write("(87 69 47 117)" + "\n")
            f.write("(2 88 94 4)" + "\n")
            f.write("(46 112 118 48)" + "\n")
            f.write("(88 89 95 94)" + "\n")
            f.write("(112 113 119 118)" + "\n")
            f.write("(89 90 96 95)" + "\n")
            f.write("(113 114 120 119)" + "\n")
            f.write("(90 91 97 96)" + "\n")
            f.write("(114 115 121 120)" + "\n")
            f.write("(91 92 98 97)" + "\n")
            f.write("(115 116 122 121)" + "\n")
            f.write("(92 93 99 98)" + "\n")
            f.write("(116 117 123 122)" + "\n")
            f.write("(93 3 5 99)" + "\n")
            f.write("(117 47 49 123)" + "\n")

            f.write("(4 94 100 6)" + "\n")
            f.write("(48 118 124 50)" + "\n")
            f.write("(94 95 101 100)" + "\n")
            f.write("(118 119 125 124)" + "\n")
            f.write("(95 96 102 101)" + "\n")
            f.write("(119 120 126 125)" + "\n")
            f.write("(96 97 103 102)" + "\n")
            f.write("(120 121 127 126)" + "\n")
            f.write("(97 98 104 103)" + "\n")
            f.write("(121 122 128 127)" + "\n")
            f.write("(98 99 105 104)" + "\n")
            f.write("(122 123 129 128)" + "\n")
            f.write("(99 5 7 105)" + "\n")
            f.write("(123 49 51 129)" + "\n")
            f.write("(16 14 18 20)" + "\n")
            f.write("(60 58 62 64)" + "\n")
            f.write("(10 8 14 16)" + "\n")
            f.write("(54 52 58 60)" + "\n")
            f.write("(8 6 12 14)" + "\n")
            f.write("(52 50 56 58)" + "\n")
            f.write("(6 100 106 12)" + "\n")
            f.write("(50 124 130 56)" + "\n")
            f.write("(100 101 107 106)" + "\n")

            f.write("(124 125 131 130)" + "\n")
            f.write("(101 102 108 107)" + "\n")
            f.write("(125 126 132 131)" + "\n")
            f.write("(102 103 109 108)" + "\n")
            f.write("(126 127 133 132)" + "\n")
            f.write("(103 104 110 109)" + "\n")
            f.write("(127 128 134 133)" + "\n")
            f.write("(104 105 111 110)" + "\n")
            f.write("(128 129 135 134)" + "\n")
            f.write("(105 7 13 111)" + "\n")
            f.write("(129 51 57 135)" + "\n")
            f.write("(7 9 15 13)" + "\n")
            f.write("(51 53 59 57)" + "\n")
            f.write("(9 11 17 15)" + "\n")
            f.write("(53 55 61 59)" + "\n")
            f.write("(15 17 21 19)" + "\n")
            f.write("(59 61 65 63)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")
            f.write(");" + "\n")
            f.write("\n")
            f.write("mergePatchPairs" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("// ************************************************************************* //")


def write_mesh_file(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str, pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str, pt84str, pt85str, pt86str, pt87str, pt88str, pt89str, pt90str, pt91str,  pt92str, pt93str, pt94str, pt95str, pt96str, pt97str, pt98str, pt99str, pt100str, pt101str, pt102str, pt103str, pt104str, pt105str, pt106str, pt107str, pt108str, pt109str, pt110str, pt111str, pt112str, pt113str, pt114str, pt115str, pt116str, pt117str, pt118str, pt119str, pt120str, pt121str, pt122str, pt123str, pt124str, pt125str, pt126str, pt127str):
    """Open the blockmesh template, edit and move to the Run folder
    Args:
    vertices defined as strings
    blockmesh_template (str): full file path where blockmesh template lives

    Returns:
    block_mesh_run_path (str): file path with the blockmesh file saved for running cases
    """
    with open(blockmesh_template,'r+') as f:
            f.seek(602) #where writing begins
            f.write("convertToMeters 1;"+"\n")
            f.write("\n")
            f.write("vertices"+"\n")
            f.write("("+"\n")

            # Write vertice strings
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
            f.write(pt48str+'\n')
            f.write(pt49str+'\n')
            f.write(pt50str+'\n')
            f.write(pt51str+'\n')

            # PRIMARY INLET vertices
            f.write(pt52str+'\n')
            f.write(pt53str+'\n')
            f.write(pt54str+'\n')
            f.write(pt55str+'\n')
            f.write(pt56str+'\n')
            f.write(pt57str+'\n')
            f.write(pt58str+'\n')
            f.write(pt59str+'\n')
            f.write(pt60str+'\n')
            f.write(pt61str+'\n')
            f.write(pt62str+'\n')
            f.write(pt63str+'\n')
            f.write(pt64str+'\n')
            f.write(pt65str+'\n')
            f.write(pt66str+'\n')
            f.write(pt67str+'\n')

            # Shifted Down
            f.write(pt68str+'\n')
            f.write(pt69str+'\n')
            f.write(pt70str+'\n')
            f.write(pt71str+'\n')
            f.write(pt72str+'\n')
            f.write(pt73str+'\n')
            f.write(pt74str+'\n')
            f.write(pt75str+'\n')
            f.write(pt76str+'\n')
            f.write(pt77str+'\n')
            f.write(pt78str+'\n')
            f.write(pt79str+'\n')
            f.write(pt80str+'\n')
            f.write(pt81str+'\n')
            f.write(pt82str+'\n')
            f.write(pt83str+'\n')

            f.write(pt84str+'\n')
            f.write(pt85str+'\n')
            f.write(pt86str+'\n')
            f.write(pt87str+'\n')
            f.write(pt88str+'\n')
            f.write(pt89str+'\n')
            f.write(pt90str+'\n')
            f.write(pt91str+'\n')
            f.write(pt92str+'\n')
            f.write(pt93str+'\n')
            f.write(pt94str+'\n')
            f.write(pt95str+'\n')
            f.write(pt96str+'\n')
            f.write(pt97str+'\n')
            f.write(pt98str+'\n')
            f.write(pt99str+'\n')
            f.write(pt100str+'\n')
            f.write(pt101str+'\n')
            f.write(pt102str+'\n')
            f.write(pt103str+'\n')
            f.write(pt104str+'\n')
            f.write(pt105str+'\n')
            f.write(pt106str+'\n')
            f.write(pt107str+'\n')
            f.write(pt108str+'\n')
            f.write(pt109str+'\n')
            f.write(pt110str+'\n')
            f.write(pt111str+'\n')
            f.write(pt112str+'\n')
            f.write(pt113str+'\n')
            f.write(pt114str+'\n')
            f.write(pt115str+'\n')
            f.write(pt116str+'\n')
            f.write(pt117str+'\n')
            f.write(pt118str+'\n')
            f.write(pt119str+'\n')
            f.write(pt120str+'\n')
            f.write(pt121str+'\n')
            f.write(pt122str+'\n')
            f.write(pt123str+'\n')
            f.write(pt124str+'\n')
            f.write(pt125str+'\n')
            f.write(pt126str+'\n')
            f.write(pt127str+'\n')


            f.write("\n")
            f.write(");"+"\n")
            f.write("\n")
            f.write("blocks"+"\n")
            f.write("(")
            f.write("\n")

            # write the blocks, with
            #f.write("hex (16 17 39 38 19 18 40 41) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (0 1 23 22 2 3 25 24) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (5 4 26 27 6 7 29 28) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (2 3 25 24 5 4 26 27) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (6 7 29 28 20 21 43 42) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (7 46 47 29 21 15 37 43) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (44 6 28 45 14 20 42 36) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (9 44 45 31 48 14 36 49) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (48 14 36 49 10 11 33 32) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (46 8 30 47 15 50 51 37) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (15 50 51 37 12 13 35 34) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (68 69 77 76 52 53 61 60) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (70 71 79 78 54 55 63 62) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (72 73 81 80 56 57 65 64) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (74 75 83 82 58 59 67 66) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (84 88 89 85 0 52 60 22) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (90 86 87 91 59 1 23 67) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (92 93 94 95 53 54 62 61) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (96 97 98 99 55 56 64 63) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (100 101 102 103 57 58 66 65) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (104 105 106 107 108 109 110 111) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (112 113 114 115 116 117 118 119) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (120 121 122 123 124 125 126 127) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")




            f.write(");" + "\n")
            f.write("\n")

            # edges
            f.write("edges" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("\n")

            #Boundaries
            # Fuel
            f.write("boundary" + "\n")
            f.write("(" + "\n")
            f.write("fuel" + "\n")
            f.write("{"+  "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(108 109 110 111)" + "\n")
            f.write("(116 117 118 119)" + "\n")
            f.write("(124 125 126 127)" + "\n")
            #  "(16 17 39 38)" + "\n" + "(38 16 19 41)" + "\n" + "(17 39 40 18)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # Primary air -- will need edits for air tray
            f.write("primary_air"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(68 69 77 76)" + "\n")
            f.write("(70 71 79 78)" + "\n")
            f.write("(72 73 81 80)" + "\n")
            f.write("(74 75 83 82)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air RHS
            f.write("Secondary_air_RHS"+ "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(3 25 26 4)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air LHS
            f.write("Secondary_air_LHS" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(2 24 27 5)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Outlet
            f.write("outlet"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(12 13 35 34)" + "\n" + "(10 11 33 32)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Stove Body
            f.write("stove_body" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(22 0 2 24)" + "\n" + "(1 23 25 3)" + "\n" + "(5 27 28 6)" + "\n" + "(4 26 29 7)" + "\n" + "(20 21 43 42)" + "\n" + "(14 20 42 36)" + "\n" + "(44 6 28 45)" + "\n" + "(21 15 37 43)" + "\n" + "(7 46 47 29)" + "\n" + "(14 36 33 11)" + "\n" + "(48 49 32 10)" + "\n" + "(9 44 45 31)" + "\n" + "(15 37 34 12)" + "\n" + "(50 51 35 13)" + "\n" + "(46 8 30 47)" + "\n" + "(8 30 51 50)" + "\n" + "(9 31 49 48)" + "\n")
            f.write("(68 76 60 52)" + "\n")
            f.write("(69 77 61 53)" + "\n")
            f.write("(70 78 62 54)" + "\n")
            f.write("(71 79 63 55)" + "\n")
            f.write("(72 80 64 56)" + "\n")
            f.write("(73 81 65 57)" + "\n")
            f.write("(74 82 66 58)" + "\n")
            f.write("(75 83 67 59)" + "\n")
            #f.write("(16 17 39 38)" + "\n")
            #f.write("(38 16 19 41)" + "\n")
            #f.write("(17 39 40 18)" + "\n")
            f.write("(0 52 60 22)" + "\n")
            f.write("(1 23 67 59)" +"\n")
            f.write("(84 85 22 0)" + "\n")
            f.write("(88 89 60 52)" + "\n")
            f.write("(90 91 67 59)" + "\n")
            f.write("(86 87 23 1)" + "\n")
            f.write("(84 88 89 85)" + "\n")
            f.write("(90 86 87 91)" + "\n")
            # MAY NEED TO ADD THE FACES OF TOP OF THE OUTER BOXS OF BOTTOM OF STOVE INTO Here
            # Space 1
            f.write("(92 95 61 53)" + "\n")
            f.write("(93 94 62 54)" + "\n")
            f.write("(92 93 94 95)" + "\n")
            f.write("(53 54 62 61)" + "\n")
            # Space 2
            f.write("(96 99 63 55)" + "\n")
            f.write("(97 98 64 56)" + "\n")
            f.write("(96 97 98 99)" + "\n")
            f.write("(55 56 64 63)" + "\n")
            # Space 3
            f.write("(100 103 65 57)" + "\n")
            f.write("(101 102 66 58)" + "\n")
            f.write("(100 101 102 103)" + "\n")
            f.write("(57 58 66 65)" + "\n")
            # New fuel blocks bottom and sides:
            f.write("(104 105 106 107)" + "\n")
            f.write("(105 106 110 109)" + "\n")
            f.write("(104 107 111 108)" + "\n")
            f.write("(112 113 114 115)" + "\n")
            f.write("(113 114 118 117)" + "\n")
            f.write("(112 115 119 116)" + "\n")
            f.write("(120 121 122 123)" + "\n")
            f.write("(121 122 126 125)" + "\n")
            f.write("(120 123 127 124)" + "\n")


            f.write(");" + "\n")
            f.write("}" + "\n")

            #Empty front and back faces
            f.write("\n")
            f.write("frontAndBack" + "\n")
            f.write("{" + "\n")
            f.write("type empty;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 1 3 2)" + "\n" + "(22 23 25 24)" + "\n" + "(2 3 4 5)" + "\n" + "(24 25 26 27)" + "\n" + "(5 4 7 6)" + "\n" + "(27 28 29 26)" + "\n" + "(6 7 21 20)" + "\n" + "(28 29 43 42)" + "\n" + "(44 6 20 14)" + "\n" + "(45 28 42 36)" + "\n" + "(29 47 37 43)" + "\n" + "(7 46 15 21)" + "\n" + "(9 44 14 48)" + "\n" + "(48 14 11 10)" + "\n" + "(31 45 36 49)" + "\n" + "(49 36 33 32)" + "\n" + "(46 8 50 15)" + "\n" + "(15 50 13 12)" + "\n" + "(47 30 51 37)" + "\n" + "(37 51 35 34)" + "\n" + "(52 53 69 68)" + "\n" + "(60 61 77 76)" + "\n" + "(54 55 71 70)" + "\n" + "(62 63 79 78)" + "\n" + "(56 57 73 72)" + "\n" + "(64 65 81 80)" + "\n" + "(58 59 75 74)" + "\n" + "(66 67 83 82)" + "\n")
            f.write("(90 86 1 59)" + "\n")
            f.write("(91 87 23 67)" + "\n")
            f.write("(84 88 52 0)" + "\n")
            f.write("(85 89 60 22)" + "\n")
            # Space 1
            f.write("(92 93 54 53)" + "\n")
            f.write("(95 94 62 61)" + "\n")
            # Space 2
            f.write("(96 97 56 55)" + "\n")
            f.write("(99 98 64 63)" + "\n")
            # Space 3
            f.write("(100 101 58 57)" + "\n")
            f.write("(103 102 66 65)" + "\n")
            # New fuel front and backs
            f.write("(104 105 109 108)" + "\n")
            f.write("(107 106 110 111)" + "\n")
            f.write("(112 113 116 117)" + "\n")
            f.write("(115 114 118 119)" + "\n")
            f.write("(120 121 125 124)" + "\n")
            f.write("(123 122 126 127)" + "\n")



            f.write(");" + "\n")
            f.write("}" + "\n")
            f.write(");" + "\n")
            f.write("\n")
            f.write("mergePatchPairs" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("// ************************************************************************* //")


#write_blockmesh(blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str)

def move_blockmesh(blockmesh_template):
    """purpose is to move the edited blockmesh template to the run folder prior to relocating to the case files. rename the file blockMeshDict for OF convention. Additionally, move the empty template from backup to the template folder
    Args:
    blockmesh_template (str): path where the NOW edited blockmeshDict file lives

    Returns:
    blockmesh_for_run (str): path where the blockMeshDict file for run is located prior to case runs.
    """
    # Running directory
    current_dir = os.getcwd()
    steps_for_run = "//blockMeshDict_foamfile//Run//"
    filename_for_run = "blockMeshDict"
    blockmesh_for_run = current_dir + steps_for_run + filename_for_run #blockmesh to be relocated to the case files

    # backup directory
    steps_for_backup = "//blockMeshDict_foamfile//Backup//"
    filename_for_backup = "blockMeshDict_template_backup"
    blockmesh_for_backup = current_dir + steps_for_backup + filename_for_backup #blockmesh to be relocated to the case files

    copy(blockmesh_template, blockmesh_for_run) # move to running directory
    copy(blockmesh_for_backup, blockmesh_template) # Move the backup blockmeshdict file to the template folder to re-produce original file convention

    return blockmesh_for_run
