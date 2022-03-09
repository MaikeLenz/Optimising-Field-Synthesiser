import numpy as np

def compressor_grating_values(angle_of_incidence=30.8, grating_line_density=1280, grating_pair_separation=2.5, wavel=800e-9):
    """
    Calculates GDD and TOD values from the compressor grating position
    angle_of_incidence - degrees
    grating_line_density - l/mm
    grating_pair_separation - cm
    wavel - m

    returns GDD and TOD in s^2 and s^3
    """
    c = 299792458 # speed of light in m/s
    N = 2 # number of passes
    m = -1 # diffraction order
    d = 1/(grating_line_density*1000) # grating period in m
    L = grating_pair_separation/100 # separation in m
    theta = angle_of_incidence*np.pi/180

    GDD = -((N*(m**2)*(wavel**3)*L)/(2*np.pi*(c**2)*(d**2))) * ((1 - ((-m*(wavel/d) - np.sin(theta))**2))**(-3/2))
    TOD = -((3*wavel)/(2*np.pi*c))*((1 + (wavel/d)*np.sin(theta) - (np.sin(theta)**2))/(1 - ((wavel/d) - np.sin(theta))**2)) * GDD
    return GDD, TOD

"""
GDD, TOD = compressor_grating_values(grating_pair_separation=0.005)
print(GDD*(10**30))
print(TOD*(10**45))
"""