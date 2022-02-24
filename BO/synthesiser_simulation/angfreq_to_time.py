#takes complex e(omega) as input and returns E(t)

#from locale import ERA_T_FMT
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fft import *

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

def FourierTransform(Et,t):
    E=sp.fft.fft(Et)
    omf=sp.fft.fftfreq(len(t))
    """
    #samp=(abs(abs(x[-1])-abs(x[0]))/len(x))/1000 
    tsamp=(abs(abs(t[-1])-abs(t[0]))/len(t))/1000
    om=omf[int(len(omf)/2+1):len(omf)]
    #repx= 2*tsamp/om
    y = abs(E[int(len(omf)/2+1):len(omf)]).tolist()
    """
    plt.plot(omf,E)
    plt.show()

def t_to_f(t, Et):
    """
    Input of t and Et
    Returns f, Ef
    """
    ts = t[1]-t[0] # Sampling interval
    sr = 1/ts # Sampling rate
    Ef = fft(Et)
    N = len(Ef) # Number of points
    n = np.arange(N)
    T = N/sr
    f = n/T

    Ef_oneside = Ef[:N//2]
    f_oneside = f[:N//2]
    return f_oneside, Ef_oneside

def f_to_t(f, Ef):
    """
    Input of f and Ef
    Returns t, Et
    """
    Et = ifft(Ef)
    N = len(Ef) # Number of points
    #t = 1/f
    fs = f[1]-f[0]
    sr = 1/fs
    N = len(Et)
    n = np.arange(N)
    T = N/sr
    t = n/T
    return t, Et

t = np.linspace(0,1,100)
freq = 2
Et = 3*np.sin(2*np.pi*freq*t)
plt.plot(t, Et, label='Before FFT')
plt.legend()

f, Ef = t_to_f(t, Et)
plt.figure()
plt.plot(f, Ef, label='After FFT')
plt.legend()

t2, Et2 = f_to_t(f, Ef)
plt.figure()
plt.plot(t2, Et2, label='After IFFT')
plt.legend()
plt.show()