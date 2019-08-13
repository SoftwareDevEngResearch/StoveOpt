# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:52:06 2019

@author: Lee
"""
"""Last test successful 4/26 12:19"""

"""The purpose of master.py is to call the functions in sequence from the varipus modules"""

#from import_geometry import *
import os
import fileinput
import shutil

""" Command line arguments:"""
# Import necessary packages
import sys
import argparse
import yaml
import time
from time import sleep

import import_geometry
import create_blockmeshfile
import new_case_setup
import post_processor
import run_surrounding_cases
import case_setup
import create_controldict
import runner
import compute_coordinates


# Importing all for now. change to explicit imports.
from import_geometry import *
from create_blockmeshfile import *
from run_surrounding_cases import *
from new_case_setup import *
from post_processor import *
from case_setup import *
from create_controldict import *
from runner import *
from compute_coordinates import *


def main():
    """ Main script"""
    # Construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser(description='Stove Optimization')
    # File directory argument
    parser.add_argument(
    '-i', '--inputfile', required=True, help='Please enter the full file path (directory and filename.extension) for the input.yaml file in LINUX format. For example, /mnt/c/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/StoveOpt/inputFiles/input.yaml')
    import sys
    args = parser.parse_args(sys.argv[1:])

    # Ensure the args all work-->string vs non string, slash variations, quotation marks
    #correct_arguments(args)
    print('args printed:')
    print(args)

    # Convert namespace to a usable input file convention
    input_file = convert_namespace(args)

    # EXTRACT DATA FROM THE INPUT FILE
    Q_100, D_fd, H_fd, Q_primary, N_holes, D_holes, max_delta_x, start_time, end_time, delta_t, num_cases_initial, write_interval, write_format, max_co, OS, Dc, H_cc, L_channel, L_deck, h_deck_pot, stick_width, W_gap = pull_input_data(input_file)

    # No shift needed
    #shift = 0.01
    #shift_positive = str(0.01)[:5]
    # Extract geometry
    #pt0x, pt0z, pt0y, pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y = extract_geometry(file_path) #unformatted list of (x,z,y) vertices

    #pt0x, pt0z, pt0y, pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, Q_100 = calculate_first_vertices(dfd, zfd, Dc, hcc, wc, hc, hcd, lcd, psp, Q_100)

    # compute_first coordinates from the compute_coordinates module
    pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, pt_64_z, pt_65_x, pt_65_y, pt_65_z = compute_first_coordinates(W_gap, Dc, H_cc, L_channel, L_deck, h_deck_pot, stick_width, D_fd, H_fd)

    # create_fuel_points from compute_coordinates
    pt_82_y, pt_76_y, pt_66_x, pt_68_x, pt_76_x, pt_82_x, pt_77_x, pt_83_x, pt_78_x, pt_84_x, pt_79_x, pt_85_x, pt_80_x, pt_86_x, pt_81_x, pt_87_x, pt_67_x, pt_69_x, pt_66_y, pt_68_y, pt_77_y, pt_83_y, pt_78_y, pt_84_y, pt_79_y, pt_85_y, pt_80_y, pt_86_y, pt_81_y, pt_87_y, pt_67_y, pt_69_y, pt_66_z, pt_76_z, pt_77_z, pt_78_z, pt_79_z, pt_80_z, pt_81_z, pt_67_z, pt_68_z, pt_82_z, pt_83_z, pt_84_z, pt_85_z, pt_86_z, pt_87_z, pt_69_z, pt_22_x, pt_22_y, pt_22_z, pt_24_x, pt_24_y, pt_24_z, pt_32_x, pt_32_y, pt_32_z, pt_38_x, pt_38_y, pt_38_z, pt_33_x, pt_33_y, pt_33_z, pt_39_x, pt_39_y, pt_39_z, pt_34_x, pt_34_y, pt_34_z, pt_40_x, pt_40_y, pt_40_z, pt_35_x, pt_35_y, pt_35_z, pt_41_x, pt_41_y, pt_41_z, pt_36_x, pt_36_y, pt_36_z, pt_42_x, pt_42_y, pt_42_z, pt_37_x, pt_37_y, pt_37_z, pt_43_x, pt_43_y, pt_43_z, pt_23_x, pt_23_y, pt_23_z, pt_25_x, pt_25_y, pt_25_z = compute_fuel_points(stick_width, Dc)

    # Create Fuel Blocks
    #pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y = create_fuel_blocks(pt0x, pt1x)

    # compute secondary vertices from compute_coordinates
    pt_26_z, pt_70_z, pt_27_z, pt_71_z, pt_28_z, pt_72_z, pt_29_z, pt_73_z, pt_30_z, pt_74_z, pt_31_z, pt_75_z, pt_88_z, pt_112_z, pt_89_z, pt_113_z, pt_90_z, pt_114_z, pt_91_z, pt_115_z, pt_92_z, pt_116_z, pt_93_z, pt_117_z, pt_94_z, pt_118_z, pt_95_z, pt_119_z, pt_96_z, pt_120_z, pt_97_z, pt_121_z, pt_98_z, pt_122_z, pt_99_z, pt_123_z, pt_100_z, pt_124_z, pt_101_z, pt_125_z, pt_102_z, pt_126_z, pt_103_z, pt_127_z, pt_104_z, pt_128_z, pt_105_z, pt_129_z, pt_106_z, pt_130_z, pt_107_z, pt_131_z, pt_108_z, pt_132_z, pt_109_z, pt_133_z, pt_110_z, pt_134_z, pt_111_z, pt_135_z, pt_26_y, pt_70_y, pt_88_y, pt_112_y, pt_94_y, pt_118_y, pt_100_y, pt_124_y, pt_106_y, pt_130_y, pt_27_y, pt_71_y, pt_89_y, pt_113_y, pt_95_y, pt_119_y, pt_101_y, pt_125_y, pt_107_y, pt_131_y, pt_28_y, pt_72_y, pt_90_y, pt_114_y, pt_96_y, pt_120_y, pt_102_y, pt_126_y, pt_108_y, pt_132_y, pt_29_y, pt_73_y, pt_91_y, pt_115_y, pt_97_y, pt_121_y, pt_103_y, pt_127_y, pt_109_y, pt_133_y, pt_30_y, pt_74_y, pt_92_y, pt_116_y, pt_98_y, pt_122_y, pt_104_y, pt_128_y, pt_110_y, pt_134_y, pt_31_y, pt_75_y, pt_93_y, pt_117_y, pt_99_y, pt_123_y, pt_105_y, pt_129_y, pt_111_y, pt_135_y, pt_70_x, pt_71_x, pt_72_x, pt_73_x, pt_74_x, pt_75_x, pt_112_x, pt_113_x, pt_114_x, pt_115_x, pt_116_x, pt_117_x, pt_118_x, pt_119_x, pt_120_x, pt_121_x, pt_122_x, pt_123_x, pt_124_x, pt_125_x, pt_126_x, pt_127_x, pt_128_x, pt_129_x, pt_130_x, pt_131_x, pt_132_x, pt_133_x, pt_134_x, pt_135_x, pt_26_x, pt_27_x, pt_28_x, pt_29_x, pt_30_x, pt_31_x, pt_88_x, pt_89_x, pt_90_x, pt_91_x, pt_92_x, pt_93_x, pt_94_x, pt_95_x, pt_96_x, pt_97_x, pt_98_x, pt_99_x, pt_100_x, pt_101_x, pt_102_x, pt_103_x, pt_104_x, pt_105_x, pt_106_x, pt_107_x, pt_108_x, pt_109_x, pt_110_x, pt_111_x = compute_secondary_vertices(pt_2_z, pt_4_z, pt_6_z, pt_12_z, pt_32_y, pt_33_y, pt_34_y, pt_35_y, pt_36_y, pt_37_y, pt_1_y, pt_32_z, pt_38_z)


    # Create additional front points
    #pt48x, pt48z, pt48y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt50x, pt50z, pt50y = create_additional_front_points(pt6x, pt7x, pt14x, pt9z, pt15x, pt8z, pt14z, pt9x, pt8x, pt15z)

    #  concatenate_vertices from compute_coordinates
    pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str = concatenate_vertices(pt_70_z, pt_71_z, pt_72_z, pt_73_z, pt_74_z, pt_75_z, pt_88_z, pt_112_z, pt_89_z, pt_113_z, pt_90_z, pt_114_z, pt_91_z, pt_115_z, pt_92_z, pt_116_z, pt_93_z, pt_117_z, pt_94_z, pt_118_z, pt_95_z, pt_119_z, pt_96_z, pt_120_z, pt_97_z, pt_121_z, pt_98_z, pt_122_z, pt_99_z, pt_123_z, pt_100_z, pt_124_z, pt_101_z, pt_125_z, pt_102_z, pt_126_z, pt_103_z, pt_127_z, pt_104_z, pt_128_z, pt_105_z, pt_129_z, pt_106_z,  pt_130_z, pt_107_z, pt_131_z, pt_108_z, pt_132_z, pt_109_z, pt_133_z, pt_110_z, pt_134_z, pt_111_z, pt_135_z, pt_70_y, pt_88_y, pt_112_y, pt_94_y, pt_118_y, pt_100_y, pt_124_y, pt_106_y, pt_130_y, pt_71_y, pt_89_y, pt_113_y, pt_95_y, pt_119_y, pt_101_y, pt_125_y, pt_107_y, pt_131_y, pt_72_y, pt_90_y, pt_114_y, pt_96_y, pt_120_y, pt_102_y, pt_126_y, pt_108_y, pt_132_y, pt_29_y, pt_73_y, pt_91_y, pt_115_y, pt_97_y, pt_121_y, pt_103_y, pt_127_y, pt_109_y, pt_133_y, pt_30_y, pt_74_y, pt_92_y, pt_116_y, pt_98_y, pt_122_y, pt_104_y, pt_128_y, pt_110_y, pt_134_y, pt_75_y, pt_93_y, pt_117_y, pt_99_y, pt_123_y, pt_105_y, pt_129_y, pt_111_y, pt_135_y, pt_70_x, pt_71_x, pt_72_x, pt_73_x, pt_74_x, pt_75_x, pt_112_x, pt_113_x, pt_114_x, pt_115_x, pt_116_x, pt_117_x, pt_118_x, pt_119_x, pt_120_x, pt_121_x, pt_122_x, pt_123_x, pt_124_x, pt_125_x, pt_126_x, pt_127_x, pt_128_x, pt_129_x, pt_130_x, pt_131_x, pt_132_x, pt_133_x, pt_134_x, pt_135_x, pt_88_x, pt_89_x, pt_90_x, pt_91_x, pt_92_x, pt_93_x, pt_94_x, pt_95_x, pt_96_x, pt_97_x, pt_98_x, pt_99_x, pt_100_x, pt_101_x, pt_102_x, pt_103_x, pt_104_x, pt_105_x, pt_106_x, pt_107_x, pt_108_x, pt_109_x, pt_110_x, pt_111_x, pt_66_x, pt_68_x, pt_76_x, pt_82_x, pt_77_x, pt_83_x, pt_78_x, pt_84_x, pt_79_x, pt_85_x, pt_80_x, pt_86_x, pt_81_x, pt_87_x, pt_67_x, pt_69_x, pt_66_y, pt_68_y, pt_77_y, pt_83_y, pt_78_y, pt_84_y, pt_79_y, pt_85_y, pt_80_y, pt_86_y, pt_81_y, pt_87_y, pt_67_y, pt_69_y, pt_66_z, pt_76_z, pt_77_z, pt_78_z, pt_79_z, pt_80_z, pt_81_z, pt_67_z, pt_68_z, pt_82_z, pt_83_z, pt_84_z, pt_85_z, pt_86_z, pt_87_z, pt_69_z, pt_76_y)

    # create_additional_vertices from compute_coordinates
    pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str = create_additional_vertices(pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z, pt_32_x, pt_32_y, pt_32_z, pt_33_x, pt_33_y, pt_33_z, pt_34_x, pt_34_y, pt_34_z, pt_35_x, pt_35_y, pt_35_z, pt_36_x, pt_36_y, pt_36_z, pt_37_x, pt_37_y, pt_37_z, pt_38_x, pt_38_y, pt_38_z, pt_39_x, pt_39_y, pt_39_z, pt_40_x, pt_40_y, pt_40_z, pt_41_x, pt_41_y, pt_41_z, pt_42_x, pt_42_y, pt_42_z, pt_43_x, pt_43_y, pt_43_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, pt_64_z, pt_65_x, pt_65_y, pt_65_z)

    # create_ghost_points from compute_coordinates
    pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str = create_ghost_points(pt_38_str, pt_82_str, pt_39_str, pt_83_str, pt_32_str, pt_76_str, pt_33_str, pt_77_str, pt_40_str, pt_84_str, pt_41_str, pt_85_str, pt_34_str, pt_78_str, pt_35_str,  pt_79_str, pt_42_str, pt_86_str, pt_43_str, pt_87_str, pt_36_str, pt_80_str, pt_37_str, pt_81_str)




    # convert front points to strings
    #pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr = points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt0x, pt0z, pt0y, pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt48x, pt48y, pt48z, pt50x, pt50y, pt50z)



    # concatenate all front point strings
    #pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt44str, pt46str, pt48str, pt50str = vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr)


    # Create concatenated strings for the back points

    #pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt45str, pt47str, pt49str, pt51str, shift_str = create_back_points(shift, pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50ystr, pt50zstr)


    # CREATE THE BOTTOM PRIMARY INLET POINTS HERE
    #pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str, pt84str, pt85str, pt86str, pt87str, pt88str, pt89str, pt90str, pt91str, pt92str, pt93str, pt94str, pt95str, pt96str, pt97str, pt98str, pt99str, pt100str, pt101str, pt102str, pt103str, pt53x, pt54x, V_primary_model, V_primary_model_str = create_primary_inlets(Dc, Q_primary, N_holes, D_holes, shift_str, shift, shift_positive)


    # CREATE THE WOOD FUEL BLOCKS:
    #stick_pitch, stick_bottom, stick_top, pt104str, pt105str, pt106str, pt107str, pt108str, pt109str, pt110str, pt111str, pt112str, pt113str, pt114str, pt115str, pt116str, pt117str, pt118str, pt119str, pt120str, pt121str, pt122str, pt123str, pt124str, pt125str, pt126str, pt127str = create_three_fuel_blocks(Dc, stick_width, shift_str)







    # Compute the initial velocity field
    velocity_dictionary, velocity_floats, k_tot = compute_initial_velocities(Q_100, num_cases_initial)
    # Create velocity strings for files
    velocity_case_names = edit_velocity_strings(velocity_dictionary, k_tot)
    # Solve for strings of case files
    case_full_paths, case_folder_names = create_case_directories(velocity_case_names, k_tot)
    # Add strings for foam file directories--NOT MAKEING DIRS YET
    case_zero_paths, case_system_paths, case_constant_paths = add_foam_directories(case_full_paths, k_tot)
    print("case system paths from main:")
    print(case_system_paths)
    # Creating foam directories in cases
    paste_static_foam_files(case_zero_paths, case_system_paths, case_constant_paths, k_tot)




    # from create_controldict module
    controldict_template = locate_controldict_template()
    write_controldict_template(controldict_template, start_time, end_time, delta_t, write_interval, write_format, max_co, pt_18_str, pt_14_str, pt_12_str, pt_13_str, pt_15_str, pt_19_str)
    controldict_for_run = move_controldict(controldict_template)
    controldict_case_paths = controldict_case_move(controldict_for_run, case_system_paths, k_tot)

    # CREATE ALL THE INITIAL SURROUNDING CASES
    blockmesh_template = locate_blockmesh_template()

    num_cells_int, num_cells_double, num_cells_int_str, num_cells_int_str_concat = compute_num_cells(max_delta_x, pt_0_y, pt_1_y)

    """write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str, pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str)
    """

    """write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str, pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str, pt84str, pt85str, pt86str, pt87str, pt88str, pt89str, pt90str, pt91str)
    """

    """
    write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str, pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str, pt84str, pt85str, pt86str, pt87str, pt88str, pt89str, pt90str, pt91str,  pt92str, pt93str, pt94str, pt95str, pt96str, pt97str, pt98str, pt99str, pt100str, pt101str, pt102str, pt103str)
    """

    # previous write_mesh
    #write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt44str, pt45str, pt46str, pt47str, pt48str, pt49str, pt50str, pt51str, pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str, pt84str, pt85str, pt86str, pt87str, pt88str, pt89str, pt90str, pt91str,  pt92str, pt93str, pt94str, pt95str, pt96str, pt97str, pt98str, pt99str, pt100str, pt101str, pt102str, pt103str, pt104str, pt105str, pt106str, pt107str, pt108str, pt109str, pt110str, pt111str, pt112str, pt113str, pt114str, pt115str, pt116str, pt117str, pt118str, pt119str, pt120str, pt121str, pt122str, pt123str, pt124str, pt125str, pt126str, pt127str)

    # Updated write_blockmesh
    write_blockmesh(num_cells_int_str_concat, blockmesh_template, num_cells_int, pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str, pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str, pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str)

    # move written blockmesh to the run folder, and the backup empty template to the tmplate directory
    blockmesh_for_run = move_blockmesh(blockmesh_template)

    # Move the blockmesh edited files to the case files
    blockmesh_case_paths = blockmesh_case_move(blockmesh_for_run, case_system_paths, k_tot)

    # Write the details files
    case_details_files = write_details_file(case_zero_paths, velocity_dictionary, k_tot)


    # Correcting primary flow
    """Q_per, V_primary, A_primary, diam_primary = correct_primary_flow(Q_primary, N_holes, D_holes, pt53x, pt54x)
    print("Q_per")
    print(Q_per)

    print("V_primary:")
    print(V_primary)

    sleep(20)
    """
    # Edit Boundary condition files
    case_U_files = write_velocity_files(velocity_dictionary, case_zero_paths, k_tot, V_primary_model_str)
    print("V_primary_model")
    print(V_primary_model)
    sleep(20)

    # FILES ARE FULLY DEFINED AT THIS POINT, NOW NEED TO RUN ITERATIVELY, PRIOR TO POST PROCESSING
    "Define case directory within loop of case based on entry in case_full_paths"
    #run_index = 0 # initialize loop
    #while run_index < 2: #testing the ability to run two at once
    import os
    case_dir = case_full_paths[1]
    print("case_dir from main")
    print(case_dir)
        #! /usr/bin/env python
        #import os
    #import runner_try
    #from runner_try import Run_Case



    # COPYING AND PASTING IN THE CTESTRUN CODE:
    #  ICE Revision: $Id$
    """pulled the lines from pyFoamRunner.py"""

    #from PyFoam.Applications.Runner import Runner
    #Runner("reactingFoam",case_dir)

    import os
    import time

    # Copy the pyFoamRunner into the case directories

    move_runner(case_full_paths, k_tot)

    # RUNNING CASES -- INDIVIDUALLY FOR NOW:
    run_cases_individual(case_full_paths, k_tot)


    ##time.sleep(10) #pause for 10 seconds

    #--------------------------------------------------------------------------


            #import PyFoam
            #from PyFoam import *
        #case_dir = os.getcwd()
            #case_dir = "C:\\Oregon_State\\Spring_2019\\Soft_dev_eng\\StoveOpt\\foamfiles\\counterFlowFlame2D\\case_25"

    #class ReactingFoamRunner(CTestRun):
    #    def init(self):
    #        self.setParameters(solver="reactingFoam",
    #                           originalCase=case_dir,
    #                           sizeClass="unlimited") # Run times are enormous here, so shouldn't have a problem with running my cases

        #if __name__=='__main__':
    #ReactingFoamRunner().run()
    #Run_Case(CTestRun)
    #run_index = run_index + 1"""



    # Edit the Boundary conditions for the 5 secondary flow cases
    #U_25_RHS_str, U_50_RHS_str, U_100_RHS_str, U_125_RHS_str, U_150_RHS_str, U_25_LHS_str, U_50_LHS_str, U_100_LHS_str, U_125_LHS_str, U_150_LHS_str = compute_velocities(U_100)

    #path_100, path_25, path_50, path_125, path_150 = locate_directories()

    # locate zero directories
    #fname_0_100, fname_0_25, fname_0_50, fname_0_125, fname_0_150, path_0_100, path_0_25, path_0_50, path_0_125, path_0_150 = locate_zero_files(path_100, path_25, path_50, path_125, path_150)

    """ If the files have already been edited, then pass over the edits----THIS IS CRUCIAL"""
    # write the velocity files in the zero folder
    #details_file_25, details_file_50, details_file_100, details_file_125, details_file_150 = write_velocity_files(U_25_RHS_str, U_50_RHS_str, U_100_RHS_str, U_125_RHS_str, U_150_RHS_str, U_25_LHS_str, U_50_LHS_str, U_100_LHS_str, U_125_LHS_str, U_150_LHS_str, path_0_100, path_0_125, path_0_150, path_0_25, path_0_50)

    # edit the boundary conditions
    #U_RHS_25, U_RHS_50, U_RHS_100, U_RHS_125, U_RHS_150, U_LHS_25, U_LHS_50, U_LHS_100, U_LHS_125, U_LHS_150 = edit_boundary_conditions(fname_0_100, fname_0_25, fname_0_50, fname_0_125, fname_0_150, U_25_RHS_str, U_50_RHS_str, U_100_RHS_str, U_125_RHS_str, U_150_RHS_str, U_25_LHS_str, U_50_LHS_str, U_100_LHS_str, U_125_LHS_str, U_150_LHS_str)

        # Edit the controlDict file
        #modify_controlDict(pt10str, pt11str, pt9str, pt48str, pt44str, pt14str, pt20str, pt6str, pt21str, pt7str, pt46str, pt15str, pt8str, pt50str, pt12str, pt13str)

    """At this point, the 25-150 cases are defined.
    This is where running the cases would go"""

        # Navigate to directories in loop, check if the the folder created by the runner exists (if not, initiate the simulation), wait until finished...







        # -----------------------------------POST PROCESSING MODULE-------------------------------------

    """Looping would likely begin here"""
    # pull in the data from files with label "case"
    foamfile_path = find_case_files()

    dir_list, case_list, length_case_list, list_temps, list_velocities = data_import(foamfile_path)

    # pull velocity, temperature, and case data from the case files. Create np array new_recarr
    new_recarr = average_pot_temperature(list_temps, length_case_list, list_velocities, case_list)

    # parse and sort
    array_sorted = parse_and_sort_array(new_recarr, length_case_list)


    # Evaluate the optimal
    T_max, velocity_max, T_max_index, velocity_column, temperature_column = evaluate_optimal(array_sorted, length_case_list)

    # plotting
    plot_variables(array_sorted, T_max, velocity_max, T_max_index, velocity_column, temperature_column)

    # compute neighboring velocities
    v_cases_added, v_cases_total_vector = compute_neighboring_velocities(array_sorted, T_max, velocity_max, T_max_index, length_case_list, velocity_column, temperature_column)


    #---------------------------------------------NEW CASE SETUP---------------------------------


    case_name_list, v_cases_total_vector_string, v_boundary_strings = define_new_case_names(v_cases_total_vector)

    full_case_paths = create_case_directories(case_name_list)

    zero_file_paths, constant_file_paths, system_file_paths = add_templates(full_case_paths)


    edit_details_files(zero_file_paths, v_boundary_strings)

    edit_iterative_boundary_conditions(zero_file_paths, constant_file_paths, system_file_paths, v_boundary_strings)




if __name__ == "__main__":
    main()
