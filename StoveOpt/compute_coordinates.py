W_gap = 0.03
Dc = 0.15
H_cc = 0.3
L_channel = 0.1
L_deck = 0.07
h_deck_pot = 0.03
stick_width = 0.02
D_fd = 0.01
H_fd = 0.1


import os



def compute_first_coordinates(W_gap, Dc, H_cc, L_channel, L_deck, h_deck_pot, stick_width, D_fd, H_fd):
    """Goal is to compute the x,y,z coordinates of the base vertices of the cookstove domain
    Args:
        D_fd (double): Diameter of secondary air inlet.
        H_fd(double): height of the centerline of secondary air inlet.
        Dc (double): Combustion chamber Diameter.
        H_cc (double): Combustion chamber height.
        W_gap (double): Channel width (spacing between shield and pot side).
        L_channel (double): Channel height.
        L_deck (double): Length of cone deck (transverse).
        h_deck_pot (double): Spacing from top of combustion chamber and bottom of pot.
        stick_width (double): Width of stick (square cross section).

    Returns:
        pt_i_x (double): x-coordinate of vertice i.
        pt_i_y (double): y-coordinate of vertice i.
        pt_i_z (double): z-coordinate of vertice i.
    """

    #Bottom CC
    pt_0_y = 0
    pt_0_z = 0
    pt_0_x = 0
    pt_1_y = Dc
    pt_1_z = 0
    pt_1_x = 0

    #Bottom of secondary inlet.
    pt_2_y = 0
    pt_2_z = H_fd -0.5*D_fd
    pt_2_x = 0
    pt_3_y = Dc
    pt_3_z = pt_2_z
    pt_3_x = 0

    #Top secondary inlet
    pt_4_y = pt_0_y
    pt_4_z = Dc + 0.5*D_fd
    pt_4_x = 0
    pt_5_y = pt_1_y
    pt_5_z = pt_4_z
    pt_5_x = 0

    #Top of combustion chamber
    pt_6_y = pt_0_y
    pt_6_z = H_cc
    pt_6_x = 0
    pt_8_y = 0 - (L_deck - W_gap)
    pt_8_z = pt_6_z
    pt_8_x = 0
    pt_10_y = 0-L_deck
    pt_10_z = pt_6_z
    pt_10_x = 0
    pt_7_y = pt_1_y
    pt_7_z = pt_6_z
    pt_7_x = 0
    pt_9_y = pt_7_y + (L_deck-W_gap)
    pt_9_z = pt_7_z
    pt_9_x = 0
    pt_11_y = pt_7_y+L_deck
    pt_11_z = pt_7_z
    pt_11_x = 0

    #Left Channel points.
    pt_12_y = pt_6_y
    pt_12_z = pt_6_z + h_deck_pot
    pt_12_x = 0
    pt_14_y = pt_8_y
    pt_14_z = pt_12_z
    pt_14_x = 0
    pt_16_y = pt_10_y
    pt_16_z = pt_14_z
    pt_16_x = 0
    pt_20_y = pt_16_y
    pt_20_z = H_cc + L_channel
    pt_20_x = 0
    pt_18_y = pt_8_y
    pt_18_z = pt_20_z
    pt_18_x = 0

    #Right channel points.
    pt_13_y = pt_7_y
    pt_13_z = pt_7_z + h_deck_pot
    pt_13_x = 0
    pt_15_y = pt_9_y
    pt_15_z = pt_13_z
    pt_15_x = 0
    pt_17_y = pt_11_y
    pt_17_z = pt_15_z
    pt_17_x = 0
    pt_21_y = pt_17_y
    pt_21_z = H_cc + L_channel
    pt_21_x = 0
    pt_19_y = pt_9_y
    pt_19_z = pt_21_z
    pt_19_x = 0

    # Define back points
    pt_44_y = pt_0_y
    pt_44_z = pt_0_z
    pt_45_y = pt_1_y
    pt_45_z = pt_1_z
    pt_46_y = pt_2_y
    pt_46_z = pt_2_z
    pt_47_y = pt_3_y
    pt_47_z = pt_3_z
    pt_48_y = pt_4_y
    pt_48_z = pt_4_z
    pt_49_y = pt_5_y
    pt_49_z = pt_5_z
    pt_50_y = pt_6_y
    pt_50_z = pt_6_z
    pt_51_y = pt_7_y
    pt_51_z = pt_7_z
    pt_52_y = pt_8_y
    pt_52_z = pt_8_z
    pt_53_y = pt_9_y
    pt_53_z = pt_9_z
    pt_54_y = pt_10_y
    pt_54_z = pt_10_z
    pt_55_y = pt_11_y
    pt_55_z = pt_11_z
    pt_56_y = pt_12_y
    pt_56_z = pt_12_z
    pt_57_y = pt_13_y
    pt_57_z = pt_13_z
    pt_58_y = pt_14_y
    pt_58_z = pt_14_z
    pt_59_y = pt_15_y
    pt_59_z = pt_15_z
    pt_60_y = pt_16_y
    pt_60_z = pt_16_z
    pt_61_y = pt_17_y
    pt_61_z = pt_17_z
    pt_62_y = pt_18_y
    pt_62_z = pt_18_z
    pt_63_y = pt_19_y
    pt_63_z = pt_19_z
    pt_64_y = pt_20_y
    pt_64_z = pt_20_z
    pt_65_y = pt_21_y
    pt_65_z = pt_21_z

    # Assigning shift
    shift = 0.01

    # Shifting the x-coordinates back



    pt_44_x = pt_45_x = pt_46_x = pt_47_x= pt_48_x= pt_49_x= pt_50_x= pt_51_x= pt_52_x= pt_53_x= pt_54_x= pt_55_x= pt_56_x= pt_57_x= pt_58_x= pt_59_x= pt_60_x= pt_61_x= pt_62_x= pt_63_x= pt_64_x= pt_65_x = shift

    """return pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z, pt_32_x, pt_32_y, pt_32_z, pt_33_x, pt_33_y, pt_33_z, pt_34_x, pt_34_y, pt_34_z, pt_35_x, pt_35_y, pt_35_z, pt_36_x, pt_36_y, pt_36_z, pt_37_x, pt_37_y, pt_37_z, pt_38_x, pt_38_y, pt_38_z, pt_39_x, pt_39_y, pt_39_z, pt_40_x, pt_40_y, pt_40_z, pt_41_x, pt_41_y, pt_41_z, pt_42_x, pt_42_y, pt_42_z, pt_43_x, pt_43_y, pt_43_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, _pt_64_z, pt_65_x, pt_65_y, pt_65_z
    """

    return pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, pt_64_z, pt_65_x, pt_65_y, pt_65_z



pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, pt_64_z, pt_65_x, pt_65_y, pt_65_z = compute_first_coordinates(W_gap, Dc, H_cc, L_channel, L_deck, h_deck_pot, stick_width, D_fd, H_fd)

def compute_fuel_points(stick_width, Dc):
    """Create the fuel vertices based on the geometry of the combustion chamber and the stick width entered by the user.
    Args:
    stick_width (double): Dimension of stick width -- square cross section
    Dc (double): Combustion chamber diameter

    Returns:
    ps (double): Pitch between sticks.

    P_1_i (double): Center point of stick 1 of 3 (x,y,z)
    P_2_i (double): Center point of stick 2 of 3 (x,y,z)
    P_3_i (double): Center point of stick 3 of 3 (x,y,z)

    pt_i_x (double): X-coordinate of point i.
    pt_i_y (double): Y-coordinate of point i.
    pt_i_z (double): Z-coordinate of point i.
    """

    # Dimensions
    N_sticks = 3 # static value
    N_spaces = N_sticks + 1
    H_st = stick_width # stick width
    ps = Dc/N_spaces

    # P_i
    P_1_y = ps
    P_1_z = H_st
    P_1_x = 0
    P_2_y = P_1_y + ps
    P_2_z = H_st
    P_2_x = 0
    P_3_y = P_2_y + ps
    P_3_z = H_st
    P_3_x = 0

    #Fuel coordinates
    pt_32_y = P_1_y - 0.5*H_st
    pt_32_z = P_1_z - 0.5*H_st
    pt_32_x = 0
    pt_33_y = P_1_y + 0.5*H_st
    pt_33_z = pt_32_z
    pt_33_x = 0
    pt_39_y = pt_33_y
    pt_39_z = P_1_z + 0.5*H_st
    pt_39_x = 0
    pt_38_y = pt_32_y
    pt_38_z = pt_39_z
    pt_38_x = 0
    pt_34_y = pt_32_y + ps
    pt_34_z = pt_32_z
    pt_34_x = 0
    pt_35_y = pt_33_y + ps
    pt_35_z = pt_33_z
    pt_35_x = 0
    pt_41_y = pt_39_y + ps
    pt_41_z = pt_39_z
    pt_41_x = 0
    pt_40_y = pt_34_y
    pt_40_z = pt_41_z
    pt_40_x = 0
    pt_36_y = pt_34_y + ps
    pt_36_z = pt_34_z
    pt_36_x = 0
    pt_37_y = pt_35_y + ps
    pt_37_z = pt_35_z
    pt_37_x = 0
    pt_43_y = pt_37_y
    pt_43_z = pt_41_z
    pt_43_x = 0
    pt_42_y = pt_36_y
    pt_42_z = pt_40_z
    pt_42_x = 0

    # Edge coordinates:
    pt_22_y = 0
    pt_22_z = pt_32_z
    pt_22_x = 0
    pt_24_y = 0
    pt_24_z = pt_38_z
    pt_24_x = 0
    pt_23_y = Dc
    pt_23_z = pt_37_z
    pt_23_x = 0
    pt_25_y = Dc
    pt_25_z = pt_43_z
    pt_25_x = 0

    # back coordinates:
    #Z-coords, bottom row:
    pt_66_z= pt_76_z= pt_77_z= pt_78_z= pt_79_z= pt_80_z= pt_81_z= pt_67_z = pt_22_z
    pt_68_z= pt_82_z= pt_83_z= pt_84_z= pt_85_z= pt_86_z= pt_87_z= pt_69_z = pt_24_z

    #Y-coordinates
    pt_66_y= pt_68_y = 0
    pt_77_y= pt_83_y = pt_33_y
    pt_78_y= pt_84_y = pt_34_y
    pt_79_y= pt_85_y = pt_35_y
    pt_80_y= pt_86_y = pt_36_y
    pt_81_y= pt_87_y = pt_37_y
    pt_67_y= pt_69_y = pt_23_y
    pt_76_y = pt_32_y
    pt_82_y = pt_76_y

    # X-coordinates
    shift = 0.01
    pt_66_x= pt_68_x= pt_76_x= pt_82_x= pt_77_x= pt_83_x= pt_78_x= pt_84_x= pt_79_x= pt_85_x= pt_80_x= pt_86_x= pt_81_x= pt_87_x= pt_67_x= pt_69_x = shift

    return pt_82_y, pt_76_y, pt_66_x, pt_68_x, pt_76_x, pt_82_x, pt_77_x, pt_83_x, pt_78_x, pt_84_x, pt_79_x, pt_85_x, pt_80_x, pt_86_x, pt_81_x, pt_87_x, pt_67_x, pt_69_x, pt_66_y, pt_68_y, pt_77_y, pt_83_y, pt_78_y, pt_84_y, pt_79_y, pt_85_y, pt_80_y, pt_86_y, pt_81_y, pt_87_y, pt_67_y, pt_69_y, pt_66_z, pt_76_z, pt_77_z, pt_78_z, pt_79_z, pt_80_z, pt_81_z, pt_67_z, pt_68_z, pt_82_z, pt_83_z, pt_84_z, pt_85_z, pt_86_z, pt_87_z, pt_69_z, pt_22_x, pt_22_y, pt_22_z, pt_24_x, pt_24_y, pt_24_z, pt_32_x, pt_32_y, pt_32_z, pt_38_x, pt_38_y, pt_38_z, pt_33_x, pt_33_y, pt_33_z, pt_39_x, pt_39_y, pt_39_z, pt_34_x, pt_34_y, pt_34_z, pt_40_x, pt_40_y, pt_40_z, pt_35_x, pt_35_y, pt_35_z, pt_41_x, pt_41_y, pt_41_z, pt_36_x, pt_36_y, pt_36_z, pt_42_x, pt_42_y, pt_42_z, pt_37_x, pt_37_y, pt_37_z, pt_43_x, pt_43_y, pt_43_z, pt_23_x, pt_23_y, pt_23_z, pt_25_x, pt_25_y, pt_25_z

