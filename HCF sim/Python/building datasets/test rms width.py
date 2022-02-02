import numpy as np
from scipy import integrate
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\')

from rms_width import *

#construct gaussian spectral intensity distribution
def intens(w,A,u,o):
    return A*np.exp(-((w-u)**2)/o**2)

omega=np.linspace(100,200,1000)
I=intens(omega,1,150,1)

print(rms_width(omega,I))
