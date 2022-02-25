#imports
import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

#now import the code form the other files
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from subtargetfunctions import *
from bossfunction import *
from field_synth_class import *
#from ErrorCorrectionFunction import * #out of date functions
from ErrorCorrectionFunction_integrate import *

"""
test if the bossfunction works to mimic rms error and reproduce a linear ramp
"""
#create fields
Field1=Wavepacket(t0=50.0, wavel=400.0, fwhm=33.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=50.0, wavel=775.0, fwhm=4.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=50.0, wavel=1100.0, fwhm=45.0, amp=1.0, CEP=0.0)
#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses=[Field1,Field2, Field3]
delays=(0,0)
#pass to synthesiser
Synth=Synthesiser(pulses,delays)
t=np.linspace(0,100,10000)

"""
#define goal field
def ramp(x,a):
    return a*x
#note: the time array must have the same spacing for the synthesiser and for the goal field!
#we want 30fs, so this is fraction of the whole t array
t_goal=t[:int((30/100)*10000)]
print(len(t_goal))
I_goal=ramp(t_goal,12/30)
"""
#parameters to be optimised
params=['CEP1','CEP2','CEP3','amp1','amp2','amp3','delay2','delay3','wavel3']
BO(params, Synth, sharpestPeak_triang, 50,50, t=t)