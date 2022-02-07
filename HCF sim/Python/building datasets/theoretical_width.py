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

    # Right now this is just a rough estimate for n2, need an actual function
    if pressure <= 10*(10**(-3)):
        n2 = 0 * (10**(-19))
    elif pressure > 10*(10**(-3)) and pressure <= 100*(10**(-3)):
        n2 = 0.1 * (10**(-19))
    elif pressure > 100*(10**(-3)) and pressure <= 500*(10**(-3)):
        n2 = 0.8 * (10**(-19))
    elif pressure > 500*(10**(-3)):
        n2 = 1.3 * (10**(-19))
    

    return 2*np.sqrt(2)*np.exp(-0.5)*w0*n2*I0*L/(c*τ)