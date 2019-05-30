# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:18:31 2019

@author: Lee
"""

# Modules will pull all of the temperature versus time data from the original runs

# Should put the data into HDF5 tables as discussed in class

# Create a rank of the maximum average temperature (on full pot body)

# This needs to be a more dynamic module with values stored for future iteration

#Data import test: for 3 example files, pull expected first value, last value, and middle value

import os
from os import walk
from os import path
from sys import path
import numpy as np
import matplotlib.pyplot as plt
#import h5py

def data_import():
    """input a list of filenames to be pulled, put out an array of temperature data
    (1) search the foamfiles directory for fnames that start with case_ and tally the number for looping through the file
    (2) loop through each and pull data from the files (3) convert to numpy arrays (4) store"""
    # navigate to the foamfiles directory
    current_directory = os.getcwd()
    #foamfile_steps = "foamfiles\counterFlowFlame2D\"
    #foamfile_path = current_directory + foamfile_steps
    foamfile_path = "C:\\Oregon_State\\Spring_2019\\Soft_dev_eng\\StoveOpt\\foamfiles\\counterFlowFlame2D\\"  
    dir_list = [directory for directory in os.listdir(foamfile_path) if os.path.isdir(foamfile_path+directory)]     
    print(dir_list)
    length_dir_list = len(dir_list)
    print("The length of the dir list: " + str(length_dir_list))
    detect_prefix = 'case' # look for case prefix
    
    i = 0 # for looping
    case_counter = 0
    case_list = [None] # empty vector
    print(case_list)
    k = 0 # case list indices
    while i < length_dir_list:
        if dir_list[i].startswith(detect_prefix):
            print(dir_list[i])
            #case_counter = case_counter  + 1
            case_list_append = dir_list[i]
            case_list[k] = case_list.append(str(dir_list[i]))
            print("here is k: " + str(k))
            print("here is i: " + str(i))
            
            case_list[k] = dir_list[i]
            print("case list k")
            print(case_list[k])
            k = k+1
            print(case_list, sep = ", ")
        i = i+1
    
    # remove the final entry of the case_list vector
    case_list_length = len(case_list)
    print("case_list_length")
    print(case_list_length)
    omitted_value= case_list.pop(case_list_length-1)
    print("omitted value")
    print(omitted_value)
    print("Updated case list")
    print(case_list)
    
    # extract and go read data from each of the files
    """(1) Loop through the case_list produced, (2) pull the strings and 
    (3) add to the correct file extension. (4) open and read the data in.
    (5) create tables in numpy (potentially). (6) return the arrays in the overall function"""
    
    length_case_list = len(case_list)
    print("case list length: " + str(length_case_list))
    j = 0
    Temps = []
    Velocities = [] # reading in the 25-150 velocities
    list_temps = []
    list_velocities = []
    while j < length_case_list:
        fname = str(case_list[j]) # pull the case file name
        dir_steps = "\\postProcessing\\probes\\0\\"
        U_dir_steps = "\\0\\"
        U_fname = "details"
        Temp_fname = "T"
        full_path = foamfile_path + fname + dir_steps + Temp_fname # this will need to be edited for a more advanced file loc
        U_full_path = foamfile_path + fname + U_dir_steps + U_fname # varies for the cases (fname)
        with open(U_full_path, 'r') as f:
            f.seek(10) # position 10 is the beginning of line 2
            Velocity = f.readlines() # read line 2nd line
            print("Here is your velocity")
            print(Velocity) # seems to be working
            globals()['Velocities%s' % j] = Velocity # putting this into the Velocity matrix, renaming based on j to match cases
            list_velocities.append(globals()['Velocities%s' % j])

        globals()['Temps%s' % j] = np.loadtxt(fname = full_path)
        list_temps.append(globals()['Temps%s' % j])
        j = j+1
    print("here are the list temps: ")
    print(list_temps)
    print(Temps1)
    type_Temps1 = type(Temps1)
    print(type_Temps1)
    shape_Temp1 = Temps1.shape
    print("Temps1 size (rows by cols): " + str(shape_Temp1))
    print("Here is the velocity matrix for case 1")
    print(Velocities0) # solid
    
    # Concatenate all the temperatures
    """while the index is under the length of case list (# of temp vars) 
            add the temperature arrays to a list  (list temps)"""
    
    # Create list of the arrays
    """Temp_array_list = []
    while x < length_case_list:"""
    
    # Validates the list_temp is a group of the arrays    
    first_temp_list_entry = list_temps[0]   
    print("This is the 0-entry in the list_temps situaton")
    print(first_temp_list_entry)
    print("Velocity matrix")
    print(list_velocities)
    return dir_list, case_list, length_case_list, list_temps, list_velocities


def average_pot_temperature(list_temps, length_case_list, list_velocities, case_list):
    """compute average temperatures of each of the arrays input"""
    #(1) loop through the Temperature probe data and pull the final row of the array. The first entry is the time step associated with the final row
    # Convert the list_velocities to numpy array
    list_velocities_array = np.asarray(list_velocities)
    print("List velocities as array: ")
    print(list_velocities_array)
    
    list_velocities_array_transpose = list_velocities_array.transpose()
    
    # convert case list to array
    case_list_array_empty = np.empty([length_case_list,1], dtype = "U10")
    shape_case_list_array_empty = case_list_array_empty.shape
    print("Shape case list array empty: ")
    print(case_list_array_empty)
    
    l = 0
    while l < length_case_list:
        case_list_array_empty[l] = case_list[l]
        l = l +1
        print("case list array empty")
        print(case_list_array_empty)
        #case_list_array = np.ndarray.transpose(case_list_array_empty)
        case_list_array = case_list_array_empty
        print("Case list array")
        print(case_list_array)
        
    case_list_array_shape = case_list_array.shape
    print("Case list array shape")
    print(case_list_array_shape)
    
    final_temp_row = [] # empty vector to be filled  with the bottom row temperatures iteratively
    final_temp_row_matrix = [] # filling the full matrix with bottom rows iteratively
    final_temp_row_averages = [] # to be filled with the average temperatures of the final rows
    case_size = length_case_list # how many cases are included (-1 due to the 0 counting in python)
    number_properties = 3 # case#, velocity, avg temps to be included in the matrix
    
    final_temp_averages_empty = np.empty([length_case_list, 1], dtype = float)
    # Pulling the bottom row from the individual case    
    x = 0 # setting loop condition
    while x < length_case_list:
        print("list temps before error")
        print(list_temps)
        # Pull the individual temperature array, pull dimensions
        Temp_array = list_temps[x]
        print("Temp array right before the error")
        print(Temp_array)
        [rows, cols] = Temp_array.shape
        final_row = rows - 1 # navigating to the final row of temperature array
        print("Final_row")
        print(final_row)
        final_col_entry = cols # last column of the array
        first_col_entry = 1 # skip the time stamp
        
        # pull the final row of the temperature matrix
        final_temp_row = Temp_array[final_row, first_col_entry:final_col_entry]
        
        # Add to the final_temp_row_matrix
        if x == 0:
            final_temp_row_matrix = final_temp_row
        else:
            final_temp_row_matrix = np.append(final_temp_row_matrix, final_temp_row)
        
        # Compute average
        temp_average = np.average(final_temp_row)
        
        final_temp_averages_empty[x] = temp_average
        final_temp_averages = final_temp_averages_empty
        print("final temp row averages")
        print(final_temp_averages)
        
        # Checking functionality
        if x == 0:
            print("here is the temp_array")
            print(Temp_array)
            print("print final_temp_row")
            print(final_temp_row)
            print("average temperature")
            print(temp_average)
            print("final_temp_row_matrix")
            print(final_temp_row_matrix)
        else:
            print("moving on from 0")
        
        x = x +1
        print("x equals: ")
        print(x)
    # Append the temperature single column matrix with the corresponding velocities
    # Float results
    #float_cols = 2
    #results_float_matrix = np.empty(case_size, float_cols)
    
    # String column (cases)
    #string_cols = 1
    #results_string_matrix = np.empty(case_size, float_cols)
    
    # Data types for array
    dt = np.dtype([('col0', 'U10'), ('col1', float), ('col2', float)]) # first col is cases, then velocities, then temps
   
    
    final_temp_row_averages_array = np.asarray(final_temp_row_averages)
    print("final temp row avg array")
    print(final_temp_row_averages_array)
    final_temp_row_averages_array_transpose = final_temp_row_averages_array.transpose()
    
    new_recarr = np.empty([length_case_list,3], dtype=dt)
    new_recarr['col0'] = case_list_array
    new_recarr['col1'] = list_velocities_array
    new_recarr['col2'] = final_temp_averages
    
    print("new_recarr")
    print(new_recarr)
    
    test_value = new_recarr[2, 2]
    print("value (2,2) :")
    print(test_value)
    
    # This makes sense
    test_value_velocity = test_value[1] # take the center value from the list
    print("Test velocity pulling :")
    print(test_value_velocity)
    
    
    test_first_index = new_recarr[1]
    print("index 1:")
    print(test_first_index)
    
    test_column = new_recarr[:,1]
    print("cases: ")
    print(test_column)    
    return new_recarr

    
#new_recarr = average_pot_temperature(list_temps, length_case_list, list_velocities, case_list)
    
 
#def average_composition_outlets(list_GHG)
"""Take in a list of GHGs from a separate data import for the outlet nodes"""
    
    

def evaluate_optimal(new_recarr, length_case_list):
    """The function evaluates the temperature and emission data, and uses the 
    information to identify where the optimals live within the ranges analayzed
    
    Inputs: 
        new_recarr: numpy array of cases, velocities, and average pot temperatures
    Outputs: 
        T_max: maximum average pot temperature
        case_max: case title associated with maximum average pot temp
        U_optimal: secondary air flow velocity associated with maximum average pot temperature"""
    # Size of the array
    shape_new_recarr = new_recarr.shape
    print("new_recarr shape: ")
    print(shape_new_recarr)
    
    # Pull Temperature column, pull max and index associated with it
    Temp_col = 2 # column with temperature data
    velocity_col = 1 # column with the velocity data
    case_column = 0 # velocity with case strings
    
    # for the length of the case_list, extract the temperatures per each list (like example above
    # 2 create a vector of the temperatures in the same order as cases within for loop. 
    # find maximum in the list, and the index
    # return to the full array and extract the velocity and case # associated with the maximum
    # print and validate
    #THE STUFF BELOW IS ALL WRONG
    y = 0 # loop index to zero
    # empty vectors
    case_vector = np.empty([length_case_list, 1], dtype = "U10")
    velocity_vector = np.empty([length_case_list, 1], dtype = float)
    temperature_vector = np.empty([length_case_list, 1], dtype = float)
    
    final_temp_averages_empty = np.empty([length_case_list, 1], dtype = float)
    while y < length_case_list:
        case = new_recarr[y,1] # looping through (case, velocity, temperature)
        case_entry = str(case[0]) # first column
        velocity_entry = case[1] # second column
        temperature_entry = case[2] #third column

        print("case entry")
        print(case_entry)

        print("velocity entry")
        print(velocity_entry)
    
        print("temp entry")
        print(temperature_entry) 

        print("y")
        print(y)
        
        # Add the entry to respective vectorys
        case_vector[y] = case_entry
        velocity_vector[y] = velocity_entry
        temperature_vector[y] = temperature_entry
        
        
        print("case vector")
        print(case_vector)

        print("velocity vector")
        print(velocity_vector)
    
        print("temp vector")
        print(temperature_vector)   
        
        y = y + 1
    
    # Find the maximum average temperature
    T_max = np.max(temperature_vector)
    #T_max_index = np.where(temperature_vector == T_max)
    T_max_index = np.argmax(temperature_vector)
    print("Maximum Temperature: ")
    print(T_max)
    print("Index with maximum temperature: ")
    print(T_max_index)
    
    # finding cases and velocites associated with maximum temperatures
    case_max = case_vector[T_max_index]
    velocity_max = velocity_vector[T_max_index]
    
    print("Maximum case: ")
    print(case_max)
    print("max velocity entry: ")
    print(velocity_max)

    return case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index
    

#case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index = evaluate_optimal(new_recarr)


def plot_variables(case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index):
    """create a matplot lib of the data extracted"""
    #fig, axs = plt.subplots(1, 3, figsize=(5,5)) # figure with multiple plots
    
    shape_case_vector = case_vector.shape
    print("case vector shape")
    print(shape_case_vector)
    
    shape_temp_vector = temperature_vector.shape
    print("temp vector shape")
    print(shape_temp_vector)
    
    shape_velocity_vector = velocity_vector.shape
    print("vel vector shape")
    print(shape_velocity_vector)
    
    
    """temp_vs_case_plot = plt.scatter(case_vector[:,0], temperature_vector[:,0])
    temp_vs_velocity_plot = plt.scatter(velocity_vector[:,0], temperature_vector[:,0])
    velocity_vs_case_plot =  plt.scatter(case_vector[:,0], velocity_vector[:,0])
    """
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.scatter(case_vector[:,0], temperature_vector[:,0])
    plt.title("Temperature versus Case No.")
    #plt.xlabel("Case No.")
    #plt.ylabel("Average Pot Temperature (Celsius)")
    plt.subplot(2,1,2)
    plt.scatter(velocity_vector[:,0], temperature_vector[:,0])
    plt.title("Temperature versus Secondary Air Velocity")
    #plt.xlabel("Secondary Air Velocity (m/s)")
    #plt.ylabel("Average Pot Temperature (Celsius)")
    """plt.subplot(3,1,3)
    plt.scatter(case_vector[:,0], velocity_vector[:,0])
    plt.title("Secondary Air Velocity versus Case No.")
    #plt.xlabel("Case No.")
    #plt.ylabel("Secondary Air Velocity (m/s)")"""
    plt.show()
    
#plot_variables(case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index)

def define_max_surrounding_velocities(case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index):
    """Use the optimal information from the evaluate optimal function to compute new secondary air flow velocities of 
    the next 5 models"""
    # Algorithm ==>
    # (1) Find maximum average pot temperature from the data set 
    # (2) Extract the velocities neighboring the maximum
    # (3) Compute 3 equally spaced velocities within the range computed
    # (4) return the new velocities as floats
    num_cases_between = 4 # three cases in between max and (each) neighbor
    num_cases_left = num_cases_between - 1
    num_cases_right = num_cases_between - 1
    
    # neighboring cases, temperatures, velocities
    case_left = case_vector[T_max_index - 1]
    case_right = case_vector[T_max_index + 1]
    temp_left = temperature_vector[T_max_index - 1]
    temp_right = temperature_vector[T_max_index + 1]
    velocity_left = velocity_vector[T_max_index - 1]
    velocity_right = velocity_vector[T_max_index + 1]
    
    print("left v")
    print(velocity_left)
    
    print("Right v")
    print(velocity_right)
    
    # Compute neighboring velocities
    # Velocity steps
    delta_V = (velocity_max-velocity_left)/num_cases_between
    print("delta V")
    print(delta_V)
    
    rows_v_inside = (num_cases_between-1)*2
    v_cases_inside = np.empty([rows_v_inside, 1], dtype = float)
    print("shape of inside vector")
    p = 0 # defining loop
    # Left hand side:
    while p < num_cases_left:
        v_cases_inside[p] = velocity_left + (p+1)*delta_V
        print("v cases inside")
        print(v_cases_inside)
        p = p+1
    
    t = 0 # setting for next entry
    
    while t < num_cases_right:
        v_cases_inside[t+num_cases_left] = velocity_right - (t+1)*delta_V
        print("v cases inside")
        print(v_cases_inside)
        t = t+1       
    
    print("v cases inside")
    print(v_cases_inside)
    
    v_cases_inside_shape = v_cases_inside.shape # used later

    return v_cases_inside, delta_V, v_cases_inside_shape
    
#v_cases_inside, delta_V, v_cases_inside_shape = define_max_surrounding_velocities(case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index)    
    
def add_outside_velocities(case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index, delta_V):
    """Add two cases on (each of) the surrounding sides of the velocity field used"""
    # find maximum, and minimum velocity in the case field
    # compute the surrounding velocities using the delta_V from the previous velocity computation
    # return the velocities
    num_cases_right = 4 #controls the velocity loop
    num_cases_left = 1
    sum_cases_outside = num_cases_right + num_cases_left # sum used for looping
    
    # Find Maximum and minimum:
    V_right_max = np.max(velocity_vector)
    V_left_min = np.min(velocity_vector)
    
    """# this would cause a zero or negative flow, so going to stop analysis here
    if V_left_min <= delta_V:
        print("Not computing left hand minimum Velocity (less zero)")
    else:
        # Think about this....
        print("Still thinking about what to do here")"""
    # RHS
    
    # Creating empty vector depending on number cases left
    if num_cases_left == 0:
        v_cases_outside = np.empty([num_cases_right, 1], dtype = float)
    else:
        v_cases_outside = np.empty([sum_cases_outside, 1], dtype = float)
    
    shape_V_cases_outside = v_cases_outside.shape
    print("Shape V cases outside vector")   
    print(shape_V_cases_outside)
    
    
    # Right hand side
    l = 0
    while l < num_cases_right:
        v_cases_outside[l] = V_right_max + (l+1)*delta_V #adding right hand side values in first
        print("l equals")
        print(l)
        l = l+1
        
    if num_cases_left == 0:
        print("No cases to add on the left side")
    else:
        k = 0
        while k < num_cases_left:
            v_cases_outside[k+num_cases_right] = V_left_min - (k+1)*delta_V
            print("k equals")
            print(k)
            k = k+1
    
    print("V cases outside")
    print(v_cases_outside)
    
    v_cases_outside_shape = v_cases_outside.shape
    
    
    return v_cases_outside, sum_cases_outside, num_cases_right, num_cases_left, v_cases_outside_shape

#v_cases_outside, sum_cases_outside, num_cases_right, num_cases_left, v_cases_outside_shape = add_outside_velocities(case_vector, temperature_vector, velocity_vector, T_max, case_max, velocity_max, T_max_index, delta_V)

def create_new_velocity_vector(v_cases_outside, v_cases_inside, v_cases_inside_shape, v_cases_outside_shape):
    """Add new velocities to a vector... to be used for case file creation"""
    # append for now
    
    print("V cases inside shape")
    print(v_cases_inside_shape)
    
    v_cases_inside_rows = v_cases_inside_shape[0]
    print("v inside rows")
    print(v_cases_inside_rows)
    
    print("V cases outside shape")
    print(v_cases_outside_shape)
    
    v_cases_outside_rows = v_cases_outside_shape[0]
    print("v outside rows")
    print(v_cases_outside_rows)
    
    # create vector with correct number of rows
    v_cases_total_rows = v_cases_inside_rows + v_cases_outside_rows
    v_cases_total_vector = np.empty([v_cases_total_rows, 1], dtype = float)
    
    # adding inside values to the total vector
    v_cases_total_vector[0:v_cases_inside_rows] = v_cases_inside
    print("inside values added")
    print(v_cases_total_vector)
    
    # adding outside values
    v_cases_total_vector[v_cases_inside_rows:v_cases_total_rows] = v_cases_outside
    print("outside values added")
    print(v_cases_total_vector)
    
    return v_cases_total_vector
    #Velocity_new_case_vector = np.empty(7,1) # 7 by 1 column
    
#v_cases_total_vector = create_new_velocity_vector(v_cases_outside, v_cases_inside, v_cases_inside_shape, v_cases_outside_shape)    
   
"""
from new_case_setup import *



case_name_list, v_cases_total_vector_string, v_boundary_strings = define_new_case_names(v_cases_total_vector)


full_case_paths = create_case_directories(case_name_list)


zero_file_paths, constant_file_paths, system_file_paths = add_templates(full_case_paths)


edit_details_files(zero_file_paths, constant_file_paths, system_file_paths, v_boundary_strings)

edit_iterative_boundary_conditions(zero_file_paths, constant_file_paths, system_file_paths, v_boundary_strings)

# TESTS
        # data_import should have a test file for comparison
        # export_hdf_files: I am not sure
        # average pot_temperature should have arrays (in HDF5 format) with expected average
        # forcast next flow rate should have 3 tests: minimum flow rate MAX T, maximum flow rate MAX T, interior flow rate MAX T."""


