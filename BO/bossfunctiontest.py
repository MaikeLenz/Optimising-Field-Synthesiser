import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *

def BO(params, Synth, function, init_points, n_iter):      
        params_dict = Synth.create_dict()
        print(params_dict)
        args = []
        for i in params:
            if i in params_dict:
                args.append(params_dict[i])
            else:
                print('Error! Invalid parameter to vary')
       
        def target_func(*args):
            t=np.linspace(-20,50,20000)
            E=[]
       
            # Update dictionary with new parameters
            for i in range(len(params)):
                params_dict[params[i]] = args[i]
               
            # Now pass dictionary into array full of all the parameters
            organised_params = np.zeros((5, Synth.no_of_channels()))
            for key, value in params_dict.items():
                for i in range(1, Synth.no_of_channels()):
                    if str(i) in key:
                        if 'wavel' in key:
                            organised_params[i][0] = value
                        elif 'fwhm' in key:
                            organised_params[i][1] = value
                        elif 'amp' in key:
                            organised_params[i][2] = value
                        elif 'CEP' in key:
                            organised_params[i][3] = value
                        elif 'delay' in key:
                            organised_params[i][4] = value
           
            # Now update synthesiser- parameters should be in the right order now
            for i in range(len(organised_params)):
                Synth.Update(i , *organised_params[i])
                           
            for i in t:
                E_i=Synth.E_field_value(i)
                E.append(E_i)
               
            return function(E)
       
        # Make pbounds dictionary
        pbounds = {}
        for i in params:
            if 'wavel' in i:
                pbounds[i] = (400,2000)
            if 'fwhm' in i:
                pbounds[i] = (5,70)
            if 'amp' in i:
                pbounds[i] = (0,10)
            if 'CEP' in i:
                pbounds[i] = (0, 2*np.pi)
            if 'delay' in i:
                pbounds[i] = (0,50)
               
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

Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=10.0, amp=1.0, CEP=0.0)


pulses=[Field1,Field2, Field3, Field4, Field5]
delays=(10,20,30,40)
Synth=Synthesiser(pulses,delays)

args=['wavel1','delay2']
BO(args, Synth, totalPower, 2,3)