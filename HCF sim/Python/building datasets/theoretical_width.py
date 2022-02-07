import numpy as np

def theoretical_width(flength, pressure, λ0, τfwhm, energy):
    """
    Returns theoretical calculation for SPM frequency width that comes from Luna simulation.
    Assumes Ne gas for now
    """
    c = 3*(10**8)
    L = flength
    I0 = energy**2
    w0 = 2*np.pi*c/λ0
    τ = τfwhm/np.log(2)
    

    return 2*np.sqrt(2)*np.exp(-0.5)*w0*n2*I0*L/(c*τ)