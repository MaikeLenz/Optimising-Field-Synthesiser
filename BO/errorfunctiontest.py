import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *
from bossfunctiontest import *
from ErrorCorrectionFunction import *

#create fields
Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=20.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=15.0, amp=1.0, CEP=0.0)

#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses=[Field1,Field2, Field3, Field4, Field5]
delays=(10,20,30,10)
#pass to synthesiser
Synth=Synthesiser(pulses,delays)

#parameters to be optimised
params=['CEP5','CEP2','CEP3','CEP4']
t=np.linspace(-20,100,20000)
#E_goal=Gauss(t, 1, 25, 5)
E_goal=[]
for i in t:
    if i<0:
        E_goal.append(0)
    elif i>=0 and i<50:
        E_i=i
        E_goal.append(E_i)
    else:
        E_goal.append(0)

"""
plt.figure()
E_tot = [] #total electric field
I=[] #total intensity
E_individual = np.zeros((Synth.no_of_channels(),1)).tolist() #list of lists containing the E field values of each channel
for i in E_individual:
    i.pop() #get rid of the first zero entry for each channel

        
for i in range(len(t)):
    #create list of total electric field value at every t
    E_i= Synth.E_field_value(t[i])
    E_tot.append(E_i)
    I.append(E_i**2)
    for j in range(len(Synth._pulse_list)):
        #append individual channel electric fields
        E_individual[j].append(Synth._pulse_list[j].E_field_value(t[i]))
"""

BO(params, Synth, errorCorrectionAdvanced,goal_field=E_goal,n_iter=1,init_points=1, t=t)
#errorCorrectionAdvanced(t, E_tot, E_goal)
