import numpy as np

def compressor_grating_values(angle_of_incidence, grating_line_density, grating_pair_separation, wavel):
    c = 299792458
    N = 2 # number of passes
    m = -1 # diffraction order
    d = 1/grating_line_density # grating period
    L = grating_pair_separation

    GDD = -((N*(m**2)*(wavel**3)*L)/(2*np.pi*(c**2)*(d**2))) * (1 - (-m*(wavel/d) - np.sin(angle_of_incidence))**2)**(-3/2)
    TOD = -((3*wavel)/(2*np.pi*c))*((1 + (wavel/d)*np.sin(angle_of_incidence) - (np.sin(angle_of_incidence)**2))/(1 - ((wavel/d) - np.sin(angle_of_incidence))**2)) * GDD
    return GDD, TOD