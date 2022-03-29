import sys
#from BO.synthesiser_simulation.angfreq_to_time import f_to_t
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\")

from angfreq_to_time import *
import numpy as np
import matplotlib.pyplot as plt
"""
def E_om(om):
    return np.exp(-(om-100)**2/(10)**2)
om=np.linspace(50,150,1000)
E=E_om(om)
t,Et=f_to_t(om,E)
plt.plot(t,Et)
plt.show()
"""

x=np.linspace(0,100,1000)
y=np.exp(-(x-50)**2)

X,Y=f_to_t(x,y)
plt.plot(x,y)
plt.figure()
plt.plot(X,Y)
plt.show()


