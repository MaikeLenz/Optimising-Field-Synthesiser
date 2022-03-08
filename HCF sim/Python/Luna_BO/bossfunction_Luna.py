import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main

import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from pulse_with_GDD import *
from Luna_subtarget import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length
c = 299792458 # m/s


def Luna_BO(params, initial_values_HCF, function, Gaussian = False, FWHM=None,  domega = 2e15, init_points=50, n_iter=50, t=np.linspace(-20,100,20000)):     
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
    GDD=initial_values_HCF[5]
    Main.energy = initial_values_HCF[6]
    if FWHM != None:
        Main.τfwhm = FWHM

    args_BO = {} #this dictionary will contain only the parameters we want to vary here
    params_dict={}
    params_dict['radius'] = initial_values_HCF[0]
    params_dict['flength'] = initial_values_HCF[1]
    params_dict['gas_str'] = initial_values_HCF[2]
    params_dict['pressure'] = initial_values_HCF[3]
    params_dict['λ0'] = initial_values_HCF[4]
    params_dict['GDD'] = initial_values_HCF[5]
    params_dict['energy'] = initial_values_HCF[6]
    if Gaussian==True:
        params_dict['FWHM'] = FWHM

    for i in params:
        if i in params_dict:
            args_BO[i] = params_dict[i] #append parameters to be varied to dictionary
    print(args_BO)

    def target_func(**args):
        """
        this is the target function of the optimiser. It is created as a nested function to take only the desired variables as inputs.
        It will consist of one of the sub-target functions in the subtarget function file or one of the rms error functions in ErrorCorrection_integrate.
        """
        for i in range(len(params)):
            params_dict[params[i]] = params_dict[params[i]]
            
        # Update the simulation's variables with new parameters
        for key, value in args_BO.items():
            if 'energy' in key:
                Main.energy = value
            elif 'λ0' in key:
                Main.λ0 = value
            elif 'pressure' in key:
                Main.pressure = value
            elif 'radius' in key:
                Main.radius = value
            elif 'flength' in key:
                Main.flength = value
            elif 'FWHM' in key:
                Main.τfwhm = value

        # Below critical power condition
        Main.eval('ω = PhysData.wlfreq(λ0)')
        Main.eval('_, n0, n2  = Tools.getN0n0n2(ω, gas; P=pressure)')
        Main.eval('Pcrit = Tools.Pcr(ω, n0, n2)')
        Pcrit = Main.Pcrit
        Pmin = 0
        tau = Main.τfwhm/(2*np.sqrt(np.log(2)))
        P = Main.energy/(np.sqrt(np.pi)*tau)
        power_condition = int(Pmin <= P <= Pcrit)

        if Gaussian == False:
            """
            Custom data pulse is defined and passed to prop capillary
            """
            omega = np.linspace(2*np.pi*c/params_dict["λ0"] - domega/2, 2*np.pi*c/params_dict["λ0"] + domega/2, 100)

            E, ϕω = E_field_freq(omega, GD=0.0, wavel=params_dict["λ0"], domega=domega, amp=1, CEP=0, GDD=GDD, TOD=0)
            Iω = np.abs(E**2)

            Main.ω = omega
            Main.Iω = Iω  
            Main.phase = ϕω 
            # Pass data to Luna
            Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
            Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

        else:
            """
            default gaussian pulse passed to prop capillary
            """
            Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

        Main.eval('t, Et = Processing.getEt(duv)')
        Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")

        
        # Get values
        t = Main.t
        Et_allz = Main.Et # array of Et at all z 
        Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
        Et0=Et_allz[:,0] #first item in each element is pulse shape at the start

        λ = Main.λ
        Iλ = Main.Iλ    
        
        return function(t, Et, λ, Iλ)*power_condition #pass t and E to sub-target function
#%%
    # Make pbounds dictionary
    pbounds = {}
    for i in params:
        #assume standard bounds
        if 'energy' in i:
            #pbounds[i] = (0,1e-3)
            #pbounds[i] = (0.1e-3,2.0e-3)
            pbounds[i] = (0.1e-3, 2e-3)
        elif 'τfwhm' in i:
            #pbounds[i] = (20e-15,50e-15)
            pbounds[i] = (4e-15, 30e-15)
        elif 'λ0' in i:
            pbounds[i] = (700e-9,900e-9)
        elif 'pressure' in i:
            #pbounds[i] = (0,3)
            #pbounds[i] = (1,15)
            pbounds[i] = (1, 15)
        elif 'radius' in i:                
            #pbounds[i] = (125e-6,300e-6)
            pbounds[i] = (50e-6, 500e-6)
        elif 'flength' in i:
            #pbounds[i] = (1,2)
            pbounds[i] = (0.1, 6)
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
    results=optimizer.max["params"]
    for key, value in args_BO.items():
        if 'energy' in key:
            Main.energy = results[key]
        elif 'λ0' in key:
            Main.λ0 = results[key]
        elif 'pressure' in key:
            Main.pressure = results[key]
        elif 'radius' in key:
            Main.radius = results[key]
        elif 'flength' in key:
            Main.flength = results[key]
        elif 'FWHM' in key:
            Main.τfwhm = results[key]

    Main.eval('t, Et = Processing.getEt(duv)')
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    λ = Main.λ
    Iλ = Main.Iλ
    t = Main.t
    Et_allz=Main.Et #array of Et at all z 
    Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
    Et0=Et_allz[:,0]
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

    return optimizer.max
