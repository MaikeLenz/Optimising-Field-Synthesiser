from bayes_opt import BayesianOptimization
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *

Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=600.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=900.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=1300.0, fwhm=10.0, amp=1.0, CEP=np.pi)
Field5=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=np.pi*0.5)


pulses=[Field1,Field2, Field3, Field4, Field5]
delays=(10,20,30,40)
Synth=Synthesiser(pulses,delays)

def f(delay0,delay1,delay2,delay3,delay4,wavel0,wavel1,wavel2,wavel3,wavel4):
    """
    returns total power over a 10fs window
    """
    Synth.Update(1,delay=delay0, wavel=wavel0)
    Synth.Update(2,delay=delay1, wavel=wavel1)
    Synth.Update(3,delay=delay2, wavel= wavel2)
    Synth.Update(4,delay=delay3, wavel= wavel3)
    Synth.Update(5,delay=delay4, wavel= wavel4)
    t=np.linspace(-20,100,800)
    E=[]
    for i in t:
        E_i=Synth.E_field_value(i)
        E.append(E_i)
    return sharpestPeak_triang(E)

pbounds = {'delay0':(0,50),'delay1': (0,50), 'delay2': (0,50), 'delay3': (0,50), 'delay4': (0,50), 'wavel0': (400,2000), 'wavel1': (400,2000), 'wavel2': (400,2000), 'wavel3': (400,2000), 'wavel4': (400,2000)}

optimizer = BayesianOptimization(
    f=f,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

optimizer.maximize(
    init_points=100,
    n_iter=100,
)

print(optimizer.max)
delay0_opt = optimizer.max.get("params").get("delay0")
delay1_opt = optimizer.max.get("params").get("delay1")
delay2_opt = optimizer.max.get("params").get("delay2")
delay3_opt = optimizer.max.get("params").get("delay3")
delay4_opt = optimizer.max.get("params").get("delay4")

wavel0_opt = optimizer.max.get("params").get("wavel0")
wavel1_opt = optimizer.max.get("params").get("wavel1")
wavel2_opt = optimizer.max.get("params").get("wavel2")
wavel3_opt = optimizer.max.get("params").get("wavel3")
wavel4_opt = optimizer.max.get("params").get("wavel4")

#t0_opt= optimizer.max.get("params").get("t0")
Synth.Update(1,delay=delay0_opt, wavel=wavel0_opt)
Synth.Update(2,delay=delay1_opt, wavel=wavel1_opt)
Synth.Update(3,delay=delay2_opt, wavel= wavel2_opt)
Synth.Update(4,delay=delay3_opt, wavel= wavel3_opt)
Synth.Update(5,delay=delay4_opt, wavel= wavel4_opt)

plt.figure()
t=np.linspace(-20.0, 100.0, 800)
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