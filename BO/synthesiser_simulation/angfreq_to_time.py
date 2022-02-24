#takes complex e(omega) as input and returns E(t)

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def E_omega_to_E_time(E_om,om):
    """
    Fourier transforms from ang freq to time domain 
    """
    Fs=2*(om[np.nonzero(E_om)[-1]]) #samplicng frequency
    E_t = sp.fft.ifft(E_om)
    print(E_t)
    t = np.linspace(0,len(E_t)/Fs,len(E_t))
    #t=np.append(t[len(t)/2:],t[:len(t)/2])
    E_t=np.append(E_t[int(len(E_t)/2):],E_t[:int(len(E_t)/2)])
    plt.plot(t,E_t)
    plt.show()
    return E_t,t