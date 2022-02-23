#takes complex e(omega) as input and returns E(t)

import numpy as np
import matplotlib.pyplot as plt

def E_omega_to_E_time(E_om,om):
    """
    Fourier transforms from ang freq to time domain 
    """
    #mu=om/(2*np.pi)
    Fs=2*(om.max()/(2*np.pi)) #samplicng frequency
    n=1000
    t = np.arange(0, n/Fs, 1/Fs)
    E_t = np.fft.ifft(E_om)
    plt.plot(t,np.abs(E_t))
    plt.show()
    return E_t,t