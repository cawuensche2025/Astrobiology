import numpy as np
import scipy.constants as sci

def initialize_constants():
    constants = {
        'R_sol': 695700000,     # m
        'T_sol': 5778,          # K
        'R_Terra': 6371000,     # m
        'UA': 1.495979E11,      # m
        'T_min': 273,           # K (water freezing)
        'T_max': 373,           # K (water boiling)
        'A_ratio': 0.25,        # Absorption/radiation ratio
        'albedo_planetas': [0.77, 0.294, 0.25],
        'greenhouse_planetas': [507, 34, 0.],
        'emissividade_planetas': [0.845, 0.9, 0.95],
        'R_planetas': [6051000, 6371000, 3389500],  # m
        'D_planetas': [0.723*1.495979E11, 1.495979E11, 1.524*1.495979E11]  # m
    }
    return constants