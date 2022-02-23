#returns I0, intensity in W/cm^2 from I(lambda)
import sys
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *
import numpy as np

def find_I0(I,wavels,energy, a):
    """
    finds intensity I0 from intenstity spectrum I as function of wavelength, array wavels.
    Pulse has energy "energy"
    Assumes optimal coupling to HCF such that w0=0.64*a where w0= beam radius at waist, a= fibre radius
    Assume transform limited at fibre start
    """
    return (energy*29979.2458*rms_width(wavels,I))/((np.pi**(3/2))*(0.64*a)**2*np.sqrt(2)*0.44*(moment(wavel_nm,intensities[i],1)/moment(wavel_nm,intensities[i],0))**2)
