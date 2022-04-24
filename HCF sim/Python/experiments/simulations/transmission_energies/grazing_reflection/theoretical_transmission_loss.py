import numpy as np

def theoretical_alpha_um3(lam,gas):
    """
    returns the theoretical decay coefficient from grazing incidence losses in units um^2
    to get the decay coefficient, need to divide this number by the core radius in um cubed
    formula from https://aip.scitation.org/doi/pdf/10.1063/1.116609
    """
    if gas=="Ar":
        n_gas=1.00028201
    if gas=="Ne":
        n_gas=1.000066102
    nu=1.4585/n_gas
    return 2*((2.405/(2*np.pi))**2*((lam**2)/(2))*((nu**2+1)/(np.sqrt(nu**2-1))))*10**18 #in um^2

print(theoretical_alpha_um3(800e-9,"Ar"))
print(theoretical_alpha_um3(800e-9,"Ne"))

print(274852/theoretical_alpha_um3(800e-9,"Ar"))