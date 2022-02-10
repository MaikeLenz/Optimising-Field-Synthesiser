import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
from julia import Main

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from Luna_subtargetfunctions import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

def Luna_BO(params, initial_values_HCF, function, init_points=50, n_iter=50, t=np.linspace(-20,100,20000)):     
    """
    performs BO with params as specified as strings in params input (params is list of strings) on the HCF.
    init_points: number of initial BO points
    n_iter: number of iterations
    plots input&output spectrum
    initial_values_HCF = [radius, flength, gas, pressure, λ0, τfwhm, energy] # array of initial values for Luna simulation, could change this to input actual Luna simulation
    """ 
    # Start by assigning values to Luna simulation
    Main.using("Luna")
    
    Main.radius = initial_values_HCF[0]
    Main.flength = initial_values_HCF[1]
    Main.gas_str = initial_values_HCF[2]
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = initial_values_HCF[3]
    Main.λ0 = initial_values_HCF[4]
    Main.τfwhm = initial_values_HCF[5]
    Main.energy = initial_values_HCF[6]

    args_BO = {} #this dictionary will contain only the parameters we want to vary here
    for i in params:
        args_BO[i] = params[i] #append parameters to be varied to dictionary

    def target_func(**args):
        """
        this is the target function of the optimiser. It is created as a nested function to take only the desired variables as inputs.
        It will consist of one of the sub-target functions in the subtarget function file or one of the rms error functions in ErrorCorrection_integrate.
        """
        for i in range(len(params)):
            args_BO[params[i]] = args[params[i]]
            
        # Update the simulation's variables with new parameters
        for key, value in args_BO.items():
            if 'energy' in key:
                Main.energy = value
            elif 'τfwhm' in key:
                Main.τfwhm = value
            elif 'λ0' in key:
                Main.λ0 = value
            elif 'pressure' in key:
                Main.pressure = value
            elif 'radius' in key:
                Main.radius = value
            elif 'flength' in key:
                Main.flength = value
                
        # Pass data to Luna
        Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

        Main.eval('t, Et = Processing.getEt(duv)')
        Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

        
        # Get values
        t = Main.t
        Et_allz = Main.Et # array of Et at all z 
        Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
        Et0=Et_allz[:,0] #first item in each element is pulse shape at the start

        λ = Main.λ
        Iλ = Main.Iλ    
        
        return function(t, Et, λ, Iλ) #pass t and E to sub-target function
#%%
    # Make pbounds dictionary
    pbounds = {}
    for i in params:
        #assume standard bounds
        if 'energy' in i:
            pbounds[i] = (0,1e-3)
        elif 'τfwhm' in i:
            pbounds[i] = (20e-15,50e-15)
        elif 'λ0' in i:
            pbounds[i] = (700e-9,900e-9)
        elif 'pressure' in i:
            pbounds[i] = (0,3)
        elif 'radius' in i:                
            pbounds[i] = (125e-6,300e-6)
        elif 'flength' in i:
            pbounds[i] = (1,2)
    print(pbounds)

    optimizer = BayesianOptimization(
        #now create BO with the defined target function
        f=target_func,
        pbounds=pbounds,
        verbose=1, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
        random_state=1,
        )

    optimizer.maximize(
        #maximises the target function output. In the case of the rms error functions, this is a minimisation because the errors are multiuplied by -1
        init_points=init_points,
        n_iter=n_iter,
        )

    print(optimizer.max) #final parameters
    
    plt.figure()
    plt.plot(λ*10**9,Iλ)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Spectral energy density (J/m)")


    plt.figure()
    plt.plot(t,Et,label="z=1m")
    plt.plot(t,Et0,label="z=0")
    plt.xlabel("time,s")
    plt.ylabel("Electric field, a.u.")
    plt.legend()
    plt.show()
