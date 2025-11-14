import matplotlib.pyplot as plt

def generate_plots(sun_results, f0_results, m1v_results, constants, startype):

    plot_temperature_vs_distance(sun_results, startype[0], constants)
    plot_luminosity_vs_distance(sun_results, startype[0], constants)
    
    plot_temperature_vs_distance(f0_results, startype[1], constants)
    plot_luminosity_vs_distance(f0_results, startype[1], constants)
    
    plot_temperature_vs_distance(m1v_results, startype[2], constants)
    plot_luminosity_vs_distance(m1v_results, startype[2], constants)

def plot_temperature_vs_distance(results, star_type, constants):
    fig = plt.figure(figsize=(10,5))
    plt.title(f'{star_type} star - Surface Temperature', fontsize=12)
    plt.xlabel('Distance to star (AU)', fontsize=12)
    plt.ylabel('Surface Temperature (K)', fontsize=12)
    plt.grid(True)
    
    # Plot habitable zone boundaries
    plt.axhline(y=273, color='r', linestyle='--', label='HZ T_min')
    plt.axhline(y=373, color='b', linestyle='--', label='HZ T_max')
    plt.axhspan(273, 373, color='lightgreen', alpha=0.1, lw=0)
    
    if star_type == "Sun":
        plt.axvline(x=results['D_min']/constants['UA'], color='r', linestyle='-.', label='Inner HZ')
        plt.axvline(x=results['D_max']/constants['UA'], color='g', linestyle='-.', label='Outer HZ')
    
    # Plot temperature curves
    for label, T_eff in results['T_eff'].items():
        plt.plot(results['radius']/constants['UA'], T_eff, label=label)
    
    plt.legend()
    plt.savefig(f'T_eff_{star_type}.png')
    plt.close()

def plot_luminosity_vs_distance(results, star_type, constants):
    fig = plt.figure(figsize=(10,5))
    plt.title(f'{star_type} star - Luminosity', fontsize=12)
    plt.xlabel('Distance to star (AU)', fontsize=12)
    plt.ylabel('Luminosity (W/m^2)', fontsize=12)
    plt.yscale('log')
    plt.grid(True)
    

    # Plot habitable zone boundaries
#    if star_type == "Sun":
    plt.axvline(x=results['D_min']/constants['UA'], color='r', linestyle='-.', label='Inner HZ')
    plt.axvline(x=results['D_max']/constants['UA'], color='g', linestyle='-.', label='Outer HZ')
    
    # Plot luminosity curves
    for label in results['L_rec'].keys():
        plt.plot(results['radius']/constants['UA'], results['L_rec'][label], label=f'{label} - rec')
    
    for label in results['L_abs'].keys():
        plt.plot(results['radius']/constants['UA'], results['L_abs'][label], label=f'{label} - abs')


    plt.legend()
    plt.savefig(f'Luminosity_{star_type}.png')
    plt.close()