pt_82_y, pt_76_y, pt_66_x, pt_68_x, pt_76_x, pt_82_x, pt_77_x, pt_83_x, pt_78_x, pt_84_x, pt_79_x, pt_85_x, pt_80_x, pt_86_x, pt_81_x, pt_87_x, pt_67_x, pt_69_x, pt_66_y, pt_68_y, pt_77_y, pt_83_y, pt_78_y, pt_84_y, pt_79_y, pt_85_y, pt_80_y, pt_86_y, pt_81_y, pt_87_y, pt_67_y, pt_69_y, pt_66_z, pt_76_z, pt_77_z, pt_78_z, pt_79_z, pt_80_z, pt_81_z, pt_67_z, pt_68_z, pt_82_z, pt_83_z, pt_84_z, pt_85_z, pt_86_z, pt_87_z, pt_69_z, pt_22_x, pt_22_y, pt_22_z, pt_24_x, pt_24_y, pt_24_z, pt_32_x, pt_32_y, pt_32_z, pt_38_x, pt_38_y, pt_38_z, pt_33_x, pt_33_y, pt_33_z, pt_39_x, pt_39_y, pt_39_z, pt_34_x, pt_34_y, pt_34_z, pt_40_x, pt_40_y, pt_40_z, pt_35_x, pt_35_y, pt_35_z, pt_41_x, pt_41_y, pt_41_z, pt_36_x, pt_36_y, pt_36_z, pt_42_x, pt_42_y, pt_42_z, pt_37_x, pt_37_y, pt_37_z, pt_43_x, pt_43_y, pt_43_z, pt_23_x, pt_23_y, pt_23_z, pt_25_x, pt_25_y, pt_25_z = compute_fuel_points(stick_width, Dc)

def compute_secondary_vertices(pt_2_z, pt_4_z, pt_6_z, pt_12_z, pt_32_y, pt_33_y, pt_34_y, pt_35_y, pt_36_y, pt_37_y, pt_1_y, pt_32_z, pt_38_z):
    """ Goal is to compute the x, y, z coordinates of all of the other coordinates required for the domain definition. The computation is based on the base points calculated in the previous vertice functions.
    Args:
    pt_i_y (double): various y-coordinates of previously defined points
    pt_i_z (double): various z-coordinates of previously defined points.

    Returns:
    pt_i_y (double): various y-coordinates for new points.
    pt_i_z (double): various z-coordinates for new points.
    pt_i_x (double): various x-coordinates for new points.
    """
    # Z-coordinates
    pt_26_z= pt_70_z= pt_27_z= pt_71_z= pt_28_z= pt_72_z= pt_29_z= pt_73_z= pt_30_z= pt_74_z= pt_31_z= pt_75_z = 0
    pt_88_z= pt_112_z = pt_89_z= pt_113_z= pt_90_z= pt_114_z= pt_91_z= pt_115_z= pt_92_z= pt_116_z= pt_93_z= pt_117_z = pt_2_z
    pt_94_z= pt_118_z= pt_95_z= pt_119_z= pt_96_z= pt_120_z= pt_97_z= pt_121_z= pt_98_z= pt_122_z= pt_99_z= pt_123_z = pt_4_z
    pt_100_z= pt_124_z= pt_101_z= pt_125_z= pt_102_z= pt_126_z= pt_103_z= pt_127_z= pt_104_z= pt_128_z= pt_105_z= pt_129_z = pt_6_z
    pt_106_z= pt_130_z= pt_107_z= pt_131_z= pt_108_z= pt_132_z= pt_109_z= pt_133_z= pt_110_z= pt_134_z= pt_111_z= pt_135_z = pt_12_z

    #Y-coordinates
    pt_26_y= pt_70_y= pt_88_y= pt_112_y= pt_94_y= pt_118_y= pt_100_y= pt_124_y= pt_106_y= pt_130_y = pt_32_y
    pt_27_y= pt_71_y= pt_89_y= pt_113_y= pt_95_y= pt_119_y= pt_101_y= pt_125_y= pt_107_y= pt_131_y = pt_33_y
    pt_28_y= pt_72_y= pt_90_y= pt_114_y= pt_96_y= pt_120_y= pt_102_y= pt_126_y= pt_108_y= pt_132_y= pt_34_y
    pt_29_y= pt_73_y= pt_91_y= pt_115_y= pt_97_y= pt_121_y= pt_103_y= pt_127_y= pt_109_y= pt_133_y = pt_35_y
    pt_30_y= pt_74_y= pt_92_y= pt_116_y= pt_98_y= pt_122_y= pt_104_y= pt_128_y= pt_110_y= pt_134_y = pt_36_y
    pt_31_y= pt_75_y= pt_93_y= pt_117_y= pt_99_y= pt_123_y= pt_105_y= pt_129_y= pt_111_y= pt_135_y = pt_37_y

    # X-coordinates
    pt_70_x= pt_71_x= pt_72_x= pt_73_x= pt_74_x= pt_75_x= pt_112_x= pt_113_x= pt_114_x= pt_115_x= pt_116_x= pt_117_x= pt_118_x= pt_119_x= pt_120_x= pt_121_x= pt_122_x= pt_123_x= pt_124_x= pt_125_x= pt_126_x= pt_127_x= pt_128_x= pt_129_x= pt_130_x= pt_131_x= pt_132_x= pt_133_x= pt_134_x= pt_135_x = -0.01
    pt_26_x= pt_27_x= pt_28_x= pt_29_x= pt_30_x= pt_31_x= pt_88_x= pt_89_x= pt_90_x= pt_91_x= pt_92_x= pt_93_x= pt_94_x= pt_95_x= pt_96_x= pt_97_x= pt_98_x= pt_99_x= pt_100_x=pt_101_x= pt_102_x= pt_103_x= pt_104_x= pt_105_x= pt_106_x= pt_107_x= pt_108_x= pt_109_x= pt_110_x= pt_111_x = 0

    return pt_26_z, pt_70_z, pt_27_z, pt_71_z, pt_28_z, pt_72_z, pt_29_z, pt_73_z, pt_30_z, pt_74_z, pt_31_z, pt_75_z, pt_88_z, pt_112_z, pt_89_z, pt_113_z, pt_90_z, pt_114_z, pt_91_z, pt_115_z, pt_92_z, pt_116_z, pt_93_z, pt_117_z, pt_94_z, pt_118_z, pt_95_z, pt_119_z, pt_96_z, pt_120_z, pt_97_z, pt_121_z, pt_98_z, pt_122_z, pt_99_z, pt_123_z, pt_100_z, pt_124_z, pt_101_z, pt_125_z, pt_102_z, pt_126_z, pt_103_z, pt_127_z, pt_104_z, pt_128_z, pt_105_z, pt_129_z, pt_106_z, pt_130_z, pt_107_z, pt_131_z, pt_108_z, pt_132_z, pt_109_z, pt_133_z, pt_110_z, pt_134_z, pt_111_z, pt_135_z, pt_26_y, pt_70_y, pt_88_y, pt_112_y, pt_94_y, pt_118_y, pt_100_y, pt_124_y, pt_106_y, pt_130_y, pt_27_y, pt_71_y, pt_89_y, pt_113_y, pt_95_y, pt_119_y, pt_101_y, pt_125_y, pt_107_y, pt_131_y, pt_28_y, pt_72_y, pt_90_y, pt_114_y, pt_96_y, pt_120_y, pt_102_y, pt_126_y, pt_108_y, pt_132_y, pt_29_y, pt_73_y, pt_91_y, pt_115_y, pt_97_y, pt_121_y, pt_103_y, pt_127_y, pt_109_y, pt_133_y, pt_30_y, pt_74_y, pt_92_y, pt_116_y, pt_98_y, pt_122_y, pt_104_y, pt_128_y, pt_110_y, pt_134_y, pt_31_y, pt_75_y, pt_93_y, pt_117_y, pt_99_y, pt_123_y, pt_105_y, pt_129_y, pt_111_y, pt_135_y, pt_70_x, pt_71_x, pt_72_x, pt_73_x, pt_74_x, pt_75_x, pt_112_x, pt_113_x, pt_114_x, pt_115_x, pt_116_x, pt_117_x, pt_118_x, pt_119_x, pt_120_x, pt_121_x, pt_122_x, pt_123_x, pt_124_x, pt_125_x, pt_126_x, pt_127_x, pt_128_x, pt_129_x, pt_130_x, pt_131_x, pt_132_x, pt_133_x, pt_134_x, pt_135_x, pt_26_x, pt_27_x, pt_28_x, pt_29_x, pt_30_x, pt_31_x, pt_88_x, pt_89_x, pt_90_x, pt_91_x, pt_92_x, pt_93_x, pt_94_x, pt_95_x, pt_96_x, pt_97_x, pt_98_x, pt_99_x, pt_100_x, pt_101_x, pt_102_x, pt_103_x, pt_104_x, pt_105_x, pt_106_x, pt_107_x, pt_108_x, pt_109_x, pt_110_x, pt_111_x

