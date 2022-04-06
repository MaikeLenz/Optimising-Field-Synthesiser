import sys

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from width_methods import *
from rms_width import *
import matplotlib.pyplot as plt
import numpy as np
#create x axis
x=np.linspace(-50,50,1000)
#define super gaussian envelope parameters
A=5
x0=0
#create array of widths
sigmas=np.linspace(1,40,80)
rms=np.array([])
thresh=np.array([])
superG=np.array([])
norm_int=np.array([])
for sigma in sigmas:
    #iterate through widths
    #create envelope
    y_env=superGauss(x,A,x0,sigma)
    #now randomise inside
    y=np.array([])
    for i in y_env:
        y=np.append(y,i*np.random.sample(1))
    #plt.plot(x,y,label="width=%s"%(2*sigma))
    rms=np.append(rms,rms_width(x,y))
    thresh=np.append(thresh,threshold(x,y))
    #superG=np.append(superG,superGauss())
    norm_int=np.append(norm_int,norm_and_int(x,y))
#plt.legend()
#plt.show()
from scipy.optimize import curve_fit
def linear(x,a):
    return a*x
poptrms,_rms=curve_fit(linear,2*sigmas,rms)
poptthresh,_thresh=curve_fit(linear,2*sigmas,thresh)
poptnorm_int,_norm_int=curve_fit(linear,2*sigmas,norm_int)
plt.scatter(2*sigmas, rms,label="RMS Width, gradient %s"%(round(poptrms[0],2)),marker="+")
plt.scatter(2*sigmas,thresh,label="Threshold Width, gradient %s"%(round(poptthresh[0],2)),marker="+")
plt.scatter(2*sigmas,norm_int,label="Normalised Integral, gradient %s"%(round(poptnorm_int[0],2)),marker="+")
plt.plot(2*sigmas,linear(2*sigmas,*poptrms))
plt.plot(2*sigmas,linear(2*sigmas,*poptthresh))
plt.plot(2*sigmas,linear(2*sigmas,*poptnorm_int))

plt.ylabel("Measured Width, a.u.",fontsize=14)
plt.xlabel("Super Gaussian Envelope Width",fontsize=14)
plt.legend(fontsize=14)
plt.show()