from bayes_opt import BayesianOptimization
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *

Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=10.0, amp=1.0, CEP=0.0)


pulses=[Field1,Field2, Field3, Field4, Field5]
delays=(10,20,30,40)
Synth=Synthesiser(pulses,delays)

#f is target function
def f(wavel0,wavel1, wavel2, wavel3, wavel4):
    """
    returns slope gradient
    """
    Synth.Update(1,wavel=wavel0)
    Synth.Update(2,wavel=wavel1)
    Synth.Update(3,wavel=wavel2)
    Synth.Update(4,wavel=wavel3)
    Synth.Update(5,wavel=wavel4)
    t=np.linspace(-20,50,20000)
    E=[]
    for i in t:
        E_i=Synth.E_field_value(i)
        E.append(E_i)
    return slopeGradient(E)

pbounds = {'wavel0':(400,2000),'wavel1': (400,2000), 'wavel2': (400,2000), 'wavel3': (400,2000), 'wavel4': (400,2000)}

optimizer = BayesianOptimization(
    f=f,
    pbounds=pbounds,
    verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

optimizer.maximize(
    init_points=20,
    n_iter=30,
)

print(optimizer.max)
wavel0_opt = optimizer.max.get("params").get("wavel0")
wavel1_opt = optimizer.max.get("params").get("wavel1")
wavel2_opt = optimizer.max.get("params").get("wavel2")
wavel3_opt = optimizer.max.get("params").get("wavel3")
wavel4_opt = optimizer.max.get("params").get("wavel4")

#t0_opt= optimizer.max.get("params").get("t0")
Synth.Update(1,wavel=wavel0_opt)
Synth.Update(2,wavel=wavel1_opt)
Synth.Update(3,wavel=wavel2_opt)
Synth.Update(4,wavel=wavel3_opt)
Synth.Update(5,wavel=wavel4_opt)
plt.figure()
t=np.linspace(-30.0, 50, 20000)
E_tot = []
I=[]
for i in range(len(t)):
    #create list of total electric field value at every t
    E_i= Synth.E_field_value(t[i])
    #E_i= Field2.E_field_value(t[i])
    E_tot.append(E_i)
    I.append(E_i**2)

plt.plot(t, np.array(E_tot))
plt.plot(t,np.array(I))
plt.xlabel("time, t")
plt.ylabel("Electric field/Intensity , a.u.")
plt.show()