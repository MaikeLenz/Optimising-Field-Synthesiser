#takes complex e(omega) as input and returns E(t)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def E_omega_to_E_time(E_om,om):
    """
    Fourier transforms from ang freq to time domain 
    """
    #mu=om/(2*np.pi)

    Fs=2*(om.max()/(2*np.pi)) #samplicng frequency
    n=len(E_om)
    E_t = sp.fft.ifft(E_om)
    t = np.linspace(0,len(E_t)/Fs,len(E_t))
    #t=np.append(t[len(t)/2:],t[:len(t)/2])
    E_t=np.append(E_t[int(len(E_t)/2):],E_t[:int(len(E_t)/2)])
    plt.plot(t,np.abs(E_t))
    plt.show()
    return E_t,t