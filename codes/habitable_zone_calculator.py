import numpy as np
import scipy.constants as sci
import matplotlib.pyplot as plt
import os
from pathlib import Path
from constants import initialize_constants
from albedo_utils import load_albedo_data, process_albedo_data
from star_computation import calculate_star_system
from output_graphs import generate_plots

#--------------------------------------------------------------
def main():
    # Initialize constants and parameters
    constants = initialize_constants()
    startype = ['Sun','F0','M1V']
    
    # Load albedo data
    albedo_data = load_albedo_data('listadealbedos.txt')
    
    # Process albedo data
    processed_albedos = process_albedo_data(albedo_data)

    # Calculate for Sun (G-type star)
    sun_results = calculate_star_system(
#        star_type="Sun",
        star_type=startype[0],
        star_temp=constants['T_sol'],
        star_radius=constants['R_sol'],
        albedo_values=processed_albedos['albedo_values'],
        earth_fraction=processed_albedos['earth_fraction'],
        albedo_regions=processed_albedos['albedo_regions'],
        constants=constants
        )
    print('Calculations for the Sun')
    # Calculate for F0 star
    f0_results = calculate_star_system(
#        star_type="F0",

        star_type=startype[1],
        star_temp=7220,
        star_radius=1.728 * constants['R_sol'],
        albedo_values=constants['albedo_planetas'],
        earth_fraction=None,
        albedo_regions=["Venus", "Earth", "Mars"],
        constants=constants
        )
    print('Calculations for a F0 star')
    
    # Calculate for M1V star
    m1v_results = calculate_star_system(
#        star_type="M1V",        
        star_type=startype[2],
        star_temp=3660,
        star_radius=0.50 * constants['R_sol'],
        albedo_values=constants['albedo_planetas'],
        earth_fraction=None,
        albedo_regions=["Venus", "Earth", "Mars"],
        constants=constants,
        radius_range=(0.05, 0.25)
        )
    print('Calculations for a M1V star') 
    
    # Generate all plots
    generate_plots(sun_results, f0_results, m1v_results, constants, startype)

if __name__ == "__main__":
    main()