pt_26_z, pt_70_z, pt_27_z, pt_71_z, pt_28_z, pt_72_z, pt_29_z, pt_73_z, pt_30_z, pt_74_z, pt_31_z, pt_75_z, pt_88_z, pt_112_z, pt_89_z, pt_113_z, pt_90_z, pt_114_z, pt_91_z, pt_115_z, pt_92_z, pt_116_z, pt_93_z, pt_117_z, pt_94_z, pt_118_z, pt_95_z, pt_119_z, pt_96_z, pt_120_z, pt_97_z, pt_121_z, pt_98_z, pt_122_z, pt_99_z, pt_123_z, pt_100_z, pt_124_z, pt_101_z, pt_125_z, pt_102_z, pt_126_z, pt_103_z, pt_127_z, pt_104_z, pt_128_z, pt_105_z, pt_129_z, pt_106_z, pt_130_z, pt_107_z, pt_131_z, pt_108_z, pt_132_z, pt_109_z, pt_133_z, pt_110_z, pt_134_z, pt_111_z, pt_135_z, pt_26_y, pt_70_y, pt_88_y, pt_112_y, pt_94_y, pt_118_y, pt_100_y, pt_124_y, pt_106_y, pt_130_y, pt_27_y, pt_71_y, pt_89_y, pt_113_y, pt_95_y, pt_119_y, pt_101_y, pt_125_y, pt_107_y, pt_131_y, pt_28_y, pt_72_y, pt_90_y, pt_114_y, pt_96_y, pt_120_y, pt_102_y, pt_126_y, pt_108_y, pt_132_y, pt_29_y, pt_73_y, pt_91_y, pt_115_y, pt_97_y, pt_121_y, pt_103_y, pt_127_y, pt_109_y, pt_133_y, pt_30_y, pt_74_y, pt_92_y, pt_116_y, pt_98_y, pt_122_y, pt_104_y, pt_128_y, pt_110_y, pt_134_y, pt_31_y, pt_75_y, pt_93_y, pt_117_y, pt_99_y, pt_123_y, pt_105_y, pt_129_y, pt_111_y, pt_135_y, pt_70_x, pt_71_x, pt_72_x, pt_73_x, pt_74_x, pt_75_x, pt_112_x, pt_113_x, pt_114_x, pt_115_x, pt_116_x, pt_117_x, pt_118_x, pt_119_x, pt_120_x, pt_121_x, pt_122_x, pt_123_x, pt_124_x, pt_125_x, pt_126_x, pt_127_x, pt_128_x, pt_129_x, pt_130_x, pt_131_x, pt_132_x, pt_133_x, pt_134_x, pt_135_x, pt_26_x, pt_27_x, pt_28_x, pt_29_x, pt_30_x, pt_31_x, pt_88_x, pt_89_x, pt_90_x, pt_91_x, pt_92_x, pt_93_x, pt_94_x, pt_95_x, pt_96_x, pt_97_x, pt_98_x, pt_99_x, pt_100_x, pt_101_x, pt_102_x, pt_103_x, pt_104_x, pt_105_x, pt_106_x, pt_107_x, pt_108_x, pt_109_x, pt_110_x, pt_111_x = compute_secondary_vertices(pt_2_z, pt_4_z, pt_6_z, pt_12_z, pt_32_y, pt_33_y, pt_34_y, pt_35_y, pt_36_y, pt_37_y, pt_1_y, pt_32_z, pt_38_z)


