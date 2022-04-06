import sys

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from width_methods import *
from rms_width import *
import matplotlib.pyplot as plt
import numpy as np
#create x axis
x=np.linspace(0,100,1000)

#define Gaussian shape

def Gauss(x, A, x0, sigma):
    """
    Fit as super Gaussian to the data and extract the parameter sigma to show the width
    """
    return A*np.exp(-2*((x-x0)/sigma)**2)

rms=np.array([])
thresh=np.array([])
norm_int=np.array([])
peak_separation=np.array([])
for i in range(100):
    #create three gaussians at a random x0, with random width
    x0a=np.random.sample(1)*70+20 #between 20 and 80
    x0b=np.random.sample(1)*70+20
    x0c=np.random.sample(1)*70+20

    #create random widths
    sigmaa=np.random.sample(1)*9+1#between 1 and 10
    sigmab=np.random.sample(1)*9+1
    sigmac=np.random.sample(1)*9+1

    #create random amplitudes
    Aa=np.random.sample(1)*2+3 #between 3 and 5
    Ab=np.random.sample(1)*2+3
    Ac=np.random.sample(1)*2+3

    gaussa=Gauss(x,Aa,x0a,sigmaa)
    gaussb=Gauss(x,Ab,x0b,sigmab)
    gaussc=Gauss(x,Ac,x0c,sigmac)
    
    peak_separation=np.append(peak_separation,max([x0a,x0b,x0c])-min([x0a,x0b,x0c]))
    #add gaussian shapes
    y=gaussa+gaussb+gaussc
    for j in range(len(y)):
        y[j]=y[j]*np.random.sample(1)
    if i==0:
        plt.plot(x,y)
    #measurewidths
    rms=np.append(rms,rms_width(x,y))
    thresh=np.append(thresh,threshold(x,y))
    #superG=np.append(superG,superGauss())
    norm_int=np.append(norm_int,norm_and_int(x,y))
#plt.legend()
plt.show()

from scipy.optimize import curve_fit
def linear(x,a,b):
    return a*x+b
poptrms,_rms=curve_fit(linear,peak_separation,rms)
poptthresh,_thresh=curve_fit(linear,peak_separation,thresh)
poptnorm_int,_norm_int=curve_fit(linear,peak_separation,norm_int)
plt.scatter(peak_separation, rms,label="RMS Width, gradient %s"%(round(poptrms[0],2)),marker="+")
plt.scatter(peak_separation,thresh,label="Threshold Width, gradient %s"%(round(poptthresh[0],2)),marker="+")
plt.scatter(peak_separation,norm_int,label="Normalised Integral, gradient %s"%(round(poptnorm_int[0],2)),marker="+")
plt.plot(peak_separation,linear(peak_separation,*poptrms))
plt.plot(peak_separation,linear(peak_separation,*poptthresh))
plt.plot(peak_separation,linear(peak_separation,*poptnorm_int))
plt.ylabel("Measured Width, a.u.",fontsize=14)
plt.xlabel("Peak Separation",fontsize=14)
plt.legend(fontsize=14)
plt.show()