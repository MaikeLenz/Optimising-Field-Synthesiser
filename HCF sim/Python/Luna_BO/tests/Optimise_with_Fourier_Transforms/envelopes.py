import numpy as np

def gauss_envelope(t,A,sig,mu):
    """
    simple gaussian envelope
    """
    return A*np.exp(-(t-mu)**2/sig**2)
