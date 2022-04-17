import numpy as np

def theoretical_aplha(lam,gas, a):
    """
    returns the theoretical decay coefficient from grazing incidence losses
    formula from https://aip.scitation.org/doi/pdf/10.1063/1.116609
    """
    if gas=="Ar":
        n_gas=1.00028201
    if gas=="Ne":
        n_gas=1.000066102
    nu=1.4585/n_gas
    return 2*((2.405/(2*np.pi))**2*((lam**2)/(2*a**3))*((nu**2+1)/(np.sqrt(nu**2-1))))

print(theoretical_alpha(790e-9,"Ar",175e-6))
print(theoretical_alpha(790e-9,"Ne",175e-6))