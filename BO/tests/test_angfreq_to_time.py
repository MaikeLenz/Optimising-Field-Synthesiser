import sys
#from BO.synthesiser_simulation.angfreq_to_time import f_to_t
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\")

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *

from angfreq_to_time import *
import numpy as np
import matplotlib.pyplot as plt
from mpmath import *

"""
def E_om(om):
    return np.exp(-(om-100)**2/(10)**2)
om=np.linspace(50,150,1000)
E=E_om(om)
t,Et=f_to_t(om,E)
plt.plot(t,Et)
plt.show()
"""
#test with gaussian
def FWHM(X,Y,frac=2):
    d = Y - (max(Y) / frac) 
    indexes = np.where(d > 0)[0] 
    return abs(X[indexes[-1]] - X[indexes[0]])
x=np.linspace(-50,50,10000)
y=np.exp(-(x)**2/1)
#L=len(y)
#x=np.append(x,np.zeros(L))
#y=np.append(y,np.zeros(L))
X,Y=f_to_t(x,y)
Y=np.abs(Y)
width1=FWHM(x,y)
width2=FWHM(X,Y)
print(width1*width2)
x_,y_=t_to_f(X,Y)
plt.plot(x,y)
plt.plot(x_,np.abs(y_))
plt.figure()
plt.plot(X,Y)

#test with sech**2 pulse
x=np.linspace(0,100,10000)
y=[]
for i in x:
    y.append((1/cosh(i))**2)
y=np.array(y)
X,Y=f_to_t(x,y)
Y=np.abs(Y)
width1=FWHM(x,y)
width2=FWHM(X,Y)
print(width1*width2)
x_,y_=t_to_f(X,Y)
plt.figure()
plt.plot(x,y)
plt.plot(x_,np.abs(y_))
plt.figure()
plt.plot(X,Y)


plt.show()