def concatenate_vertices(pt_70_z, pt_71_z, pt_72_z, pt_73_z, pt_74_z, pt_75_z, pt_88_z, pt_112_z, pt_89_z, pt_113_z, pt_90_z, pt_114_z, pt_91_z, pt_115_z, pt_92_z, pt_116_z, pt_93_z, pt_117_z, pt_94_z, pt_118_z, pt_95_z, pt_119_z, pt_96_z, pt_120_z, pt_97_z, pt_121_z, pt_98_z, pt_122_z, pt_99_z, pt_123_z, pt_100_z, pt_124_z, pt_101_z, pt_125_z, pt_102_z, pt_126_z, pt_103_z, pt_127_z, pt_104_z, pt_128_z, pt_105_z, pt_129_z, pt_106_z,  pt_130_z, pt_107_z, pt_131_z, pt_108_z, pt_132_z, pt_109_z, pt_133_z, pt_110_z, pt_134_z, pt_111_z, pt_135_z, pt_70_y, pt_88_y, pt_112_y, pt_94_y, pt_118_y, pt_100_y, pt_124_y, pt_106_y, pt_130_y, pt_71_y, pt_89_y, pt_113_y, pt_95_y, pt_119_y, pt_101_y, pt_125_y, pt_107_y, pt_131_y, pt_72_y, pt_90_y, pt_114_y, pt_96_y, pt_120_y, pt_102_y, pt_126_y, pt_108_y, pt_132_y, pt_29_y, pt_73_y, pt_91_y, pt_115_y, pt_97_y, pt_121_y, pt_103_y, pt_127_y, pt_109_y, pt_133_y, pt_30_y, pt_74_y, pt_92_y, pt_116_y, pt_98_y, pt_122_y, pt_104_y, pt_128_y, pt_110_y, pt_134_y, pt_75_y, pt_93_y, pt_117_y, pt_99_y, pt_123_y, pt_105_y, pt_129_y, pt_111_y, pt_135_y, pt_70_x, pt_71_x, pt_72_x, pt_73_x, pt_74_x, pt_75_x, pt_112_x, pt_113_x, pt_114_x, pt_115_x, pt_116_x, pt_117_x, pt_118_x, pt_119_x, pt_120_x, pt_121_x, pt_122_x, pt_123_x, pt_124_x, pt_125_x, pt_126_x, pt_127_x, pt_128_x, pt_129_x, pt_130_x, pt_131_x, pt_132_x, pt_133_x, pt_134_x, pt_135_x, pt_88_x, pt_89_x, pt_90_x, pt_91_x, pt_92_x, pt_93_x, pt_94_x, pt_95_x, pt_96_x, pt_97_x, pt_98_x, pt_99_x, pt_100_x, pt_101_x, pt_102_x, pt_103_x, pt_104_x, pt_105_x, pt_106_x, pt_107_x, pt_108_x, pt_109_x, pt_110_x, pt_111_x, pt_66_x, pt_68_x, pt_76_x, pt_82_x, pt_77_x, pt_83_x, pt_78_x, pt_84_x, pt_79_x, pt_85_x, pt_80_x, pt_86_x, pt_81_x, pt_87_x, pt_67_x, pt_69_x, pt_66_y, pt_68_y, pt_77_y, pt_83_y, pt_78_y, pt_84_y, pt_79_y, pt_85_y, pt_80_y, pt_86_y, pt_81_y, pt_87_y, pt_67_y, pt_69_y, pt_66_z, pt_76_z, pt_77_z, pt_78_z, pt_79_z, pt_80_z, pt_81_z, pt_67_z, pt_68_z, pt_82_z, pt_83_z, pt_84_z, pt_85_z, pt_86_z, pt_87_z, pt_69_z, pt_76_y):
    """
    Goal is to concatenate the coordinates into full string vertices for mesh file convention
    Args:


    Returns:
        pt_i_x_str (str): x-coordinate of vertice i, string type.
        pt_i_y_str (str): y-coordinate of vertice i, string type.
        pt_i_z_str (str): z-coordinate of vertice i, string type.

        pt_i_str (str): full string definition of vertice i.

    """



    pt_66_x_str = str(pt_66_x)[:5]
    pt_66_y_str = str(pt_66_y)[:5]
    pt_66_z_str = str(pt_66_z)[:5]
    pt_67_x_str = str(pt_67_x)[:5]
    pt_67_y_str = str(pt_67_y)[:5]
    pt_67_z_str = str(pt_67_z)[:5]
    pt_68_x_str = str(pt_68_x)[:5]
    pt_68_y_str = str(pt_68_y)[:5]
    pt_68_z_str = str(pt_68_z)[:5]
    pt_69_x_str = str(pt_69_x)[:5]
    pt_69_y_str = str(pt_69_y)[:5]
    pt_69_z_str = str(pt_69_z)[:5]
    pt_70_x_str = str(pt_70_x)[:5]
    pt_70_y_str = str(pt_70_y)[:5]
    pt_70_z_str = str(pt_70_z)[:5]
    pt_71_x_str = str(pt_71_x)[:5]
    pt_71_y_str = str(pt_71_y)[:5]
    pt_71_z_str = str(pt_71_z)[:5]
    pt_72_x_str = str(pt_72_x)[:5]
    pt_72_y_str = str(pt_72_y)[:5]
    pt_72_z_str = str(pt_72_z)[:5]
    pt_73_x_str = str(pt_73_x)[:5]
    pt_73_y_str = str(pt_73_y)[:5]
    pt_73_z_str = str(pt_73_z)[:5]
    pt_74_x_str = str(pt_74_x)[:5]
    pt_74_y_str = str(pt_74_y)[:5]
    pt_74_z_str = str(pt_74_z)[:5]
    pt_75_x_str = str(pt_75_x)[:5]
    pt_75_y_str = str(pt_75_y)[:5]
    pt_75_z_str = str(pt_75_z)[:5]
    pt_76_x_str = str(pt_76_x)[:5]
    pt_76_y_str = str(pt_76_y)[:5]
    pt_76_z_str = str(pt_76_z)[:5]
    pt_77_x_str = str(pt_77_x)[:5]
    pt_77_y_str = str(pt_77_y)[:5]
    pt_77_z_str = str(pt_77_z)[:5]
    pt_78_x_str = str(pt_78_x)[:5]
    pt_78_y_str = str(pt_78_y)[:5]
    pt_78_z_str = str(pt_78_z)[:5]
    pt_79_x_str = str(pt_79_x)[:5]
    pt_79_y_str = str(pt_79_y)[:5]
    pt_79_z_str = str(pt_79_z)[:5]
    pt_80_x_str = str(pt_80_x)[:5]
    pt_80_y_str = str(pt_80_y)[:5]
    pt_80_z_str = str(pt_80_z)[:5]
    pt_81_x_str = str(pt_81_x)[:5]
    pt_81_y_str = str(pt_81_y)[:5]
    pt_81_z_str = str(pt_81_z)[:5]
    pt_82_x_str = str(pt_82_x)[:5]
    pt_82_y_str = str(pt_82_y)[:5]
    pt_82_z_str = str(pt_82_z)[:5]
    pt_83_x_str = str(pt_83_x)[:5]
    pt_83_y_str = str(pt_83_y)[:5]
    pt_83_z_str = str(pt_83_z)[:5]
    pt_84_x_str = str(pt_84_x)[:5]
    pt_84_y_str = str(pt_84_y)[:5]
    pt_84_z_str = str(pt_84_z)[:5]
    pt_85_x_str = str(pt_85_x)[:5]
    pt_85_y_str = str(pt_85_y)[:5]
    pt_85_z_str = str(pt_85_z)[:5]
    pt_86_x_str = str(pt_86_x)[:5]
    pt_86_y_str = str(pt_86_y)[:5]
    pt_86_z_str = str(pt_86_z)[:5]
    pt_87_x_str = str(pt_87_x)[:5]
    pt_87_y_str = str(pt_87_y)[:5]
    pt_87_z_str = str(pt_87_z)[:5]
    pt_88_x_str = str(pt_88_x)[:5]
    pt_88_y_str = str(pt_88_y)[:5]
    pt_88_z_str = str(pt_88_z)[:5]
    pt_89_x_str = str(pt_89_x)[:5]
    pt_89_y_str = str(pt_89_y)[:5]
    pt_89_z_str = str(pt_89_z)[:5]
    pt_90_x_str = str(pt_90_x)[:5]
    pt_90_y_str = str(pt_90_y)[:5]
    pt_90_z_str = str(pt_90_z)[:5]
    pt_91_x_str = str(pt_91_x)[:5]
    pt_91_y_str = str(pt_91_y)[:5]
    pt_91_z_str = str(pt_91_z)[:5]
    pt_92_x_str = str(pt_92_x)[:5]
    pt_92_y_str = str(pt_92_y)[:5]
    pt_92_z_str = str(pt_92_z)[:5]
    pt_93_x_str = str(pt_93_x)[:5]
    pt_93_y_str = str(pt_93_y)[:5]
    pt_93_z_str = str(pt_93_z)[:5]
    pt_94_x_str = str(pt_94_x)[:5]
    pt_94_y_str = str(pt_94_y)[:5]
    pt_94_z_str = str(pt_94_z)[:5]
    pt_95_x_str = str(pt_95_x)[:5]
    pt_95_y_str = str(pt_95_y)[:5]
    pt_95_z_str = str(pt_95_z)[:5]
    pt_96_x_str = str(pt_96_x)[:5]
    pt_96_y_str = str(pt_96_y)[:5]
    pt_96_z_str = str(pt_96_z)[:5]
    pt_97_x_str = str(pt_97_x)[:5]
    pt_97_y_str = str(pt_97_y)[:5]
    pt_97_z_str = str(pt_97_z)[:5]
    pt_98_x_str = str(pt_98_x)[:5]
    pt_98_y_str = str(pt_98_y)[:5]
    pt_98_z_str = str(pt_98_z)[:5]
    pt_99_x_str = str(pt_99_x)[:5]
    pt_99_y_str = str(pt_99_y)[:5]
    pt_99_z_str = str(pt_99_z)[:5]
    pt_100_x_str = str(pt_100_x)[:5]
    pt_100_y_str = str(pt_100_y)[:5]
    pt_100_z_str = str(pt_100_z)[:5]
    pt_101_x_str = str(pt_101_x)[:5]
    pt_101_y_str = str(pt_101_y)[:5]
    pt_101_z_str = str(pt_101_z)[:5]
    pt_102_x_str = str(pt_102_x)[:5]
    pt_102_y_str = str(pt_102_y)[:5]
    pt_102_z_str = str(pt_102_z)[:5]
    pt_103_x_str = str(pt_103_x)[:5]
    pt_103_y_str = str(pt_103_y)[:5]
    pt_103_z_str = str(pt_103_z)[:5]
    pt_104_x_str = str(pt_104_x)[:5]
    pt_104_y_str = str(pt_104_y)[:5]
    pt_104_z_str = str(pt_104_z)[:5]
    pt_105_x_str = str(pt_105_x)[:5]
    pt_105_y_str = str(pt_105_y)[:5]
    pt_105_z_str = str(pt_105_z)[:5]
    pt_106_x_str = str(pt_106_x)[:5]
    pt_106_y_str = str(pt_106_y)[:5]
    pt_106_z_str = str(pt_106_z)[:5]
    pt_107_x_str = str(pt_107_x)[:5]
    pt_107_y_str = str(pt_107_y)[:5]
    pt_107_z_str = str(pt_107_z)[:5]
    pt_108_x_str = str(pt_108_x)[:5]
    pt_108_y_str = str(pt_108_y)[:5]
    pt_108_z_str = str(pt_108_z)[:5]
    pt_109_x_str = str(pt_109_x)[:5]
    pt_109_y_str = str(pt_109_y)[:5]
    pt_109_z_str = str(pt_109_z)[:5]
    pt_110_x_str = str(pt_110_x)[:5]
    pt_110_y_str = str(pt_110_y)[:5]
    pt_110_z_str = str(pt_110_z)[:5]
    pt_111_x_str = str(pt_111_x)[:5]
    pt_111_y_str = str(pt_111_y)[:5]
    pt_111_z_str = str(pt_111_z)[:5]
    pt_112_x_str = str(pt_112_x)[:5]
    pt_112_y_str = str(pt_112_y)[:5]
    pt_112_z_str = str(pt_112_z)[:5]
    pt_113_x_str = str(pt_113_x)[:5]
    pt_113_y_str = str(pt_113_y)[:5]
    pt_113_z_str = str(pt_113_z)[:5]
    pt_114_x_str = str(pt_114_x)[:5]
    pt_114_y_str = str(pt_114_y)[:5]
    pt_114_z_str = str(pt_114_z)[:5]
    pt_115_x_str = str(pt_115_x)[:5]
    pt_115_y_str = str(pt_115_y)[:5]
    pt_115_z_str = str(pt_115_z)[:5]
    pt_116_x_str = str(pt_116_x)[:5]
    pt_116_y_str = str(pt_116_y)[:5]
    pt_116_z_str = str(pt_116_z)[:5]
    pt_117_x_str = str(pt_117_x)[:5]
    pt_117_y_str = str(pt_117_y)[:5]
    pt_117_z_str = str(pt_117_z)[:5]
    pt_118_x_str = str(pt_118_x)[:5]
    pt_118_y_str = str(pt_118_y)[:5]
    pt_118_z_str = str(pt_118_z)[:5]
    pt_119_x_str = str(pt_119_x)[:5]
    pt_119_y_str = str(pt_119_y)[:5]
    pt_119_z_str = str(pt_119_z)[:5]
    pt_120_x_str = str(pt_120_x)[:5]
    pt_120_y_str = str(pt_120_y)[:5]
    pt_120_z_str = str(pt_120_z)[:5]
    pt_121_x_str = str(pt_121_x)[:5]
    pt_121_y_str = str(pt_121_y)[:5]
    pt_121_z_str = str(pt_121_z)[:5]
    pt_122_x_str = str(pt_122_x)[:5]
    pt_122_y_str = str(pt_122_y)[:5]
    pt_122_z_str = str(pt_122_z)[:5]
    pt_123_x_str = str(pt_123_x)[:5]
    pt_123_y_str = str(pt_123_y)[:5]
    pt_123_z_str = str(pt_123_z)[:5]
    pt_124_x_str = str(pt_124_x)[:5]
    pt_124_y_str = str(pt_124_y)[:5]
    pt_124_z_str = str(pt_124_z)[:5]
    pt_125_x_str = str(pt_125_x)[:5]
    pt_125_y_str = str(pt_125_y)[:5]
    pt_125_z_str = str(pt_125_z)[:5]
    pt_126_x_str = str(pt_126_x)[:5]
    pt_126_y_str = str(pt_126_y)[:5]
    pt_126_z_str = str(pt_126_z)[:5]
    pt_127_x_str = str(pt_127_x)[:5]
    pt_127_y_str = str(pt_127_y)[:5]
    pt_127_z_str = str(pt_127_z)[:5]
    pt_128_x_str = str(pt_128_x)[:5]
    pt_128_y_str = str(pt_128_y)[:5]
    pt_128_z_str = str(pt_128_z)[:5]
    pt_129_x_str = str(pt_129_x)[:5]
    pt_129_y_str = str(pt_129_y)[:5]
    pt_129_z_str = str(pt_129_z)[:5]
    pt_130_x_str = str(pt_130_x)[:5]
    pt_130_y_str = str(pt_130_y)[:5]
    pt_130_z_str = str(pt_130_z)[:5]
    pt_131_x_str = str(pt_131_x)[:5]
    pt_131_y_str = str(pt_131_y)[:5]
    pt_131_z_str = str(pt_131_z)[:5]
    pt_132_x_str = str(pt_132_x)[:5]
    pt_132_y_str = str(pt_132_y)[:5]
    pt_132_z_str = str(pt_132_z)[:5]
    pt_133_x_str = str(pt_133_x)[:5]
    pt_133_y_str = str(pt_133_y)[:5]
    pt_133_z_str = str(pt_133_z)[:5]
    pt_134_x_str = str(pt_134_x)[:5]
    pt_134_y_str = str(pt_134_y)[:5]
    pt_134_z_str = str(pt_134_z)[:5]
    pt_135_x_str = str(pt_135_x)[:5]
    pt_135_y_str = str(pt_135_y)[:5]
    pt_135_z_str = str(pt_135_z)[:5]

    # Concatenate the strings:



    pt_66_str = "(" +  pt_66_x_str + " " + pt_66_y_str + " " + pt_66_z_str + ")"
    pt_67_str = "(" +  pt_67_x_str + " " + pt_67_y_str + " " + pt_67_z_str + ")"
    pt_68_str = "(" +  pt_68_x_str + " " + pt_68_y_str + " " + pt_68_z_str + ")"
    pt_69_str = "(" +  pt_69_x_str + " " + pt_69_y_str + " " + pt_69_z_str + ")"
    pt_70_str = "(" +  pt_70_x_str + " " + pt_70_y_str + " " + pt_70_z_str + ")"
    pt_71_str = "(" +  pt_71_x_str + " " + pt_71_y_str + " " + pt_71_z_str + ")"
    pt_72_str = "(" +  pt_72_x_str + " " + pt_72_y_str + " " + pt_72_z_str + ")"
    pt_73_str = "(" +  pt_73_x_str + " " + pt_73_y_str + " " + pt_73_z_str + ")"
    pt_74_str = "(" +  pt_74_x_str + " " + pt_74_y_str + " " + pt_74_z_str + ")"
    pt_75_str = "(" +  pt_75_x_str + " " + pt_75_y_str + " " + pt_75_z_str + ")"
    pt_76_str = "(" +  pt_76_x_str + " " + pt_76_y_str + " " + pt_76_z_str + ")"
    pt_77_str = "(" +  pt_77_x_str + " " + pt_77_y_str + " " + pt_77_z_str + ")"
    pt_78_str = "(" +  pt_78_x_str + " " + pt_78_y_str + " " + pt_78_z_str + ")"
    pt_79_str = "(" +  pt_79_x_str + " " + pt_79_y_str + " " + pt_79_z_str + ")"
    pt_80_str = "(" +  pt_80_x_str + " " + pt_80_y_str + " " + pt_80_z_str + ")"
    pt_81_str = "(" +  pt_81_x_str + " " + pt_81_y_str + " " + pt_81_z_str + ")"
    pt_82_str = "(" +  pt_82_x_str + " " + pt_82_y_str + " " + pt_82_z_str + ")"
    pt_83_str = "(" +  pt_83_x_str + " " + pt_83_y_str + " " + pt_83_z_str + ")"
    pt_84_str = "(" +  pt_84_x_str + " " + pt_84_y_str + " " + pt_84_z_str + ")"
    pt_85_str = "(" +  pt_85_x_str + " " + pt_85_y_str + " " + pt_85_z_str + ")"
    pt_86_str = "(" +  pt_86_x_str + " " + pt_86_y_str + " " + pt_86_z_str + ")"
    pt_87_str = "(" +  pt_87_x_str + " " + pt_87_y_str + " " + pt_87_z_str + ")"
    pt_88_str = "(" +  pt_88_x_str + " " + pt_88_y_str + " " + pt_88_z_str + ")"
    pt_89_str = "(" +  pt_89_x_str + " " + pt_89_y_str + " " + pt_89_z_str + ")"
    pt_90_str = "(" +  pt_90_x_str + " " + pt_90_y_str + " " + pt_90_z_str + ")"
    pt_91_str = "(" +  pt_91_x_str + " " + pt_91_y_str + " " + pt_91_z_str + ")"
    pt_92_str = "(" +  pt_92_x_str + " " + pt_92_y_str + " " + pt_92_z_str + ")"
    pt_93_str = "(" +  pt_93_x_str + " " + pt_93_y_str + " " + pt_93_z_str + ")"
    pt_94_str = "(" +  pt_94_x_str + " " + pt_94_y_str + " " + pt_94_z_str + ")"
    pt_95_str = "(" +  pt_95_x_str + " " + pt_95_y_str + " " + pt_95_z_str + ")"
    pt_96_str = "(" +  pt_96_x_str + " " + pt_96_y_str + " " + pt_96_z_str + ")"
    pt_97_str = "(" +  pt_97_x_str + " " + pt_97_y_str + " " + pt_97_z_str + ")"
    pt_98_str = "(" +  pt_98_x_str + " " + pt_98_y_str + " " + pt_98_z_str + ")"
    pt_99_str = "(" +  pt_99_x_str + " " + pt_99_y_str + " " + pt_99_z_str + ")"
    pt_100_str = "(" +  pt_100_x_str + " " + pt_100_y_str + " " + pt_100_z_str + ")"
    pt_101_str = "(" +  pt_101_x_str + " " + pt_101_y_str + " " + pt_101_z_str + ")"
    pt_102_str = "(" +  pt_102_x_str + " " + pt_102_y_str + " " + pt_102_z_str + ")"
    pt_103_str = "(" +  pt_103_x_str + " " + pt_103_y_str + " " + pt_103_z_str + ")"
    pt_104_str = "(" +  pt_104_x_str + " " + pt_104_y_str + " " + pt_104_z_str + ")"
    pt_105_str = "(" +  pt_105_x_str + " " + pt_105_y_str + " " + pt_105_z_str + ")"
    pt_106_str = "(" +  pt_106_x_str + " " + pt_106_y_str + " " + pt_106_z_str + ")"
    pt_107_str = "(" +  pt_107_x_str + " " + pt_107_y_str + " " + pt_107_z_str + ")"
    pt_108_str = "(" +  pt_108_x_str + " " + pt_108_y_str + " " + pt_108_z_str + ")"
    pt_109_str = "(" +  pt_109_x_str + " " + pt_109_y_str + " " + pt_109_z_str + ")"
    pt_110_str = "(" +  pt_110_x_str + " " + pt_110_y_str + " " + pt_110_z_str + ")"
    pt_111_str = "(" +  pt_111_x_str + " " + pt_111_y_str + " " + pt_111_z_str + ")"
    pt_112_str = "(" +  pt_112_x_str + " " + pt_112_y_str + " " + pt_112_z_str + ")"
    pt_113_str = "(" +  pt_113_x_str + " " + pt_113_y_str + " " + pt_113_z_str + ")"
    pt_114_str = "(" +  pt_114_x_str + " " + pt_114_y_str + " " + pt_114_z_str + ")"
    pt_115_str = "(" +  pt_115_x_str + " " + pt_115_y_str + " " + pt_115_z_str + ")"
    pt_116_str = "(" +  pt_116_x_str + " " + pt_116_y_str + " " + pt_116_z_str + ")"
    pt_117_str = "(" +  pt_117_x_str + " " + pt_117_y_str + " " + pt_117_z_str + ")"
    pt_118_str = "(" +  pt_118_x_str + " " + pt_118_y_str + " " + pt_118_z_str + ")"
    pt_119_str = "(" +  pt_119_x_str + " " + pt_119_y_str + " " + pt_119_z_str + ")"
    pt_120_str = "(" +  pt_120_x_str + " " + pt_120_y_str + " " + pt_120_z_str + ")"
    pt_121_str = "(" +  pt_121_x_str + " " + pt_121_y_str + " " + pt_121_z_str + ")"
    pt_122_str = "(" +  pt_122_x_str + " " + pt_122_y_str + " " + pt_122_z_str + ")"
    pt_123_str = "(" +  pt_123_x_str + " " + pt_123_y_str + " " + pt_123_z_str + ")"
    pt_124_str = "(" +  pt_124_x_str + " " + pt_124_y_str + " " + pt_124_z_str + ")"
    pt_125_str = "(" +  pt_125_x_str + " " + pt_125_y_str + " " + pt_125_z_str + ")"
    pt_126_str = "(" +  pt_126_x_str + " " + pt_126_y_str + " " + pt_126_z_str + ")"
    pt_127_str = "(" +  pt_127_x_str + " " + pt_127_y_str + " " + pt_127_z_str + ")"
    pt_128_str = "(" +  pt_128_x_str + " " + pt_128_y_str + " " + pt_128_z_str + ")"
    pt_129_str = "(" +  pt_129_x_str + " " + pt_129_y_str + " " + pt_129_z_str + ")"
    pt_130_str = "(" +  pt_130_x_str + " " + pt_130_y_str + " " + pt_130_z_str + ")"
    pt_131_str = "(" +  pt_131_x_str + " " + pt_131_y_str + " " + pt_131_z_str + ")"
    pt_132_str = "(" +  pt_132_x_str + " " + pt_132_y_str + " " + pt_132_z_str + ")"
    pt_133_str = "(" +  pt_133_x_str + " " + pt_133_y_str + " " + pt_133_z_str + ")"
    pt_134_str = "(" +  pt_134_x_str + " " + pt_134_y_str + " " + pt_134_z_str + ")"
    pt_135_str = "(" +  pt_135_x_str + " " + pt_135_y_str + " " + pt_135_z_str + ")"



    return pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str


pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str = concatenate_vertices(pt_70_z, pt_71_z, pt_72_z, pt_73_z, pt_74_z, pt_75_z, pt_88_z, pt_112_z, pt_89_z, pt_113_z, pt_90_z, pt_114_z, pt_91_z, pt_115_z, pt_92_z, pt_116_z, pt_93_z, pt_117_z, pt_94_z, pt_118_z, pt_95_z, pt_119_z, pt_96_z, pt_120_z, pt_97_z, pt_121_z, pt_98_z, pt_122_z, pt_99_z, pt_123_z, pt_100_z, pt_124_z, pt_101_z, pt_125_z, pt_102_z, pt_126_z, pt_103_z, pt_127_z, pt_104_z, pt_128_z, pt_105_z, pt_129_z, pt_106_z,  pt_130_z, pt_107_z, pt_131_z, pt_108_z, pt_132_z, pt_109_z, pt_133_z, pt_110_z, pt_134_z, pt_111_z, pt_135_z, pt_70_y, pt_88_y, pt_112_y, pt_94_y, pt_118_y, pt_100_y, pt_124_y, pt_106_y, pt_130_y, pt_71_y, pt_89_y, pt_113_y, pt_95_y, pt_119_y, pt_101_y, pt_125_y, pt_107_y, pt_131_y, pt_72_y, pt_90_y, pt_114_y, pt_96_y, pt_120_y, pt_102_y, pt_126_y, pt_108_y, pt_132_y, pt_29_y, pt_73_y, pt_91_y, pt_115_y, pt_97_y, pt_121_y, pt_103_y, pt_127_y, pt_109_y, pt_133_y, pt_30_y, pt_74_y, pt_92_y, pt_116_y, pt_98_y, pt_122_y, pt_104_y, pt_128_y, pt_110_y, pt_134_y, pt_75_y, pt_93_y, pt_117_y, pt_99_y, pt_123_y, pt_105_y, pt_129_y, pt_111_y, pt_135_y, pt_70_x, pt_71_x, pt_72_x, pt_73_x, pt_74_x, pt_75_x, pt_112_x, pt_113_x, pt_114_x, pt_115_x, pt_116_x, pt_117_x, pt_118_x, pt_119_x, pt_120_x, pt_121_x, pt_122_x, pt_123_x, pt_124_x, pt_125_x, pt_126_x, pt_127_x, pt_128_x, pt_129_x, pt_130_x, pt_131_x, pt_132_x, pt_133_x, pt_134_x, pt_135_x, pt_88_x, pt_89_x, pt_90_x, pt_91_x, pt_92_x, pt_93_x, pt_94_x, pt_95_x, pt_96_x, pt_97_x, pt_98_x, pt_99_x, pt_100_x, pt_101_x, pt_102_x, pt_103_x, pt_104_x, pt_105_x, pt_106_x, pt_107_x, pt_108_x, pt_109_x, pt_110_x, pt_111_x, pt_66_x, pt_68_x, pt_76_x, pt_82_x, pt_77_x, pt_83_x, pt_78_x, pt_84_x, pt_79_x, pt_85_x, pt_80_x, pt_86_x, pt_81_x, pt_87_x, pt_67_x, pt_69_x, pt_66_y, pt_68_y, pt_77_y, pt_83_y, pt_78_y, pt_84_y, pt_79_y, pt_85_y, pt_80_y, pt_86_y, pt_81_y, pt_87_y, pt_67_y, pt_69_y, pt_66_z, pt_76_z, pt_77_z, pt_78_z, pt_79_z, pt_80_z, pt_81_z, pt_67_z, pt_68_z, pt_82_z, pt_83_z, pt_84_z, pt_85_z, pt_86_z, pt_87_z, pt_69_z, pt_76_y)




