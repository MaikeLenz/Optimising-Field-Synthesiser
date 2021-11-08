import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\synth_sim\\')
from TargetFunction import *
from field_synth_class3 import *

def BO(params, Synth, function, init_points, n_iter):     
    """
    performs BO with params as specified as strings in params input (params is list of strings) on the synthesiser Synth.
    init_points: number of initial BO points
    n_iter: number of iterations
    plots output total and individual fields.
    """ 
    params_dict = Synth.create_dict() #returns synthesiser parameters as dictionary
    args_BO = {} #this dictionary will contain only the parameters we want to vary here
    for i in params:
        if i in params_dict:
            args_BO[i]=params_dict[i] #append parameters to be varied to dictionary
        else:
            print('Error! Invalid parameter to vary') #this means that the string entered in params is not one of the recognised options
        
    t=np.linspace(-20,100,20000) #time frame to look at, in fs

    def target_func(**args):
        """
        this is the target function of the optimiser. It is created as a nested function to take only the desired variables as inputs.
        """
        E=[]
        # Update the synthesiser's dictionary with new parameters
        for i in range(len(params)):
            params_dict[params[i]] = args[params[i]]
               
        # Now pass dictionary into array full of all the parameters
        #need the parameters in the right order to update the synthesiser
        organised_params = np.zeros((Synth.no_of_channels(),5))
        #print(organised_params)
        for key, value in params_dict.items():
            for i in range(Synth.no_of_channels()+1):
                if str(i) in key:
                    #iterate through parameters and insert into organised params array
                    if 'wavel' in key:
                        organised_params[i-1][0] = value
                    elif 'fwhm' in key:
                        organised_params[i-1][1] = value
                    elif 'amp' in key:
                        organised_params[i-1][2] = value
                    elif 'CEP' in key:
                        organised_params[i-1][3] = value
                    elif 'delay' in key:
                        organised_params[i-1][4] = value

        # Now update synthesiser- parameters should be in the right order now
        for i in range(len(organised_params)+1):
            Synth.Update(i , *organised_params[i-1])
        for i in t: 
            #create the list of total E field vaues over range t
            E_i=Synth.E_field_value(i)
            E.append(E_i)       
        return function(t,E) #pass t and E to sub target function

    # Make pbounds dictionary
    pbounds = {}
    for i in params:
        #assume standard bounds, same for each channel
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
    print(pbounds)

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
        

    for i in range(len(Synth._pulse_list)):
        #update all the original field objects to the optimised parameters
        Synth._pulse_list[i].Update(Synth,i+1)
        
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
        

    plt.plot(t, np.array(E_tot), label="Electric field")
    for i in range(len(Synth._pulse_list)):
        j=i+1
        plt.plot(t, np.array(E_individual[i]), label="Electric field %s" %j)

    plt.plot(t,np.array(I), label="Intensity")
    plt.legend()
    plt.xlabel("time, t")
    plt.ylabel("Electric field/Intensity , a.u.")


    for i in range(len(Synth._pulse_list)):
        #printing channels in individual plots
        plt.figure()
        j=i+1
        plt.plot(t, np.array(E_individual[i]), label="Electric field %s" %j)
        plt.legend()
    
    plt.show()


#create fields
Field1=Wavepacket(t0=0.0, wavel=400.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field2=Wavepacket(t0=0.0, wavel=700.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field3=Wavepacket(t0=0.0, wavel=1000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field4=Wavepacket(t0=0.0, wavel=2000.0, fwhm=10.0, amp=1.0, CEP=0.0)
Field5=Wavepacket(t0=0.0, wavel=1500.0, fwhm=10.0, amp=1.0, CEP=0.0)

#initialise pulse list and tuple of relative delays (from 1st pulse)
pulses=[Field1,Field2, Field3, Field4, Field5]
delays=(10,10,10,10)
#pass to synthesiser
Synth=Synthesiser(pulses,delays)

#parameters to be optimised
params=['wavel1','wavel2', 'delay2','delay5']
BO(params, Synth, sharpestPeak_triang, 10,10)
