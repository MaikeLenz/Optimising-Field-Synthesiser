from bayes_opt import BayesianOptimization
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *

Field1=Wavepacket(t0=0.0, freq=633.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, freq=700.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, freq=500.0, fwhm=30.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, freq=640.0, fwhm=15.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, freq=200.0, fwhm=12.0, amp=1.0, CEP=0.0)


pulses=[Field1,Field2, Field3, Field4, Field5]
carrier_freqs=(10,20,30,40)
Synth=Synthesiser(pulses,carrier_freqs)

#f is target function
def f(carrier_freq0,carrier_freq1, carrier_freq2, carrier_freq3, carrier_freq4):
    """
    returns slope gradient
    """
    Synth.Update(1,carrier_freq=carrier_freq0)
    Synth.Update(2,carrier_freq=carrier_freq1)
    Synth.Update(3,carrier_freq=carrier_freq2)
    Synth.Update(4,carrier_freq=carrier_freq3)
    Synth.Update(5,carrier_freq=carrier_freq4)
    t=np.linspace(-20,50,20000)
    E=[]
    for i in t:
        E_i=Synth.E_field_value(i)
        E.append(E_i)
    return slopeGradient(E)

pbounds = {'carrier_freq0':(10,10000),'carrier_freq1': (100,1000), 'carrier_freq2': (100,1000), 'carrier_freq3': (100,1000), 'carrier_freq4': (100,1000)}

optimizer = BayesianOptimization(
    f=f,
    pbounds=pbounds,
    verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    random_state=1,
)

optimizer.maximize(
    init_points=20,
    n_iter=30,
)

print(optimizer.max)
carrier_freq0_opt = optimizer.max.get("params").get("carrier_freq0")
carrier_freq1_opt = optimizer.max.get("params").get("carrier_freq1")
carrier_freq2_opt = optimizer.max.get("params").get("carrier_freq2")
carrier_freq3_opt = optimizer.max.get("params").get("carrier_freq3")
carrier_freq4_opt = optimizer.max.get("params").get("carrier_freq4")

#t0_opt= optimizer.max.get("params").get("t0")
Synth.Update(1,carrier_freq=carrier_freq0_opt)
Synth.Update(2,carrier_freq=carrier_freq1_opt)
Synth.Update(3,carrier_freq=carrier_freq2_opt)
Synth.Update(4,carrier_freq=carrier_freq3_opt)
Synth.Update(5,carrier_freq=carrier_freq4_opt)
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