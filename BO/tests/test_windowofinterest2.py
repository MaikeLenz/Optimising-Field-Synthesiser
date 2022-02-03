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
test if the optimisation can happen only in a limited window of interest, defined in femtoseconds
"""
#SECOND method: do an rms error minimisation with a goal field of limited duration
#here, use a 50fs long ramp, we don't care about anything before or after

#define goal field
def ramp(x,a):
    return a*x
#note: the time array must have the same spacing for the synthesiser and for the goal field!
t=np.linspace(0,100,10000)
#we want 50fs, so this is half of the whole t array
t_goal=t[:5000]
I_goal=ramp(t_goal,2/50)

#create fields
Field6=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field7=Wavepacket(t0=0.0, wavel=700.0, fwhm=20.0, amp=1.0, CEP=0.0)
Field8=Wavepacket(t0=0.0, wavel=1000.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field9=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field10=Wavepacket(t0=0.0, wavel=1500.0, fwhm=15.0, amp=1.0, CEP=0.0)

#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses2=[Field6,Field7, Field8, Field9, Field10]
delays2=(10,20,30,10)
#pass to synthesiser
Synth2=Synthesiser(pulses2,delays2)

#parameters to be optimised
params2=['wavel1','wavel2','wavel3','wavel4','wavel5']

BO(params2, Synth2, errorCorrectionAdvanced_int, 1,1, goal_field=I_goal)
#no errors, looks good




