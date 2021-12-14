import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *
from bossfunction import *
#from ErrorCorrectionFunction import *
from ErrorCorrectionFunction_integrate import *


#create fields
Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=20.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=15.0, amp=1.0, CEP=0.0)
Field6=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field7=Wavepacket(t0=0.0, wavel=700.0, fwhm=20.0, amp=1.0, CEP=0.0)
Field8=Wavepacket(t0=0.0, wavel=1000.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field9=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field10=Wavepacket(t0=0.0, wavel=1500.0, fwhm=15.0, amp=1.0, CEP=0.0)

#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses=[Field1,Field2, Field3, Field4, Field5,Field6]#,Field7,Field8,Field9,Field10]
delays=(10,10,10,10,10)
#pass to synthesiser
Synth=Synthesiser(pulses,delays)

#parameters to be optimised
params=['amp1', 'amp2','amp4','amp3', 'amp5','amp6','wavel1','wavel2','wavel3','wavel4','wavel5','wavel6',"fwhm1","fwhm2","fwhm3","fwhm4","fwhm5"]#,"CEP1", "CEP2", "CEP3","CEP4","CEP5","CEP6"]
t=np.linspace(-20,100,2000)
#E_goal=Gauss(t, 1, 25, 5)
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

BO(params, Synth, sharpestPeak_triang, n_iter=20,init_points=20, t=t)
