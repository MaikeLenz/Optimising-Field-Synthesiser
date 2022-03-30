import numpy as np
from scipy.fft import *

def t_to_f(t, Et):
    """
    Input of t and Et
    Returns f, Ef
    """
    Ef = fft(Et)
    Ef = fftshift(Ef) # shift to centre of spectrum
    N = len(Et) # Number of points   
    dt=t[1]-t[0]#time intervals
    f = fftfreq(N, dt)
    f = fftshift(f) # shift to centre of spectrum
    return f,Ef

def f_to_t(f, Ef):
    """
    Input of f and Ef
    Returns t, Et
    """
    #prepare Ef such that Ef[0] is zero frequency, first half is positive frequencies and second half is negative frequencies.
    if any(i<0 for i in f) == False:
        #if no negative frequencies, append negative array
        Ef=np.append(Ef, np.zeros(len(Ef)))
    else:
        #else reorder array
        #need to put these values at the end of the Et array s.t. first half is positive and sceond is -ve frequencies
        neg_indices=np.where(f < 0)[0]
        pos_indices=np.where(f>=0)[0]
        Ef_neg=Ef[neg_indices]
        Ef_pos=Ef[pos_indices]
        Ef=np.array(list(Ef_pos)+list(Ef_neg))
    
    Et = ifft(Ef)
    N = len(Ef) # Number of points

    df=np.abs(f[1]-f[0])#smallest frequency difference gives inverse of duration
    T=1/df#overall duration
    t=np.linspace(-T/2,T/2,len(Et))#construct time axis
    #sometimes Et gets chopped up into positive times first then negative, in that case return Et_new
    Et_oneside = list(Et[:N//2])
    Et_otherside=list(Et[N//2:])
    Et_new=np.array(Et_otherside+Et_oneside)
    return t,Et_new
