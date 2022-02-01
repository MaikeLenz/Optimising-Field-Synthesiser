from bayes_opt import BayesianOptimization
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *

def BO(Synth, function, init_points, n_iter, args):
    def target_func(*args):
        #creates target function. use sub-function and arguments that should be varied
        t=np.linspace(-20,50,20000)
        E=[]
        for i in args:
            Synth.Update(1,delay=delay0, wavel=wavel0)
        Synth.Update(2,delay=delay1, wavel=wavel1)
        Synth.Update(3,delay=delay2, wavel= wavel2)
        Synth.Update(4,delay=delay3, wavel= wavel3)
        Synth.Update(5,delay=delay4, wavel= wavel4)

        Synth.Update(i+1,wavel)
        for i in t:
            E_i=Synth.E_field_value(i)
            E.append(E_i)
        return function(E)
        """
    """
    pbounds = {'delay0':(0,50),'delay1': (0,50), 'delay2': (0,50), 'delay3': (0,50), 'delay4': (0,50), 'wavel0': (400,2000), 'wavel1': (400,2000), 'wavel2': (400,2000), 'wavel3': (400,2000), 'wavel4': (400,2000), 'fwhm0' : (5,70), 'fwhm1' : (5,70), 'fwhm2' : (5,70), 'fwhm3' : (5,70),'fwhm4' : (5,70), 'CEP0': (0,2*np.pi), 'CEP1': (0,2*np.pi), 'CEP2': (0,2*np.pi), 'CEP3': (0,2*np.pi), 'CEP4': (0,2*np.pi)}
    
    for i in range(len(args_dict)):
        for j in range(len(args_dict[i])):
            pbounds[str(args[i][j])] = bounds[i][j]
    optimizer = BayesianOptimization(
        f=target_func,
        pbounds=pbounds,
        verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
        random_state=1,
    )

    optimizer.maximize(
        init_points=init_points,
        n_iter=n_iter,
    )

    print(optimizer.max)
    optparams=[]
    for arg in args:
        optparams.append(optimizer.max.get("params").get(str(arg)))

    #t0_opt= optimizer.max.get("params").get("t0")
    for opt in optparams:
        Synth.Update(1,wavel=wavel0_opt)

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


Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=10.0, amp=1.0, CEP=0.0)


pulses=[Field1,Field2, Field3, Field4, Field5]
delays=(10,20,30,40)
Synth=Synthesiser(pulses,delays)

args=["wavel0","delay0"]

BO(Synth, totalPower, 2,3, args)