# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:59:06 2019

@author: ADAPTED FROM nxsofsys from github link: https://github.com/dicehub/PyFoam/blob/dev/examples/TestRunner/runIcoFoamCavity.py
"""
import os
import time

def run_cases_individual(case_full_paths, k_tot):
    """Run cases one after another
    Args:
    case_full_paths (dict): list of full strings of case folders for future use
    k_tot (int): number of cases total written initially

    Returns
    status (array): array of the status of each case (running, complete, not started)
    """
    # Creates a list containing 5 lists, each of 8 items, all set to 0

    u = 0 # initialize running loop
    while u < k_tot: # outer loop
        active_case_dir = case_full_paths[u]
        os.chdir(active_case_dir)
        os.system("python" + " " "pyFoamRunner.py" + " " + "reactingFoam")
        time.sleep(10)
        u = u + 1
