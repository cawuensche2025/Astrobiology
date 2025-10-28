import os
import numpy as np
import scipy.constants as sci

def calculate_star_system(star_type, star_temp, star_radius, albedo_values, 
                         earth_fraction, albedo_regions, constants, radius_range=(0.1, 4.2)):

    # print('Star computation for', star_type, albedo_regions)

    # Calculate star luminosity
    L_star = calculate_star_luminosity(star_temp, star_radius)
    
    # Generate radius array
    radius = generate_radius_array(radius_range, constants['UA'])
    
    # Calculate habitable zone boundaries
    D_min, D_max = calculate_habitable_zone(star_temp, star_radius, constants)
    
    # Calculate temperatures and luminosities
    results = {
        'star_type': star_type,
        'L_star': L_star,
        'radius': radius,
        'D_min': D_min,
        'D_max': D_max,
        'T_eff': {},
        'L_rec': {},
        'L_abs': {}
    }
    
    for i, albedo in enumerate(albedo_values):
        # Calculate effective temperature
        T_eff = calculate_effective_temperature(
            L_star, albedo, radius, 
            constants['emissividade_planetas'][1 if star_type == "Sun" else i],
            constants['greenhouse_planetas'][1 if star_type == "Sun" else i]
        )
        
        # Calculate received and absorbed luminosity
        planet_radius = constants['R_Terra'] if star_type == "Sun" else constants['R_planetas'][i]
        L_rec, L_abs = calculate_planet_luminosity(
            star_temp, star_radius, radius, planet_radius, albedo
        )

        # Store results
        label = albedo_regions[i]
        results['T_eff'][label] = T_eff
        results['L_rec'][label] = L_rec
        results['L_abs'][label] = L_abs
    
    return results

def calculate_star_luminosity(T_star, R_star):
    return 4 * np.pi * (R_star**2) * sci.sigma * T_star**4

def calculate_habitable_zone(T_star, R_star, constants):
    D_min = np.sqrt(constants['A_ratio'] * (T_star/constants['T_max'])**4 * R_star**2)
    D_max = np.sqrt(constants['A_ratio'] * (T_star/constants['T_min'])**4 * R_star**2)
    return D_min, D_max

def calculate_effective_temperature(L_star, albedo, radius, emissivity, greenhouse):
    A1 = L_star * (1 - albedo)
    B1 = 16 * np.pi * sci.sigma * emissivity * radius**2
    return greenhouse + (A1 / B1)**0.25

def calculate_planet_luminosity(T_star, R_star, radius, planet_radius, albedo):
    A_planet = np.pi * planet_radius**2
    L_rec = sci.sigma * T_star**4 * (R_star/radius)**2 * A_planet
    L_abs = L_rec * (1 - albedo)
    return L_rec, L_abs

def generate_radius_array(range_limits, UA, num_points=84):
    start, end = range_limits
    step = (end - start) / num_points
    return np.array([(start + n*step)*UA for n in range(num_points)])