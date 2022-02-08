"""
Tutorial how to use the simulation with BO
"""

#imports
import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

#now import the code form the other files
import sys
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from subtargetfunctions import *
from field_synth_class import *
from bossfunction import *
#from ErrorCorrectionFunction import * #out of date functions
from ErrorCorrectionFunction_integrate import *


#create channels that make up the synthesiser as wavepacket objects
#for each one, define:
#  the start time t0, which is irrelevant at the moment and can be set to zero, 
#  the central wavelength in nm, 
#  the fwhm in fs, relative amplitude, 
#  and the carrier envelope phase between zero and 2 pi
# example with 6 channels:
Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=20.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=15.0, amp=1.0, CEP=0.0)
Field6=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)

#initialise pulse list and tuple of relative delays (relative to 1st pulse)
pulses=[Field1,Field2, Field3, Field4, Field5,Field6]
delays=(2,4,6,8,10)
#now the 2nd pulse is 2fs after the 1st, the 3rd is 4fs after the 1st, the 4th is 6fs after the 1st, etc.

#create the synthesiser object. 
#need the list of channels and the tuple of relative delays
Synth=Synthesiser(pulses,delays)

#now define parameters to be optimised as strings
#options:
#wavelength: "wavel"+no. of channel
#fwhm: "fwhm"+no. of channel
#amplitude: "amp"+no.of channel
#CEP: "CEP"+no.of channel
#delay: "delay"+no. of channel

#example where ecah of the six wavelengths are to be varied:
params=["wavel1","wavel2","wavel3","wavel4","wavel5","wavel6"]

#create array of times
t=np.linspace(-20,60,2000)

#need more comments here about: available sub-target functions, minimising rms errors
E_goal=np.array([])

#ramp
for i in t:
    if i<0:
        E_goal=np.append(E_goal,[0])
    elif i<30:
        E_i=60-2*i
        E_goal=np.append(E_goal,[E_i])
    else:
        E_goal=np.append(E_goal,[0])


#top hat
for i in t:
    if i<0:
        E_goal=np.append(E_goal,[0])
    elif i>=0 and i<40:
        E_i=1
        E_goal=np.append(E_goal,[E_i])
    else:
        E_goal=np.append(E_goal,[0])



#BO(params, Synth, errorCorrection_int, goal_field=E_goal, n_iter=100,init_points=200, t=t)
#print(errorCorrection_int(t,E_goal,E_goal))

BO(params, Synth, errorCorrectionAdvanced_int, n_iter=10,init_points=10, t=t)