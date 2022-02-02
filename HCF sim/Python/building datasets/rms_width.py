import numpy as np
from scipy import integrate

def moment(omega,I,n): 
    """
    returns an integral of the nth moment of intensity over frequency
    """
    integrand = np.array([]) #array of overlaps of the intensity with itself with a freq shift omega_shift
    for i in range(len(omega)):
        integrand=np.append(integrand,I[i]*omega[i]**n)
    return integrate.simps(integrand,omega) 

def rms_width(omega,I):
    """
    returns the rms width of an intensity distribution over angular frequencies omega
    """
    return ((moment(omega,I,2)/moment(omega,I,0))-(moment(omega,I,1)/moment(omega,I,0))**2)**0.5