def create_additional_vertices(pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z, pt_32_x, pt_32_y, pt_32_z, pt_33_x, pt_33_y, pt_33_z, pt_34_x, pt_34_y, pt_34_z, pt_35_x, pt_35_y, pt_35_z, pt_36_x, pt_36_y, pt_36_z, pt_37_x, pt_37_y, pt_37_z, pt_38_x, pt_38_y, pt_38_z, pt_39_x, pt_39_y, pt_39_z, pt_40_x, pt_40_y, pt_40_z, pt_41_x, pt_41_y, pt_41_z, pt_42_x, pt_42_y, pt_42_z, pt_43_x, pt_43_y, pt_43_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, _pt_64_z, pt_65_x, pt_65_y, pt_65_z):
    """Second vertice creator, due to more than 255 args"""
    pt_0_x_str = str(pt_0_x)[:5]
    pt_0_y_str = str(pt_0_y)[:5]
    pt_0_z_str = str(pt_0_z)[:5]
    pt_1_x_str = str(pt_1_x)[:5]
    pt_1_y_str = str(pt_1_y)[:5]
    pt_1_z_str = str(pt_1_z)[:5]
    pt_2_x_str = str(pt_2_x)[:5]
    pt_2_y_str = str(pt_2_y)[:5]
    pt_2_z_str = str(pt_2_z)[:5]
    pt_3_x_str = str(pt_3_x)[:5]
    pt_3_y_str = str(pt_3_y)[:5]
    pt_3_z_str = str(pt_3_z)[:5]
    pt_4_x_str = str(pt_4_x)[:5]
    pt_4_y_str = str(pt_4_y)[:5]
    pt_4_z_str = str(pt_4_z)[:5]
    pt_5_x_str = str(pt_5_x)[:5]
    pt_5_y_str = str(pt_5_y)[:5]
    pt_5_z_str = str(pt_5_z)[:5]
    pt_6_x_str = str(pt_6_x)[:5]
    pt_6_y_str = str(pt_6_y)[:5]
    pt_6_z_str = str(pt_6_z)[:5]
    pt_7_x_str = str(pt_7_x)[:5]
    pt_7_y_str = str(pt_7_y)[:5]
    pt_7_z_str = str(pt_7_z)[:5]
    pt_8_x_str = str(pt_8_x)[:5]
    pt_8_y_str = str(pt_8_y)[:5]
    pt_8_z_str = str(pt_8_z)[:5]
    pt_9_x_str = str(pt_9_x)[:5]
    pt_9_y_str = str(pt_9_y)[:5]
    pt_9_z_str = str(pt_9_z)[:5]
    pt_10_x_str = str(pt_10_x)[:5]
    pt_10_y_str = str(pt_10_y)[:5]
    pt_10_z_str = str(pt_10_z)[:5]
    pt_11_x_str = str(pt_11_x)[:5]
    pt_11_y_str = str(pt_11_y)[:5]
    pt_11_z_str = str(pt_11_z)[:5]
    pt_12_x_str = str(pt_12_x)[:5]
    pt_12_y_str = str(pt_12_y)[:5]
    pt_12_z_str = str(pt_12_z)[:5]
    pt_13_x_str = str(pt_13_x)[:5]
    pt_13_y_str = str(pt_13_y)[:5]
    pt_13_z_str = str(pt_13_z)[:5]
    pt_14_x_str = str(pt_14_x)[:5]
    pt_14_y_str = str(pt_14_y)[:5]
    pt_14_z_str = str(pt_14_z)[:5]
    pt_15_x_str = str(pt_15_x)[:5]
    pt_15_y_str = str(pt_15_y)[:5]
    pt_15_z_str = str(pt_15_z)[:5]
    pt_16_x_str = str(pt_16_x)[:5]
    pt_16_y_str = str(pt_16_y)[:5]
    pt_16_z_str = str(pt_16_z)[:5]
    pt_17_x_str = str(pt_17_x)[:5]
    pt_17_y_str = str(pt_17_y)[:5]
    pt_17_z_str = str(pt_17_z)[:5]
    pt_18_x_str = str(pt_18_x)[:5]
    pt_18_y_str = str(pt_18_y)[:5]
    pt_18_z_str = str(pt_18_z)[:5]
    pt_19_x_str = str(pt_19_x)[:5]
    pt_19_y_str = str(pt_19_y)[:5]
    pt_19_z_str = str(pt_19_z)[:5]
    pt_20_x_str = str(pt_20_x)[:5]
    pt_20_y_str = str(pt_20_y)[:5]
    pt_20_z_str = str(pt_20_z)[:5]
    pt_21_x_str = str(pt_21_x)[:5]
    pt_21_y_str = str(pt_21_y)[:5]
    pt_21_z_str = str(pt_21_z)[:5]
    pt_22_x_str = str(pt_22_x)[:5]
    pt_22_y_str = str(pt_22_y)[:5]
    pt_22_z_str = str(pt_22_z)[:5]
    pt_23_x_str = str(pt_23_x)[:5]
    pt_23_y_str = str(pt_23_y)[:5]
    pt_23_z_str = str(pt_23_z)[:5]
    pt_24_x_str = str(pt_24_x)[:5]
    pt_24_y_str = str(pt_24_y)[:5]
    pt_24_z_str = str(pt_24_z)[:5]
    pt_25_x_str = str(pt_25_x)[:5]
    pt_25_y_str = str(pt_25_y)[:5]
    pt_25_z_str = str(pt_25_z)[:5]
    pt_26_x_str = str(pt_26_x)[:5]
    pt_26_y_str = str(pt_26_y)[:5]
    pt_26_z_str = str(pt_26_z)[:5]
    pt_27_x_str = str(pt_27_x)[:5]
    pt_27_y_str = str(pt_27_y)[:5]
    pt_27_z_str = str(pt_27_z)[:5]
    pt_28_x_str = str(pt_28_x)[:5]
    pt_28_y_str = str(pt_28_y)[:5]
    pt_28_z_str = str(pt_28_z)[:5]
    pt_29_x_str = str(pt_29_x)[:5]
    pt_29_y_str = str(pt_29_y)[:5]
    pt_29_z_str = str(pt_29_z)[:5]
    pt_30_x_str = str(pt_30_x)[:5]
    pt_30_y_str = str(pt_30_y)[:5]
    pt_30_z_str = str(pt_30_z)[:5]
    pt_31_x_str = str(pt_31_x)[:5]
    pt_31_y_str = str(pt_31_y)[:5]
    pt_31_z_str = str(pt_31_z)[:5]
    pt_32_x_str = str(pt_32_x)[:5]
    pt_32_y_str = str(pt_32_y)[:5]
    pt_32_z_str = str(pt_32_z)[:5]
    pt_33_x_str = str(pt_33_x)[:5]
    pt_33_y_str = str(pt_33_y)[:5]
    pt_33_z_str = str(pt_33_z)[:5]
    pt_34_x_str = str(pt_34_x)[:5]
    pt_34_y_str = str(pt_34_y)[:5]
    pt_34_z_str = str(pt_34_z)[:5]
    pt_35_x_str = str(pt_35_x)[:5]
    pt_35_y_str = str(pt_35_y)[:5]
    pt_35_z_str = str(pt_35_z)[:5]
    pt_36_x_str = str(pt_36_x)[:5]
    pt_36_y_str = str(pt_36_y)[:5]
    pt_36_z_str = str(pt_36_z)[:5]
    pt_37_x_str = str(pt_37_x)[:5]
    pt_37_y_str = str(pt_37_y)[:5]
    pt_37_z_str = str(pt_37_z)[:5]
    pt_38_x_str = str(pt_38_x)[:5]
    pt_38_y_str = str(pt_38_y)[:5]
    pt_38_z_str = str(pt_38_z)[:5]
    pt_39_x_str = str(pt_39_x)[:5]
    pt_39_y_str = str(pt_39_y)[:5]
    pt_39_z_str = str(pt_39_z)[:5]
    pt_40_x_str = str(pt_40_x)[:5]
    pt_40_y_str = str(pt_40_y)[:5]
    pt_40_z_str = str(pt_40_z)[:5]
    pt_41_x_str = str(pt_41_x)[:5]
    pt_41_y_str = str(pt_41_y)[:5]
    pt_41_z_str = str(pt_41_z)[:5]
    pt_42_x_str = str(pt_42_x)[:5]
    pt_42_y_str = str(pt_42_y)[:5]
    pt_42_z_str = str(pt_42_z)[:5]
    pt_43_x_str = str(pt_43_x)[:5]
    pt_43_y_str = str(pt_43_y)[:5]
    pt_43_z_str = str(pt_43_z)[:5]
    pt_44_x_str = str(pt_44_x)[:5]
    pt_44_y_str = str(pt_44_y)[:5]
    pt_44_z_str = str(pt_44_z)[:5]
    pt_45_x_str = str(pt_45_x)[:5]
    pt_45_y_str = str(pt_45_y)[:5]
    pt_45_z_str = str(pt_45_z)[:5]
    pt_46_x_str = str(pt_46_x)[:5]
    pt_46_y_str = str(pt_46_y)[:5]
    pt_46_z_str = str(pt_46_z)[:5]
    pt_47_x_str = str(pt_47_x)[:5]
    pt_47_y_str = str(pt_47_y)[:5]
    pt_47_z_str = str(pt_47_z)[:5]
    pt_48_x_str = str(pt_48_x)[:5]
    pt_48_y_str = str(pt_48_y)[:5]
    pt_48_z_str = str(pt_48_z)[:5]
    pt_49_x_str = str(pt_49_x)[:5]
    pt_49_y_str = str(pt_49_y)[:5]
    pt_49_z_str = str(pt_49_z)[:5]
    pt_50_x_str = str(pt_50_x)[:5]
    pt_50_y_str = str(pt_50_y)[:5]
    pt_50_z_str = str(pt_50_z)[:5]
    pt_51_x_str = str(pt_51_x)[:5]
    pt_51_y_str = str(pt_51_y)[:5]
    pt_51_z_str = str(pt_51_z)[:5]
    pt_52_x_str = str(pt_52_x)[:5]
    pt_52_y_str = str(pt_52_y)[:5]
    pt_52_z_str = str(pt_52_z)[:5]
    pt_53_x_str = str(pt_53_x)[:5]
    pt_53_y_str = str(pt_53_y)[:5]
    pt_53_z_str = str(pt_53_z)[:5]
    pt_54_x_str = str(pt_54_x)[:5]
    pt_54_y_str = str(pt_54_y)[:5]
    pt_54_z_str = str(pt_54_z)[:5]
    pt_55_x_str = str(pt_55_x)[:5]
    pt_55_y_str = str(pt_55_y)[:5]
    pt_55_z_str = str(pt_55_z)[:5]
    pt_56_x_str = str(pt_56_x)[:5]
    pt_56_y_str = str(pt_56_y)[:5]
    pt_56_z_str = str(pt_56_z)[:5]
    pt_57_x_str = str(pt_57_x)[:5]
    pt_57_y_str = str(pt_57_y)[:5]
    pt_57_z_str = str(pt_57_z)[:5]
    pt_58_x_str = str(pt_58_x)[:5]
    pt_58_y_str = str(pt_58_y)[:5]
    pt_58_z_str = str(pt_58_z)[:5]
    pt_59_x_str = str(pt_59_x)[:5]
    pt_59_y_str = str(pt_59_y)[:5]
    pt_59_z_str = str(pt_59_z)[:5]
    pt_60_x_str = str(pt_60_x)[:5]
    pt_60_y_str = str(pt_60_y)[:5]
    pt_60_z_str = str(pt_60_z)[:5]
    pt_61_x_str = str(pt_61_x)[:5]
    pt_61_y_str = str(pt_61_y)[:5]
    pt_61_z_str = str(pt_61_z)[:5]
    pt_62_x_str = str(pt_62_x)[:5]
    pt_62_y_str = str(pt_62_y)[:5]
    pt_62_z_str = str(pt_62_z)[:5]
    pt_63_x_str = str(pt_63_x)[:5]
    pt_63_y_str = str(pt_63_y)[:5]
    pt_63_z_str = str(pt_63_z)[:5]
    pt_64_x_str = str(pt_64_x)[:5]
    pt_64_y_str = str(pt_64_y)[:5]
    pt_64_z_str = str(pt_64_z)[:5]
    pt_65_x_str = str(pt_65_x)[:5]
    pt_65_y_str = str(pt_65_y)[:5]
    pt_65_z_str = str(pt_65_z)[:5]

    pt_0_str = "(" + pt_0_x_str + " " + pt_0_y_str + " " + pt_0_z_str + ")"
    pt_1_str = "(" + pt_1_x_str + " " + pt_1_y_str + " " + pt_1_z_str + ")"
    pt_2_str = "(" + pt_2_x_str + " " + pt_2_y_str + " " + pt_2_z_str + ")"
    pt_3_str = "(" + pt_3_x_str + " " + pt_3_y_str + " " + pt_3_z_str + ")"
    pt_4_str = "(" + pt_4_x_str + " " + pt_4_y_str + " " + pt_4_z_str + ")"
    pt_5_str = "(" + pt_5_x_str + " " + pt_5_y_str + " " + pt_5_z_str + ")"
    pt_6_str = "(" + pt_6_x_str + " " + pt_6_y_str + " " + pt_6_z_str + ")"
    pt_7_str = "(" + pt_7_x_str + " " + pt_7_y_str + " " + pt_7_z_str + ")"
    pt_8_str = "(" + pt_8_x_str + " " + pt_8_y_str + " " + pt_8_z_str + ")"
    pt_9_str = "(" + pt_9_x_str + " " + pt_9_y_str + " " + pt_9_z_str + ")"
    pt_10_str = "(" + pt_10_x_str + " " + pt_10_y_str + " " + pt_10_z_str + ")"
    pt_11_str = "(" + pt_11_x_str + " " + pt_11_y_str + " " + pt_11_z_str + ")"
    pt_12_str = "(" + pt_12_x_str + " " + pt_12_y_str + " " + pt_12_z_str + ")"
    pt_13_str = "(" + pt_13_x_str + " " + pt_13_y_str + " " + pt_13_z_str + ")"
    pt_14_str = "(" + pt_14_x_str + " " + pt_14_y_str + " " + pt_14_z_str + ")"
    pt_15_str = "(" + pt_15_x_str + " " + pt_15_y_str + " " + pt_15_z_str + ")"
    pt_16_str = "(" + pt_16_x_str + " " + pt_16_y_str + " " + pt_16_z_str + ")"
    pt_17_str = "(" + pt_17_x_str + " " + pt_17_y_str + " " + pt_17_z_str + ")"
    pt_18_str = "(" + pt_18_x_str + " " + pt_18_y_str + " " + pt_18_z_str + ")"
    pt_19_str = "(" + pt_19_x_str + " " + pt_19_y_str + " " + pt_19_z_str + ")"
    pt_20_str = "(" + pt_20_x_str + " " + pt_20_y_str + " " + pt_20_z_str + ")"
    pt_21_str = "(" + pt_21_x_str + " " + pt_21_y_str + " " + pt_21_z_str + ")"
    pt_22_str = "(" + pt_22_x_str + " " + pt_22_y_str + " " + pt_22_z_str + ")"
    pt_23_str = "(" + pt_23_x_str + " " + pt_23_y_str + " " + pt_23_z_str + ")"
    pt_24_str = "(" + pt_24_x_str + " " + pt_24_y_str + " " + pt_24_z_str + ")"
    pt_25_str = "(" +  pt_25_x_str + " " + pt_25_y_str + " " + pt_25_z_str + ")"
    pt_26_str = "(" +  pt_26_x_str + " " + pt_26_y_str + " " + pt_26_z_str + ")"
    pt_27_str = "(" +  pt_27_x_str + " " + pt_27_y_str + " " + pt_27_z_str + ")"
    pt_28_str = "(" +  pt_28_x_str + " " + pt_28_y_str + " " + pt_28_z_str + ")"
    pt_29_str = "(" +  pt_29_x_str + " " + pt_29_y_str + " " + pt_29_z_str + ")"
    pt_30_str = "(" +  pt_30_x_str + " " + pt_30_y_str + " " + pt_30_z_str + ")"
    pt_31_str = "(" +  pt_31_x_str + " " + pt_31_y_str + " " + pt_31_z_str + ")"
    pt_32_str = "(" +  pt_32_x_str + " " + pt_32_y_str + " " + pt_32_z_str + ")"
    pt_33_str = "(" +  pt_33_x_str + " " + pt_33_y_str + " " + pt_33_z_str + ")"
    pt_34_str = "(" +  pt_34_x_str + " " + pt_34_y_str + " " + pt_34_z_str + ")"
    pt_35_str = "(" +  pt_35_x_str + " " + pt_35_y_str + " " + pt_35_z_str + ")"
    pt_36_str = "(" +  pt_36_x_str + " " + pt_36_y_str + " " + pt_36_z_str + ")"
    pt_37_str = "(" +  pt_37_x_str + " " + pt_37_y_str + " " + pt_37_z_str + ")"
    pt_38_str = "(" +  pt_38_x_str + " " + pt_38_y_str + " " + pt_38_z_str + ")"
    pt_39_str = "(" +  pt_39_x_str + " " + pt_39_y_str + " " + pt_39_z_str + ")"
    pt_40_str = "(" +  pt_40_x_str + " " + pt_40_y_str + " " + pt_40_z_str + ")"
    pt_41_str = "(" +  pt_41_x_str + " " + pt_41_y_str + " " + pt_41_z_str + ")"
    pt_42_str = "(" +  pt_42_x_str + " " + pt_42_y_str + " " + pt_42_z_str + ")"
    pt_43_str = "(" +  pt_43_x_str + " " + pt_43_y_str + " " + pt_43_z_str + ")"
    pt_44_str = "(" +  pt_44_x_str + " " + pt_44_y_str + " " + pt_44_z_str + ")"
    pt_45_str = "(" +  pt_45_x_str + " " + pt_45_y_str + " " + pt_45_z_str + ")"
    pt_46_str = "(" +  pt_46_x_str + " " + pt_46_y_str + " " + pt_46_z_str + ")"
    pt_47_str = "(" +  pt_47_x_str + " " + pt_47_y_str + " " + pt_47_z_str + ")"
    pt_48_str = "(" +  pt_48_x_str + " " + pt_48_y_str + " " + pt_48_z_str + ")"
    pt_49_str = "(" +  pt_49_x_str + " " + pt_49_y_str + " " + pt_49_z_str + ")"
    pt_50_str = "(" +  pt_50_x_str + " " + pt_50_y_str + " " + pt_50_z_str + ")"
    pt_51_str = "(" +  pt_51_x_str + " " + pt_51_y_str + " " + pt_51_z_str + ")"
    pt_52_str = "(" +  pt_52_x_str + " " + pt_52_y_str + " " + pt_52_z_str + ")"
    pt_53_str = "(" +  pt_53_x_str + " " + pt_53_y_str + " " + pt_53_z_str + ")"
    pt_54_str = "(" +  pt_54_x_str + " " + pt_54_y_str + " " + pt_54_z_str + ")"
    pt_55_str = "(" +  pt_55_x_str + " " + pt_55_y_str + " " + pt_55_z_str + ")"
    pt_56_str = "(" +  pt_56_x_str + " " + pt_56_y_str + " " + pt_56_z_str + ")"
    pt_57_str = "(" +  pt_57_x_str + " " + pt_57_y_str + " " + pt_57_z_str + ")"
    pt_58_str = "(" +  pt_58_x_str + " " + pt_58_y_str + " " + pt_58_z_str + ")"
    pt_59_str = "(" +  pt_59_x_str + " " + pt_59_y_str + " " + pt_59_z_str + ")"
    pt_60_str = "(" +  pt_60_x_str + " " + pt_60_y_str + " " + pt_60_z_str + ")"
    pt_61_str = "(" +  pt_61_x_str + " " + pt_61_y_str + " " + pt_61_z_str + ")"
    pt_62_str = "(" +  pt_62_x_str + " " + pt_62_y_str + " " + pt_62_z_str + ")"
    pt_63_str = "(" +  pt_63_x_str + " " + pt_63_y_str + " " + pt_63_z_str + ")"
    pt_64_str = "(" +  pt_64_x_str + " " + pt_64_y_str + " " + pt_64_z_str + ")"
    pt_65_str = "(" +  pt_65_x_str + " " + pt_65_y_str + " " + pt_65_z_str + ")"

    return pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str


pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str = create_additional_vertices(pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z, pt_32_x, pt_32_y, pt_32_z, pt_33_x, pt_33_y, pt_33_z, pt_34_x, pt_34_y, pt_34_z, pt_35_x, pt_35_y, pt_35_z, pt_36_x, pt_36_y, pt_36_z, pt_37_x, pt_37_y, pt_37_z, pt_38_x, pt_38_y, pt_38_z, pt_39_x, pt_39_y, pt_39_z, pt_40_x, pt_40_y, pt_40_z, pt_41_x, pt_41_y, pt_41_z, pt_42_x, pt_42_y, pt_42_z, pt_43_x, pt_43_y, pt_43_z, pt_44_x, pt_44_y, pt_44_z, pt_45_x, pt_45_y, pt_45_z, pt_46_x, pt_46_y, pt_46_z, pt_47_x, pt_47_y, pt_47_z, pt_48_x, pt_48_y, pt_48_z, pt_49_x, pt_49_y, pt_49_z, pt_50_x, pt_50_y, pt_50_z, pt_51_x, pt_51_y, pt_51_z, pt_52_x, pt_52_y, pt_52_z, pt_53_x, pt_53_y, pt_53_z, pt_54_x, pt_54_y, pt_54_z, pt_55_x, pt_55_y, pt_55_z, pt_56_x, pt_56_y, pt_56_z, pt_57_x, pt_57_y, pt_57_z, pt_58_x, pt_58_y, pt_58_z, pt_59_x, pt_59_y, pt_59_z, pt_60_x, pt_60_y, pt_60_z, pt_61_x, pt_61_y, pt_61_z, pt_62_x, pt_62_y, pt_62_z, pt_63_x, pt_63_y, pt_63_z, pt_64_x, pt_64_y, pt_64_z, pt_65_x, pt_65_y, pt_65_z)


