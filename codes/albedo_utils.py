import numpy as np
import os

def load_albedo_data(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Albedo file '{filename}' not found")
    
    with open(filename, 'r') as infile:
        return infile.readlines()

def process_albedo_data(albedo_data):
    albedo_values = []
    earth_fraction = []
    albedo_regions = []
    
    for line in albedo_data[1:]:  # Skip header
        sline = line.split(',')
        albedo_values.append(float(sline[0]))
        earth_fraction.append(float(sline[1]))
        albedo_regions.append(sline[2].strip())
    
    weighted_albedos = [x * y for x, y in zip(albedo_values, earth_fraction)]

    return {
        'albedo_values': np.array(albedo_values),
        'earth_fraction': np.array(earth_fraction),
        'albedo_regions': albedo_regions,
        'weighted_albedos': np.array(weighted_albedos)
    }