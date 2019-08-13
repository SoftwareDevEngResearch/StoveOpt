# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:39:27 2019

@author: Lee
"""
import numpy
import yaml
import sys
import argparse
import xlrd
import time
from time import sleep

def convert_namespace(args):
    """Purpose is to convert the namespace from the args to a pure input file for reading

    Args:
        args (namespace): Argument provided by user on command fuel_vertice_concatenate

    Returns:

        input_file (string): Outputs the input file extracted from the name space. Location of the input file provided by user.

    """
    input_file = args.inputfile
    print("input file value within import geometry module, convert namespace fn")
    print(input_file)

    print("input file TYPE")
    print(type(input_file))

    return input_file


"""Need to figure out the correct_arguments script"""
def pull_input_data(input_file):
    """
    Goal is to convert the geometry file argument to working syntax: Single quote, back slash

    Args:

        args (dictionary): Object contains the contents of the input file specified by the user


    Returns:

    TO DO

    """

    with open(input_file, 'r') as f:
        doc = yaml.load(f)

        # Secondary flow Definitions
        Q_100 = doc['case']['Secondary air flow rate'] # 100% flow rate [m^3/s]
        D_fd = doc['case']['Diameter of secondary air inlet']
        H_fd = doc['case']['Height of secondary air inlet']

        # Air tray flow definitons
        Q_primary = doc['case']['Primary air flow rate'] # maximum primary airflow rate
        N_holes = doc['case']['Number of holes in air tray']
        D_holes = doc['case']['Diameter of holes in air tray']

        # CFD definitions
        max_delta_x = doc['case']['Maximum grid spacing'] # maximum grid spacing selected [m]
        start_time = doc['case']['Start time']
        end_time = doc['case']['End Time']
        delta_t = doc['case']['Time step'] # time step for simulation
        num_cases_initial = doc['case']['Initial number of cases']
        write_interval = doc['case']['Write interval']
        write_format = doc['case']['Write format']
        max_co = doc['case']['maxCo']
        OS = doc['case']['Operating System'] # operating system of the user. Used for fpath manipulation

        # Stove geometry Definitions
        Dc = doc['case']['Combustion chamber diameter']
        H_cc = doc['case']['Combustion chamber height']
        W_gap = doc['case']['Channel width']
        L_channel = doc['case']['Channel height']
        #H_deck = doc['case']['Height of cone deck']
        L_deck = doc['case']['Length of cone deck']
        h_deck_pot = doc['case']['Pot spacing']

        # sticks
        stick_width = doc['case']['Dimension of wood sticks']


    return Q_100, D_fd, H_fd, Q_primary, N_holes, D_holes, max_delta_x, start_time, end_time, delta_t, num_cases_initial, write_interval, write_format, max_co, OS, Dc, H_cc, L_channel, L_deck, h_deck_pot, stick_width, W_gap


def locate_geometry(path, fname):
    """
    Pull file path and name from the input file (command line argument)

    Args:

        path (str): string containing the directory of the stove geometry file

        fname (str): string with the filename of the geom file (with extension)
    Returns:
        file_path (str): full file path for input stove geometry defined by user in input yaml file.s
    """
    file_path = path + '//' + fname
    print(file_path)
    #else:
    return file_path

def extract_geometry(file_path):
    """
    Pulling Data from excel workbook

    Args:

        file_path (str): full file path for input stove geometry defined by user in input yaml file.

    Returns:
        pt#i (float): A series of points pulled from the user defined geometry

    """
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name('Outputs')
    pt0x = worksheet.cell(1,2).value
    pt0z = worksheet.cell(1,3).value
    pt0y = worksheet.cell(1,4).value
    pt1x = worksheet.cell(2,2).value
    pt1z = worksheet.cell(2,3).value
    pt1y = worksheet.cell(2,4).value
    pt2x = worksheet.cell(3,2).value
    pt2z = worksheet.cell(3,3).value
    pt2y = worksheet.cell(3,4).value
    pt3x = worksheet.cell(4,2).value
    pt3z = worksheet.cell(4,3).value
    pt3y = worksheet.cell(4,4).value
    pt4x = worksheet.cell(5,2).value
    pt4z = worksheet.cell(5,3).value
    pt4y = worksheet.cell(5,4).value
    pt5x = worksheet.cell(6,2).value
    pt5z = worksheet.cell(6,3).value
    pt5y = worksheet.cell(6,4).value
    pt6x = worksheet.cell(7,2).value
    pt6z = worksheet.cell(7,3).value
    pt6y = worksheet.cell(7,4).value
    pt7x = worksheet.cell(8,2).value
    pt7z = worksheet.cell(8,3).value
    pt7y = worksheet.cell(8,4).value
    pt8x = worksheet.cell(9,2).value
    pt8z = worksheet.cell(9,3).value
    pt8y = worksheet.cell(9,4).value
    pt9x = worksheet.cell(10,2).value
    pt9z = worksheet.cell(10,3).value
    pt9y = worksheet.cell(10,4).value
    pt10x = worksheet.cell(11,2).value
    pt10z = worksheet.cell(11,3).value
    pt10y = worksheet.cell(11,4).value
    pt11x = worksheet.cell(12,2).value
    pt11z = worksheet.cell(12,3).value
    pt11y = worksheet.cell(12,4).value
    pt12x = worksheet.cell(13,2).value
    pt12z = worksheet.cell(13,3).value
    pt12y = worksheet.cell(13,4).value
    pt13x = worksheet.cell(14,2).value
    pt13z = worksheet.cell(14,3).value
    pt13y = worksheet.cell(14,4).value
    pt14x = worksheet.cell(15,2).value
    pt14z = worksheet.cell(15,3).value
    pt14y = worksheet.cell(15,4).value
    pt15x = worksheet.cell(16,2).value
    pt15z = worksheet.cell(16,3).value
    pt15y = worksheet.cell(16,4).value

    print("pt0x from extract geom")
    print(pt0x)
    print("pt0y from extract geom")
    print(pt0y)
    print("pt0z from extract geom")
    print(pt0z)

    pt0x, pt0z, pt0y, pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y

def calculate_first_vertices(dfd, zfd, Dc, hcc, wc, hc, hcd, lcd, psp, Q_100):
    """Compute the first batch of vertices based on the user inputs
    Args:


    Returns:
    pt#i (double): General coordinate where x is the horizontal, z is vertical, and y is in/out of the domain
    Q_100 (double): Velocity of secondary inlet.
    """
    pt0x = 0
    pt0z = 0
    pt0y = 0

    pt1x = Dc # bottom right coord
    pt1z = 0
    pt1y = 0

    # Pt 2 is the bottom LHS secondary air inlet
    pt2x = 0
    pt2z = zfd - (dfd/2)
    pt2y = 0

    # Pt 3 is the bottom RHS secondary air inlet
    pt3x = Dc
    pt3z = zfd- (dfd/2)
    pt3y = 0

    # pt4 is RHS top of secondary air inlet
    pt4x = Dc
    pt4z = zfd + (dfd/2)
    pt4y = 0

    # pt5 is the left hand side top of secondary air inlet
    pt5x = 0
    pt5z = zfd + (dfd/2)
    pt5y = 0

    # pt 6 is LHS chamber to cone deck
    pt6x = 0
    pt6y = 0
    pt6z = hcd # cone deck Height

    # pt 7 is RHS chamber to cone deck
    pt7x = Dc
    pt7y = 0
    pt7z = hcd # cone deck Height

    # pt 8 is RHS bottom of Channel
    pt8x = Dc + lcd # chamber diam plus length cone deck
    pt8z = hcd
    pt8y = 0

    # pt9 is LHS left bottom channel
    pt9x = -1*lcd
    pt9z = hcd
    pt9y = 0

    # pt10 is LHS top left channel
    pt10x = -1*lcd
    pt10z = hc + hcd # channel height plus height of cone deck
    pt10y = 0

    # pt 11 is LHS top right channel
    pt11x = -1*lcd + wc
    pt11z = hc + hcd
    pt11y = 0

    # pt 12 is RHS top right channel
    pt12x = Dc + (lcd-wc)
    pt12z = hc + hcd
    pt12y = 0

    # pt13 is RHS top right channel
    pt13x = Dc + lcd
    pt13z = hc + hcd
    pt13y = 0

    # pt14 is LHS bottom inner channel wall
    pt14x = -1*lcd + wc
    pt14z = hcd + psp
    pt14y = 0

    #pt 15 is RHS bottom inner channel wall
    pt15x = Dc + (lcd-wc)
    pt15z = hcd + psp
    pt15y = 0

    # Convert the Q_100 to flow velocity:
    A_secondary = 3.1415923*(dfd**2) # Area of circle
    U_100 = Q_100*A_secondary
    Q_100 = U_100 # Reassign

    return pt0x, pt0z, pt0y, pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, Q_100

# Create additional front face points including wood zone
def create_fuel_blocks(pt0x, pt1x):
    """
    Creates geometry for the fuel block with the following assumptions:  Rectangular fuel source, Centered along the vertical axis of the combustion chamber, Width of fuel block is half the diameter of the combustion chamber, Assumed fuel height of 3 inches (0.0762 m), bottom of the fuel is 3 inches off the ground.

    Args:

        pt0x (float): origin x-coordinate of cookstove geometry
        pt1x (float): Bottom east vertice of cookstove combustion chamber

     Returns:

         points (float): x,y,z coordinates of the wood fuel block

    """
    fuel_width = 0.5*(pt1x - pt0x)
    fuel_x_center = fuel_width
    fuel_x_left_coord = fuel_x_center - (fuel_width)/2
    fuel_x_right_coord = fuel_x_center + (fuel_width)/2
    fuel_height = 0.02 # [m]
    fuel_bottom_coords = 0.02
    fuel_top_coords = fuel_bottom_coords + fuel_height
    pt16x = fuel_x_left_coord
    pt17x = fuel_x_right_coord
    pt18x = fuel_x_right_coord
    pt19x = fuel_x_left_coord
    pt16z = fuel_bottom_coords
    pt17z = fuel_bottom_coords
    pt18z = fuel_top_coords
    pt19z = fuel_top_coords
    pt16y = 0
    pt17y = 0
    pt18y = 0
    pt19y = 0
    return pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y

# 20 defined by 6x and 14z
# 21 defined by 7x and 15z
# 44 defined by 14x and 9z
# 46 defined by 15x and 8z

def create_primary_inlets(Dc, Q_primary, N_holes, D_holes, shift_str, shift, shift_positive):
    """Create the four equally spaced primary fuel inlets based on user definition.
    Args:
    Dc (double): Diameter of combustion chamber as defined by user in input.yaml
    Q_primary (double): Primary flow rate as defined by user in input.yaml
    N_holes (int): Number of holes in air tray as defined by user
    D_holes (double): Diameter of holes in the air tray

    Returns:
    pt52str (str): vertice along bottom of primary inlet
    pt53str (str): vertice along bottom of primary inlet
    pt54str (str): vertice along bottom of primary inlet
    pt55str (str): vertice along bottom of primary inlet
    pt56str (str): vertice along bottom of primary inlet
    pt57str (str): vertice along bottom of primary inlet
    pt58str (str): vertice along bottom of primary inlet
    pt59str (str): vertice along bottom of primary inlet


    pt60str (str): back vertice along bottom of primary inlet
    pt61str (str): back vertice along bottom of primary inlet
    pt62str (str): back vertice along bottom of primary inlet
    pt63str (str): back vertice along bottom of primary inlet
    pt64str (str): back vertice along bottom of primary inlet
    pt65str (str): back vertice along bottom of primary inlet
    pt66str (str): back vertice along bottom of primary inlet
    pt67str (str): back vertice along bottom of primary inlet


    pt68str (str): Shifted vertice along the bottom of the body
    pt69str (str): Shifted vertice along the bottom of the body
    pt70str (str): Shifted vertice along the bottom of the body
    pt71str (str): Shifted vertice along the bottom of the body
    pt72str (str): Shifted vertice along the bottom of the body
    pt73str (str): Shifted vertice along the bottom of the body
    pt74str (str): Shifted vertice along the bottom of the body
    pt75str (str): Shifted vertice along the bottom of the body
    pt76str (str): Shifted vertice along the bottom of the body
    pt77str (str): Shifted vertice along the bottom of the body
    pt78str (str): Shifted vertice along the bottom of the body
    pt79str (str): Shifted vertice along the bottom of the body
    pt80str (str): Shifted vertice along the bottom of the body
    pt81str (str): Shifted vertice along the bottom of the body
    pt82str (str): Shifted vertice along the bottom of the body
    pt83str (str): Shifted vertice along the bottom of the body
    V_primary_model (double): Primary velocity through each of the inlets
    V_primary_model_str (str): String version of primary velocity through each inlet

    """


    N_inlets = 4 # Number of inlets to be modelled
    N_spaces = N_inlets + 1 # Number of stove body segments along the bottom of C-chamber
    N_segments = N_inlets + N_spaces # total number of equally spaced segments along bottom of domain
    size_segments = Dc/N_segments # Used for creating vertices


    # Computing the sum of average flow velocities through air tray assuming equal flow distrobution for air tray
    A_hole = 3.1415926*0.25*(D_holes**2) # Area of individual hole in air tray
    v_sum_airtray = Q_primary*N_holes*A_hole


    # Computing the bulk velocity through the four inlets included in the CFD model
    V_primary_model = v_sum_airtray/N_inlets
    V_primary_model_str = str(V_primary_model)[:10]
    # Now, creating the vertices for the geometry
    # Example: pt1xstr= str(pt1x)[:5]

    print("size segments diameter")
    print(size_segments)
    sleep(10)
    pt52xstr = str(size_segments)[:5]
    pt52ystr = str(0)
    pt52zstr = str(0)

    pt53xstr = str(2*size_segments)[:5]
    pt53ystr = str(0)
    pt53zstr = str(0)
    pt53x = 2*size_segments

    pt54xstr = str(3*size_segments)[:5]
    pt54ystr = str(0)
    pt54zstr = str(0)
    pt54x = 3*size_segments

    pt55xstr = str(4*size_segments)[:5]
    pt55ystr = str(0)
    pt55zstr = str(0)

    pt56xstr = str(5*size_segments)[:5]
    pt56ystr = str(0)
    pt56zstr = str(0)

    pt57xstr = str(6*size_segments)[:5]
    pt57ystr = str(0)
    pt57zstr = str(0)

    pt58xstr = str(7*size_segments)[:5]
    pt58ystr = str(0)
    pt58zstr = str(0)

    pt59xstr = str(8*size_segments)[:5]
    pt59ystr = str(0)
    pt59zstr = str(0)

    # Back points -- make sure the shift is defned prior to this function
    pt60xstr = str(1*size_segments)[:5]
    pt60ystr = str(shift)[:5]
    pt60zstr = str(0)

    pt61xstr = str(2*size_segments)[:5]
    pt61ystr = str(shift)[:5]
    pt61zstr = str(0)

    pt62xstr = str(3*size_segments)[:5]
    pt62ystr = str(shift)[:5]
    pt62zstr = str(0)

    pt63xstr = str(4*size_segments)[:5]
    pt63ystr = str(shift)[:5]
    pt63zstr = str(0)

    pt64xstr = str(5*size_segments)[:5]
    pt64ystr = str(shift)[:5]
    pt64zstr = str(0)

    pt65xstr = str(6*size_segments)[:5]
    pt65ystr = str(shift)[:5]
    pt65zstr = str(0)

    pt66xstr = str(7*size_segments)[:5]
    pt66ystr = str(shift)[:5]
    pt66zstr = str(0)

    pt67xstr = str(8*size_segments)[:5]
    pt67ystr = str(shift)[:5]
    pt67zstr = str(0)

    # Concatenate into vertice strings
    # example pt51str = "(" + shift_str + " " + pt50xstr + " " + pt50zstr + ")"
    pt52str = "(" + pt52ystr + " " + pt52xstr + " " + pt52zstr + ")"
    pt53str = "(" + pt53ystr + " " + pt53xstr + " " + pt53zstr + ")"
    pt54str = "(" + pt54ystr + " " + pt54xstr + " " + pt54zstr + ")"
    pt55str = "(" + pt55ystr + " " + pt55xstr + " " + pt55zstr + ")"
    pt56str = "(" + pt56ystr + " " + pt56xstr + " " + pt56zstr + ")"
    pt57str = "(" + pt57ystr + " " + pt57xstr + " " + pt57zstr + ")"
    pt58str = "(" + pt58ystr + " " + pt58xstr + " " + pt58zstr + ")"
    pt59str = "(" + pt59ystr + " " + pt59xstr + " " + pt59zstr + ")"

    pt60str = "(" + shift_str + " " + pt60xstr + " " + pt60zstr + ")"
    pt61str = "(" + shift_str + " " + pt61xstr + " " + pt61zstr + ")"
    pt62str = "(" + shift_str + " " + pt62xstr + " " + pt62zstr + ")"
    pt63str = "(" + shift_str + " " + pt63xstr + " " + pt63zstr + ")"
    pt64str = "(" + shift_str + " " + pt64xstr + " " + pt64zstr + ")"
    pt65str = "(" + shift_str + " " + pt65xstr + " " + pt65zstr + ")"
    pt66str = "(" + shift_str + " " + pt66xstr + " " + pt66zstr + ")"
    pt67str = "(" + shift_str + " " + pt67xstr + " " + pt67zstr + ")"

    # Shifting vertically for the top of each inlet block
    pt68str = "(" + pt52ystr + " " + pt52xstr + " " + shift_str + ")"
    pt69str = "(" + pt53ystr + " " + pt53xstr + " " + shift_str + ")"
    pt70str = "(" + pt54ystr + " " + pt54xstr + " " + shift_str + ")"
    pt71str = "(" + pt55ystr + " " + pt55xstr + " " + shift_str + ")"
    pt72str = "(" + pt56ystr + " " + pt56xstr + " " + shift_str + ")"
    pt73str = "(" + pt57ystr + " " + pt57xstr + " " + shift_str + ")"
    pt74str = "(" + pt58ystr + " " + pt58xstr + " " + shift_str + ")"
    pt75str = "(" + pt59ystr + " " + pt59xstr + " " + shift_str + ")"

    pt76str = "(" + shift_str + " " + pt60xstr + " " + shift_str + ")"
    pt77str = "(" + shift_str + " " + pt61xstr + " " + shift_str + ")"
    pt78str = "(" + shift_str + " " + pt62xstr + " " + shift_str + ")"
    pt79str = "(" + shift_str + " " + pt63xstr + " " + shift_str + ")"
    pt80str = "(" + shift_str + " " + pt64xstr + " " + shift_str + ")"
    pt81str = "(" + shift_str + " " + pt65xstr + " " + shift_str + ")"
    pt82str = "(" + shift_str + " " + pt66xstr + " " + shift_str + ")"
    pt83str = "(" + shift_str + " " + pt67xstr + " " + shift_str + ")"

    # creating outer points

    # LHS front
    pt84xstr = str(0)
    pt84zstr = str(-1*shift/2)
    pt84ystr = pt52ystr
    # LHS back
    pt85xstr = str(0)
    pt85zstr = str(-1*shift/2)
    pt85ystr = shift_str
    # RHS Front
    pt86xstr = str(Dc)
    pt86zstr = str(-1*shift/2)
    pt86ystr = pt59ystr
    # RHS back
    pt87xstr = str(Dc)
    pt87zstr = str(-1*shift/2)
    pt87ystr = shift_str

    # LHS short boundary
    # Front
    pt88xstr = pt52xstr
    pt88ystr = pt52ystr
    pt88zstr = str(-1*shift/2)
    # Back
    pt89xstr = pt52xstr
    pt89ystr = shift_str
    pt89zstr = str(-1*shift/2)

    # RHS short boundary
    pt90xstr = pt59xstr
    pt90ystr = pt52ystr
    pt90zstr = str(-1*shift/2)
    # Back
    pt91xstr = pt59xstr
    pt91ystr = shift_str
    pt91zstr = str(-1*shift/2)

    # Should this work, need to go create the block vertices for the 3 inner sections
    pt84str = "(" + pt84ystr + " " + pt84xstr + " " + pt84zstr + ")"
    pt85str = "(" + pt85ystr + " " + pt85xstr + " " + pt85zstr + ")"
    pt86str = "(" + pt86ystr + " " + pt86xstr + " " + pt86zstr + ")"
    pt87str = "(" + pt87ystr + " " + pt87xstr + " " + pt87zstr + ")"
    # The short shifts on the outer primary inlets
    pt88str = "(" + pt88ystr + " " + pt88xstr + " " + pt88zstr + ")"
    pt89str = "(" + pt89ystr + " " + pt89xstr + " " + pt89zstr + ")"
    pt90str = "(" + pt90ystr + " " + pt90xstr + " " + pt90zstr + ")"
    pt91str = "(" + pt91ystr + " " + pt91xstr + " " + pt91zstr + ")"

    # Inner section 1 l
    pt92xstr = pt53xstr
    pt92ystr = pt53ystr
    pt92zstr = str(-1*shift/2)
    pt93xstr = pt54xstr
    pt93ystr = pt54ystr
    pt93zstr = str(-1*shift/2)
    pt94xstr = pt62xstr
    pt94ystr = shift_str
    pt94zstr = str(-1*shift/2)
    pt95xstr = pt61xstr
    pt95ystr = shift_str
    pt95zstr = str(-1*shift/2)


    # ----------Inner section 2
    pt96xstr = pt55xstr
    pt96ystr = pt55ystr
    pt96zstr = str(-1*shift/2)
    pt97xstr = pt56xstr
    pt97ystr = pt56ystr
    pt97zstr = str(-1*shift/2)
    pt98xstr = pt64xstr
    pt98ystr = shift_str
    pt98zstr = str(-1*shift/2)
    pt99xstr = pt63xstr
    pt99ystr = shift_str
    pt99zstr = str(-1*shift/2)

    # ----------Inner section 3 R
    pt100xstr = pt57xstr
    pt100ystr = pt57ystr
    pt100zstr = str(-1*shift/2)
    pt101xstr = pt58xstr
    pt101ystr = pt58ystr
    pt101zstr = str(-1*shift/2)
    pt102xstr = pt66xstr
    pt102ystr = shift_str
    pt102zstr = str(-1*shift/2)
    pt103xstr = pt65xstr
    pt103ystr = shift_str
    pt103zstr = str(-1*shift/2)

    # concatenate the primary inlet strings:
    pt92str = "(" + pt92ystr + " " + pt92xstr + " " + pt92zstr + ")"
    pt93str = "(" + pt93ystr + " " + pt93xstr + " " + pt93zstr + ")"
    pt94str = "(" + pt94ystr + " " + pt94xstr + " " + pt94zstr + ")"
    pt95str = "(" + pt95ystr + " " + pt95xstr + " " + pt95zstr + ")"
    pt96str = "(" + pt96ystr + " " + pt96xstr + " " + pt96zstr + ")"
    pt97str = "(" + pt97ystr + " " + pt97xstr + " " + pt97zstr + ")"
    pt98str = "(" + pt98ystr + " " + pt98xstr + " " + pt98zstr + ")"
    pt99str = "(" + pt99ystr + " " + pt99xstr + " " + pt99zstr + ")"
    pt100str = "(" + pt100ystr + " " + pt100xstr + " " + pt100zstr + ")"
    pt101str = "(" + pt101ystr + " " + pt101xstr + " " + pt101zstr + ")"
    pt102str = "(" + pt102ystr + " " + pt102xstr + " " + pt102zstr + ")"
    pt103str = "(" + pt103ystr + " " + pt103xstr + " " + pt103zstr + ")"


    return pt52str, pt53str, pt54str, pt55str, pt56str, pt57str, pt58str, pt59str, pt60str, pt61str, pt62str, pt63str, pt64str, pt65str, pt66str, pt67str, pt68str, pt69str, pt70str, pt71str, pt72str, pt73str, pt74str, pt75str, pt76str, pt77str, pt78str, pt79str, pt80str, pt81str, pt82str, pt83str, pt84str, pt85str, pt86str, pt87str, pt88str, pt89str, pt90str, pt91str, pt92str, pt93str, pt94str, pt95str, pt96str, pt97str, pt98str, pt99str, pt100str, pt101str, pt102str, pt103str, pt53x, pt54x, V_primary_model, V_primary_model_str




def correct_primary_flow(Q_primary, N_holes, D_holes, pt53x, pt54x):
    """Compute the primary flow velocites, assuming uniform flow in each primary inlet
    Args:
    Q_primary (double): total primary air flow rate input by user
    N_holes (int): Number of holes in air tray input by user
    D_holes (double): Diameter of primary inlet holes in air tray
    pt53x (double): LHS inlet x-coordinate primary hole
    pt54x (double): RHS inlet x-coordinate primary hole

    Returns:
    Q_per (double): Primary flow rate distributed to each inlet
    V_primary (double): Velocity through primary inlets
    A_primary (double): Areas of primary inlets
    diam_primary (double): Diameter of the primary inlet holes in the model
    """
    Q_per = Q_primary/3 # Evenly distributed
    diam_primary = pt54x-pt53x # Difference is the diameter
    A_primary = (3.1415926/4)*diam_primary**2 # Area of each primary inlet
    V_primary = Q_per*A_primary # Velocity through each of the inlets
    return Q_per, V_primary, A_primary, diam_primary


def create_additional_front_points(pt6x, pt7x, pt14x, pt9z, pt15x, pt8z, pt14z, pt9x, pt8x, pt15z):
    """
    Create pot surface points to create faces--Naming them 21(L)-22(R) to not collide with current fuel vert numbers

    Args:
        points (float): cookstove geometry

    Returns:

        points (float): series of points created as the back plane of the stove. Used to create a 2D geometry


    """
    # Left point
    pt20x = pt6x
    pt20z = pt14z
    pt20y = 0
    # Right point
    pt21x = pt7x
    pt21z = pt15z
    pt21y = 0

    pt44x = pt14x
    pt44z = pt9z
    pt44y = 0

    pt46x = pt15x
    pt46z = pt8z
    pt46y = 0

    pt48x = pt9x
    pt48z = pt14z
    pt48y = 0

    pt50x =  pt8x
    pt50z = pt15z
    pt50y = 0


    return pt48x, pt48z, pt48y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt50x, pt50z, pt50y

# Stove front (0-15), wood front (16-19), additional points front (20,21,44,46)
def points_to_strings(pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, pt0x, pt0z, pt0y, pt17x, pt18x, pt19x, pt16x, pt17z, pt18z, pt19z, pt16z, pt17y, pt18y, pt19y, pt16y, pt20x, pt20z, pt20y, pt21x, pt21z, pt21y, pt44x, pt44z, pt44y, pt46x, pt46z, pt46y, pt48x, pt48y, pt48z, pt50x, pt50y, pt50z):
    """
    Take in the raw vertice information from spreadsheet, and format the floats into strings->For front vertices

    Args:
        points (float): all front coordinates

    Returns:
        points as strings (str): Coordinates converted to strings compatible with openfoam convention (length 5).


    """
    pt0xstr= str(pt0x)[:5]
    pt0zstr = str(pt0z)[:5]
    pt0ystr = str(pt0y)[:5]

    print("pt0xstr from ponts to strings")
    print(pt0xstr)

    print("pt0zstr from ponts to strings")
    print(pt0zstr)

    print("pt0ystr from ponts to strings")
    print(pt0ystr)

    pt1xstr= str(pt1x)[:5]
    pt1zstr = str(pt1z)[:5]
    pt1ystr = str(pt1y)[:5]
    pt2xstr= str(pt2x)[:5]
    pt2zstr = str(pt2z)[:5]
    pt2ystr = str(pt2y)[:5]
    pt3xstr= str(pt3x)[:5]
    pt3zstr = str(pt3z)[:5]
    pt3ystr = str(pt3y)[:5]
    pt4xstr= str(pt4x)[:5]
    pt4zstr = str(pt4z)[:5]
    pt4ystr = str(pt4y)[:5]
    pt5xstr= str(pt5x)[:5]
    pt5zstr = str(pt5z)[:5]
    pt5ystr = str(pt5y)[:5]
    pt6xstr= str(pt6x)[:5]
    pt6zstr = str(pt6z)[:5]
    pt6ystr = str(pt6y)[:5]
    pt7xstr= str(pt7x)[:5]
    pt7zstr = str(pt7z)[:5]
    pt7ystr = str(pt7y)[:5]
    pt8xstr= str(pt8x)[:5]
    pt8zstr = str(pt8z)[:5]
    pt8ystr = str(pt8y)[:5]
    pt9xstr= str(pt9x)[:5]
    pt9zstr = str(pt9z)[:5]
    pt9ystr = str(pt9y)[:5]
    pt10xstr= str(pt10x)[:5]
    pt10zstr = str(pt10z)[:5]
    pt10ystr = str(pt10y)[:5]
    pt11xstr= str(pt11x)[:5]
    pt11zstr = str(pt11z)[:5]
    pt11ystr = str(pt11y)[:5]
    pt12xstr= str(pt12x)[:5]
    pt12zstr = str(pt12z)[:5]
    pt12ystr = str(pt12y)[:5]
    pt13xstr= str(pt13x)[:5]
    pt13zstr = str(pt13z)[:5]
    pt13ystr = str(pt13y)[:5]
    pt14xstr= str(pt14x)[:5]
    pt14zstr = str(pt14z)[:5]
    pt14ystr = str(pt14y)[:5]
    pt15xstr= str(pt15x)[:5]
    pt15zstr = str(pt15z)[:5]
    pt15ystr = str(pt15y)[:5]

    pt16xstr= str(pt16x)[:5]
    pt16zstr = str(pt16z)[:5]
    pt16ystr = str(pt16y)[:5]
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
    pt21xstr= str(pt21x)[:5]
    pt21zstr = str(pt21z)[:5]
    pt21ystr = str(pt21y)[:5]
    pt44xstr= str(pt44x)[:5]
    pt44zstr = str(pt44z)[:5]
    pt44ystr = str(pt44y)[:5]
    pt46xstr= str(pt46x)[:5]
    pt46zstr = str(pt46z)[:5]
    pt46ystr = str(pt46y)[:5]

    pt48xstr= str(pt48x)[:5]
    pt48zstr = str(pt48z)[:5]
    pt48ystr = str(pt48y)[:5]

    pt50xstr= str(pt50x)[:5]
    pt50zstr = str(pt50z)[:5]
    pt50ystr = str(pt50y)[:5]
    return pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr


# Stove front (0-15), wood front (16-19), additional points front (20,21,44,46)
# x = x1, y = x2, z = x3 coordinates based on OpenFOAM convention
def vertice_concatenate(pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50zstr, pt50ystr):
    """
    Convert the individual vertex strings and concatenate to the format required for blockmeshdict file

    Args:
        points as strings (str): Coordinates converted to strings compatible with openfoam convention (length 5).

    Returns:
        concatenated front points (str): The x,y,z values of front points concatenated into single vertice location


    """
    # Stove Body
    pt0str = "(" + pt0ystr + " " + pt0xstr + " " + pt0zstr + ")"
    pt1str = "(" + pt1ystr + " " + pt1xstr + " " + pt1zstr + ")"
    pt2str = "(" + pt2ystr + " " + pt2xstr + " " + pt2zstr + ")"
    pt3str = "(" + pt3ystr + " " + pt3xstr + " " + pt3zstr + ")"
    pt4str = "(" + pt4ystr + " " + pt4xstr + " " + pt4zstr + ")"
    pt5str = "(" + pt5ystr + " " + pt5xstr + " " + pt5zstr + ")"
    pt6str = "(" + pt6ystr + " " + pt6xstr + " " + pt6zstr + ")"
    pt7str = "(" + pt7ystr + " " + pt7xstr + " " + pt7zstr + ")"
    pt8str = "(" + pt8ystr + " " + pt8xstr + " " + pt8zstr + ")"
    pt9str = "(" + pt9ystr + " " + pt9xstr + " " + pt9zstr + ")"
    pt10str = "(" + pt10ystr + " " + pt10xstr + " " + pt10zstr + ")"
    pt11str = "(" + pt11ystr + " " + pt11xstr + " " + pt11zstr + ")"
    pt12str = "(" + pt12ystr + " " + pt12xstr + " " + pt12zstr + ")"
    pt13str = "(" + pt13ystr + " " + pt13xstr + " " + pt13zstr + ")"
    pt14str = "(" + pt14ystr + " " + pt14xstr + " " + pt14zstr + ")"
    pt15str = "(" + pt15ystr + " " + pt15xstr + " " + pt15zstr + ")"

    # Wood
    pt16str = "(" + pt16ystr + " " + pt16xstr + " " + pt16zstr + ")"
    pt17str = "(" + pt17ystr + " " + pt17xstr + " " + pt17zstr + ")"
    pt18str = "(" + pt18ystr + " " + pt18xstr + " " + pt18zstr + ")"
    pt19str = "(" + pt19ystr + " " + pt19xstr + " " + pt19zstr + ")"

    # Additional front pts
    pt20str = "(" + pt20ystr + " " + pt20xstr + " " + pt20zstr + ")"
    pt21str = "(" + pt21ystr + " " + pt21xstr + " " + pt21zstr + ")"
    pt44str = "(" + pt44ystr + " " + pt44xstr + " " + pt44zstr + ")"
    pt46str = "(" + pt46ystr + " " + pt46xstr + " " + pt46zstr + ")"
    pt48str = "(" + pt48ystr + " " + pt48xstr + " " + pt48zstr + ")"
    pt50str = "(" + pt50ystr + " " + pt50xstr + " " + pt50zstr + ")"

    return pt0str, pt1str, pt2str, pt3str, pt4str, pt5str, pt6str, pt7str, pt8str, pt9str, pt10str, pt11str, pt12str, pt13str, pt14str, pt15str, pt16str, pt17str, pt18str, pt19str, pt20str, pt21str, pt44str, pt46str, pt48str, pt50str


def create_three_fuel_blocks(Dc, stick_width, shift_str):
    """Create the three wood stick vertices for pyrolysis gas release
    Args:
    Dc (double): Combustion chamber Diameter supplied by User
    stick_width (double): Wood stick dimension supplied by user
    shift_str (str): Distance shifted in the y-direction to create the back face of the cookstove

    Returns:
    pt104str through pt123str (str): Vertices required for fuel block definition
    stick_pitch (double): Pitch between sticks computed based on 3 sticks equally spaced in Dc combustion diam
    stick_bottom (double): z-coordinate associated with bottom of N_sticks
    stick_top (double): z-coordinate associated with top of N_sticks
    """

    # Assumed stick height
    height_stick = 0.02 # [m] Height of the bottom of the sticks from the datum ASSUMED
    stick_bottom = height_stick
    stick_top = stick_bottom + stick_width

    # Computing pitch
    N_sticks = 3 # Held constant for analysis
    stick_pitch = Dc/(N_sticks+1)

    # Wood block 1:
    # bottom
    pt104x = stick_pitch-0.5*(stick_width)
    pt104z = stick_bottom
    pt104y = 0
    pt105x = pt104x + stick_width
    pt105z = stick_bottom
    pt105y = 0
    pt106x = pt105x
    pt106z = stick_bottom
    pt106y = shift_str
    pt107x = pt104x
    pt107z = stick_bottom
    pt107y = shift_str
    # Top
    pt108x = pt104x
    pt108z = stick_top
    pt108y = 0
    pt109x = pt105x
    pt109z = stick_top
    pt109y = 0
    pt110x = pt109x
    pt110z = stick_top
    pt110y = shift_str
    pt111x = pt104x
    pt111z = stick_top
    pt111y = shift_str

    # Wood block 2
    # bottom
    pt112x = pt104x + stick_pitch
    pt112z = stick_bottom
    pt112y = 0
    pt113x = pt112x + stick_width
    pt113z = stick_bottom
    pt113y = 0
    pt114x = pt113x
    pt114z = stick_bottom
    pt114y = shift_str
    pt115x = pt112x
    pt115z = stick_bottom
    pt115y = shift_str
    # Top
    pt116x = pt112x
    pt116z = stick_top
    pt116y = 0
    pt117x = pt113x
    pt117z = stick_top
    pt117y = 0
    pt118x = pt114x
    pt118z = stick_top
    pt118y = shift_str
    pt119x = pt115x
    pt119z = stick_top
    pt119y = shift_str

    # Wood block 3
    # bottom
    pt120x = pt112x + stick_pitch
    pt120z = stick_bottom
    pt120y = 0
    pt121x = pt120x + stick_width
    pt121z = stick_bottom
    pt121y = 0
    pt122x = pt121x
    pt122z = stick_bottom
    pt122y = shift_str
    pt123x = pt120x
    pt123z = stick_bottom
    pt123y = shift_str
    # Top
    pt124x = pt120x
    pt124z = stick_top
    pt124y = 0
    pt125x = pt121x
    pt125z = stick_top
    pt125y = 0
    pt126x = pt122x
    pt126z = stick_top
    pt126y = shift_str
    pt127x = pt120x
    pt127z = stick_top
    pt127y = shift_str

    # Convert individual coordinates to strings of length 5
    pt104xstr = str(pt104x)[:5]
    pt104zstr = str(pt104z)[:5]
    pt104ystr = str(pt104y)[:5]
    pt105xstr = str(pt105x)[:5]
    pt105zstr = str(pt105z)[:5]
    pt105ystr = str(pt105y)[:5]
    pt106xstr = str(pt106x)[:5]
    pt106zstr = str(pt106z)[:5]
    pt106ystr = str(pt106y)[:5]
    pt107xstr = str(pt107x)[:5]
    pt107zstr = str(pt107z)[:5]
    pt107ystr = str(pt107y)[:5]
    pt108xstr = str(pt108x)[:5]
    pt108zstr = str(pt108z)[:5]
    pt108ystr = str(pt108y)[:5]
    pt109xstr = str(pt109x)[:5]
    pt109zstr = str(pt109z)[:5]
    pt109ystr = str(pt109y)[:5]
    pt110xstr = str(pt110x)[:5]
    pt110zstr = str(pt110z)[:5]
    pt110ystr = str(pt110y)[:5]
    pt111xstr = str(pt111x)[:5]
    pt111zstr = str(pt111z)[:5]
    pt111ystr = str(pt111y)[:5]
    pt112xstr = str(pt112x)[:5]
    pt112zstr = str(pt112z)[:5]
    pt112ystr = str(pt112y)[:5]
    pt113xstr = str(pt113x)[:5]
    pt113zstr = str(pt113z)[:5]
    pt113ystr = str(pt113y)[:5]
    pt114xstr = str(pt114x)[:5]
    pt114zstr = str(pt114z)[:5]
    pt114ystr = str(pt114y)[:5]
    pt115xstr = str(pt115x)[:5]
    pt115zstr = str(pt115z)[:5]
    pt115ystr = str(pt115y)[:5]
    pt116xstr = str(pt116x)[:5]
    pt116zstr = str(pt116z)[:5]
    pt116ystr = str(pt116y)[:5]

    pt117xstr = str(pt117x)[:5]
    pt117zstr = str(pt117z)[:5]
    pt117ystr = str(pt117y)[:5]
    pt118xstr = str(pt118x)[:5]
    pt118zstr = str(pt118z)[:5]
    pt118ystr = str(pt118y)[:5]
    pt119xstr = str(pt119x)[:5]
    pt119zstr = str(pt119z)[:5]
    pt119ystr = str(pt119y)[:5]
    pt120xstr = str(pt120x)[:5]
    pt120zstr = str(pt120z)[:5]
    pt120ystr = str(pt120y)[:5]
    pt121xstr = str(pt121x)[:5]
    pt121zstr = str(pt121z)[:5]
    pt121ystr = str(pt121y)[:5]
    pt122xstr = str(pt122x)[:5]
    pt122zstr = str(pt122z)[:5]
    pt122ystr = str(pt122y)[:5]
    pt123xstr = str(pt123x)[:5]
    pt123zstr = str(pt123z)[:5]
    pt123ystr = str(pt123y)[:5]
    pt124xstr = str(pt124x)[:5]
    pt124zstr = str(pt124z)[:5]
    pt124ystr = str(pt124y)[:5]
    pt125xstr = str(pt125x)[:5]
    pt125zstr = str(pt125z)[:5]
    pt125ystr = str(pt125y)[:5]
    pt126xstr = str(pt126x)[:5]
    pt126zstr = str(pt126z)[:5]
    pt126ystr = str(pt126y)[:5]
    pt127xstr = str(pt127x)[:5]
    pt127zstr = str(pt127z)[:5]
    pt127ystr = str(pt127y)[:5]

    # Concatenating coordinates
    pt104str = "(" + pt104ystr + " " + pt104xstr + " " + pt104zstr + ")"
    pt105str = "(" + pt105ystr + " " + pt105xstr + " " + pt105zstr + ")"
    pt106str = "(" + pt106ystr + " " + pt106xstr + " " + pt106zstr + ")"
    pt107str = "(" + pt107ystr + " " + pt107xstr + " " + pt107zstr + ")"
    pt108str = "(" + pt108ystr + " " + pt108xstr + " " + pt108zstr + ")"
    pt109str = "(" + pt109ystr + " " + pt109xstr + " " + pt109zstr + ")"
    pt110str = "(" + pt110ystr + " " + pt110xstr + " " + pt110zstr + ")"
    pt111str = "(" + pt111ystr + " " + pt111xstr + " " + pt111zstr + ")"
    pt112str = "(" + pt112ystr + " " + pt112xstr + " " + pt112zstr + ")"
    pt113str = "(" + pt113ystr + " " + pt113xstr + " " + pt113zstr + ")"
    pt114str = "(" + pt114ystr + " " + pt114xstr + " " + pt114zstr + ")"
    pt115str = "(" + pt115ystr + " " + pt115xstr + " " + pt115zstr + ")"
    pt116str = "(" + pt116ystr + " " + pt116xstr + " " + pt116zstr + ")"
    pt117str = "(" + pt117ystr + " " + pt117xstr + " " + pt117zstr + ")"
    pt118str = "(" + pt118ystr + " " + pt118xstr + " " + pt118zstr + ")"
    pt119str = "(" + pt119ystr + " " + pt119xstr + " " + pt119zstr + ")"
    pt120str = "(" + pt120ystr + " " + pt120xstr + " " + pt120zstr + ")"
    pt121str = "(" + pt121ystr + " " + pt121xstr + " " + pt121zstr + ")"
    pt122str = "(" + pt122ystr + " " + pt122xstr + " " + pt122zstr + ")"
    pt123str = "(" + pt123ystr + " " + pt123xstr + " " + pt123zstr + ")"
    pt124str = "(" + pt124ystr + " " + pt124xstr + " " + pt124zstr + ")"
    pt125str = "(" + pt125ystr + " " + pt125xstr + " " + pt125zstr + ")"
    pt126str = "(" + pt126ystr + " " + pt126xstr + " " + pt126zstr + ")"
    pt127str = "(" + pt127ystr + " " + pt127xstr + " " + pt127zstr + ")"

    return stick_pitch, stick_bottom, stick_top, pt104str, pt105str, pt106str, pt107str, pt108str, pt109str, pt110str, pt111str, pt112str, pt113str, pt114str, pt115str, pt116str, pt117str, pt118str, pt119str, pt120str, pt121str, pt122str, pt123str, pt124str, pt125str, pt126str, pt127str



def create_back_points(shift, pt1xstr, pt1zstr, pt1ystr, pt2xstr, pt2zstr, pt2ystr, pt3xstr, pt3zstr, pt3ystr, pt4xstr, pt4zstr, pt4ystr, pt5xstr, pt5zstr, pt5ystr, pt6xstr, pt6zstr, pt6ystr, pt7xstr, pt7zstr, pt7ystr, pt8xstr, pt8zstr, pt8ystr, pt9xstr, pt9zstr, pt9ystr, pt10xstr, pt10zstr, pt10ystr, pt11xstr, pt11zstr, pt11ystr, pt12xstr, pt12zstr, pt12ystr, pt13xstr, pt13zstr, pt13ystr,  pt14xstr, pt14zstr, pt14ystr, pt15xstr, pt15zstr, pt15ystr, pt0xstr, pt0zstr, pt0ystr, pt16xstr, pt16zstr, pt16ystr, pt17xstr, pt17zstr, pt17ystr, pt18xstr, pt18zstr, pt18ystr, pt19xstr, pt19zstr, pt19ystr, pt20xstr, pt20zstr, pt20ystr, pt21xstr, pt21zstr, pt21ystr, pt44xstr, pt44zstr, pt44ystr, pt46xstr, pt46zstr, pt46ystr, pt48xstr, pt48zstr, pt48ystr, pt50xstr, pt50ystr, pt50zstr):
    """
    Back coordinates of the cookstove--simply shifting the x2 (y) coordinate back by a value shift

    Args:
        concatenated back points (str): The x,y,z values of back points concatenated into single vertice location


    """
    if shift > 0:
        shift = shift*(-1)
        print('Shift multiplied by -1')
    elif shift == 0:
        print('Shift is equal to zero: get ready for some errors')
    elif shift < 0:
        print('Shift is less than zero naturally')
    shift_str = str(shift)[:5] # converting to string

    # Stove Body--back
    pt22str = "(" + shift_str + " " + pt0xstr + " " + pt0zstr + ")"
    pt23str = "(" + shift_str + " " + pt1xstr + " " + pt1zstr + ")"
    pt24str = "(" + shift_str + " " + pt2xstr + " " + pt2zstr + ")"
    pt25str = "(" + shift_str + " " + pt3xstr + " " + pt3zstr + ")"
    pt26str = "(" + shift_str + " " + pt4xstr + " " + pt4zstr + ")"
    pt27str = "(" + shift_str + " " + pt5xstr + " " + pt5zstr + ")"
    pt28str = "(" + shift_str + " " + pt6xstr + " " + pt6zstr + ")"
    pt29str = "(" + shift_str + " " + pt7xstr + " " + pt7zstr + ")"
    pt30str = "(" + shift_str + " " + pt8xstr + " " + pt8zstr + ")"
    pt31str = "(" + shift_str + " " + pt9xstr + " " + pt9zstr + ")"
    pt32str = "(" + shift_str + " " + pt10xstr + " " + pt10zstr + ")"
    pt33str = "(" + shift_str + " " + pt11xstr + " " + pt11zstr + ")"
    pt34str = "(" + shift_str + " " + pt12xstr + " " + pt12zstr + ")"
    pt35str = "(" + shift_str + " " + pt13xstr + " " + pt13zstr + ")"
    pt36str = "(" + shift_str + " " + pt14xstr + " " + pt14zstr + ")"
    pt37str = "(" + shift_str + " " + pt15xstr + " " + pt15zstr + ")"

    # Wood
    pt38str = "(" + shift_str + " " + pt16xstr + " " + pt16zstr + ")"
    pt39str = "(" + shift_str + " " + pt17xstr + " " + pt17zstr + ")"
    pt40str = "(" + shift_str + " " + pt18xstr + " " + pt18zstr + ")"
    pt41str = "(" + shift_str + " " + pt19xstr + " " + pt19zstr + ")"

    # Additional front pts
    pt42str = "(" + shift_str + " " + pt20xstr + " " + pt20zstr + ")"
    pt43str = "(" + shift_str + " " + pt21xstr + " " + pt21zstr + ")"
    pt45str = "(" + shift_str + " " + pt44xstr + " " + pt44zstr + ")"
    pt47str = "(" + shift_str + " " + pt46xstr + " " + pt46zstr + ")"
    pt49str = "(" + shift_str + " " + pt48xstr + " " + pt48zstr + ")"
    pt51str = "(" + shift_str + " " + pt50xstr + " " + pt50zstr + ")"

    return pt22str, pt23str, pt24str, pt25str, pt26str, pt27str, pt28str, pt29str, pt30str, pt31str, pt32str, pt33str, pt34str, pt35str, pt36str, pt37str, pt38str, pt39str, pt40str, pt41str, pt42str, pt43str, pt45str, pt47str, pt49str, pt51str, shift_str