def create_ghost_points(pt_38_str, pt_82_str, pt_39_str, pt_83_str, pt_32_str, pt_76_str, pt_33_str, pt_77_str, pt_40_str, pt_84_str, pt_41_str, pt_85_str, pt_34_str, pt_78_str, pt_35_str,  pt_79_str, pt_42_str, pt_86_str, pt_43_str, pt_87_str, pt_36_str, pt_80_str, pt_37_str, pt_81_str):
    """Create point on top of the existing fuel blocks to create internal faces:
    """
    pt_136_str = pt_38_str
    pt_137_str = pt_82_str
    pt_138_str = pt_39_str
    pt_139_str = pt_83_str
    pt_140_str = pt_32_str
    pt_141_str = pt_76_str
    pt_142_str = pt_33_str
    pt_143_str = pt_77_str
    pt_144_str = pt_40_str
    pt_145_str = pt_84_str
    pt_146_str = pt_41_str
    pt_147_str = pt_85_str
    pt_148_str = pt_34_str
    pt_149_str = pt_78_str
    pt_150_str = pt_35_str
    pt_151_str = pt_79_str
    pt_152_str = pt_42_str
    pt_153_str = pt_86_str
    pt_154_str = pt_43_str
    pt_155_str = pt_87_str
    pt_156_str = pt_36_str
    pt_157_str = pt_80_str
    pt_158_str = pt_37_str
    pt_159_str = pt_81_str

    return pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str

pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str = create_ghost_points(pt_38_str, pt_82_str, pt_39_str, pt_83_str, pt_32_str, pt_76_str, pt_33_str, pt_77_str, pt_40_str, pt_84_str, pt_41_str, pt_85_str, pt_34_str, pt_78_str, pt_35_str,  pt_79_str, pt_42_str, pt_86_str, pt_43_str, pt_87_str, pt_36_str, pt_80_str, pt_37_str, pt_81_str)

def write_mesh(pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str, pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str, pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str):
    """
    """
    # TEMPORARY FILE WRITING:
    current = os.getcwd()
    steps = "//mesh_test//bmesh"
    file_example=current + steps
    with open(file_example,'r+') as f:
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

            f.write('\n')
            f.write(");")


write_mesh(pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str, pt_36_str, pt_37_str, pt_38_str, pt_39_str, pt_40_str, pt_41_str, pt_42_str, pt_43_str, pt_44_str, pt_45_str, pt_46_str, pt_47_str, pt_48_str, pt_49_str, pt_50_str, pt_51_str, pt_52_str, pt_53_str, pt_54_str, pt_55_str, pt_56_str, pt_57_str, pt_58_str, pt_59_str, pt_60_str, pt_61_str, pt_62_str, pt_63_str, pt_64_str, pt_65_str, pt_66_str, pt_67_str, pt_68_str, pt_69_str, pt_70_str, pt_71_str, pt_72_str, pt_73_str, pt_74_str, pt_75_str, pt_76_str, pt_77_str, pt_78_str, pt_79_str, pt_80_str, pt_81_str, pt_82_str, pt_83_str, pt_84_str, pt_85_str, pt_86_str, pt_87_str, pt_88_str, pt_89_str, pt_90_str, pt_91_str, pt_92_str, pt_93_str, pt_94_str, pt_95_str, pt_96_str, pt_97_str, pt_98_str, pt_99_str, pt_100_str, pt_101_str, pt_102_str, pt_103_str, pt_104_str, pt_105_str, pt_106_str, pt_107_str, pt_108_str, pt_109_str, pt_110_str, pt_111_str, pt_112_str, pt_113_str, pt_114_str, pt_115_str, pt_116_str, pt_117_str, pt_118_str, pt_119_str, pt_120_str, pt_121_str, pt_122_str, pt_123_str, pt_124_str, pt_125_str, pt_126_str, pt_127_str, pt_128_str, pt_129_str, pt_130_str, pt_131_str, pt_132_str, pt_133_str, pt_134_str, pt_135_str, pt_136_str, pt_137_str, pt_138_str, pt_139_str, pt_140_str, pt_141_str, pt_142_str, pt_143_str, pt_144_str, pt_145_str, pt_146_str, pt_147_str, pt_148_str, pt_149_str, pt_150_str, pt_151_str, pt_152_str, pt_153_str, pt_154_str, pt_155_str, pt_156_str, pt_157_str, pt_158_str, pt_159_str)
