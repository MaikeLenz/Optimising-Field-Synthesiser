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

Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=20.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=15.0, amp=1.0, CEP=0.0)
Field6=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)

pulses=[Field1,Field2, Field3, Field4, Field5,Field6]
delays=(2,4,6,8,10)

Synth=Synthesiser(pulses,delays)

params=["wavel1","wavel2","wavel3","wavel4","wavel5","wavel6"]
#        "fwhm1", "fwhm2", "fwhm3", "fwhm4", "fwhm5", "fwhm6",
#        "CEP1", "CEP2", "CEP3", "CEP4", "CEP5", "CEP6", 
#        "delay1", "delay2", "delay3", "delay4", "delay5", "delay6"]
t=np.linspace(-20,60,2000)

BO(params, Synth, slopeGradient, n_iter=1,init_points=1, t=t)
"""
delays=(0,0,0,0,0)

Synth=Synthesiser(pulses,delays)

params=["wavel1","wavel2","wavel3","wavel4","wavel5","wavel6",
        "fwhm1", "fwhm2", "fwhm3", "fwhm4", "fwhm5", "fwhm6",
        "CEP1", "CEP2", "CEP3", "CEP4", "CEP5", "CEP6",]
#        "delay1", "delay2", "delay3", "delay4", "delay5", "delay6"]
t=np.linspace(-20,60,2000)

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

BO(params, Synth, errorCorrectionAdvanced_int, n_iter=100,init_points=10, t=t, goal_field=E_goal, window=None)
"""