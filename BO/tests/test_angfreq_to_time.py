import sys
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\")

from angfreq_to_time import *
import numpy as np
"""
def E_om(om):
    return np.exp(-(om-100)**2/(10)**2)
om=np.linspace(50,150,1000)
E=E_om(om)
E_omega_to_E_time(E,om)
"""
om=np.array([0,50,100])
E_om=np.array([0,1,0])
E_omega_to_E_time(E_om,om)