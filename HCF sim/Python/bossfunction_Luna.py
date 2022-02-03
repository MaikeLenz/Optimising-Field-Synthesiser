import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
from julia import Main

import sys
sys.path.append('D:\\MSci\\GitHub Code\\Optimising-Field-Synthesiser-main\\BO\\')
sys.path.append('D:\\MSci\\GitHub Code\\Optimising-Field-Synthesiser-main\\synth_sim\\')
from subtargetfunctions import *
from field_synth_class import *
from ErrorCorrectionFunction_integrate import *

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length

def BO(params, initial_values, function, init_points=50, n_iter=50, goal_field=None, t=np.linspace(-20,100,20000), window=None):     
    """
    performs BO with params as specified as strings in params input (params is list of strings) on the HCF.
    init_points: number of initial BO points
    n_iter: number of iterations
    plots input&output spectrum
    initial_values = [radius, flength, gas, pressure, λ0, τfwhm, energy] # array of initial values
    """ 
    # Start by assigning values to Luna simulation
    Main.using("Luna")
    
    Main.radius = initial_values[0]
    Main.flength = initial_values[1]
    Main.gas_str = initial_values[2]
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure = initial_values[3]
    Main.λ0 = initial_values[4]
    Main.τfwhm = initial_values[5]
    Main.energy = initial_values[6]

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
                
        # Run the simulation
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')
        Main.eval('t, Et = Processing.getEt(duv)')
        
        # Get values
        t = Main.t
        Et_allz = Main.Et # array of Et at all z 
        Et = Et_allz[:,-1] # last item in each element is pulse shape at the end
        
        # Run minimisation
        if function == errorCorrectionAdvanced_int or function == errorCorrection_int:
            #to minimise rms errors, the sub-target function contains another argument, the goal intensity field
            return function(t, Et**2, goal_field)    
        else: 
            #perhaps already pass the array of intensities in here?
            return function(t, Et) #pass t and E to sub-target function
#%%
    # Make pbounds dictionary
    pbounds = {}
    for i in params:
        #assume standard bounds, same for each channel
        if 'wavel' in i:
            pbounds[i] = (400,2000)
        if 'fwhm' in i:
            pbounds[i] = (5,70)
        if 'amp' in i:
            pbounds[i] = (0.1,3)
        if 'CEP' in i:
            pbounds[i] = (0, 2*np.pi)
        if 'delay' in i:
            pbounds[i] = (0,50)
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
        

    for i in range(len(Synth._pulse_list)):
        #update all the original field objects to the optimised parameters
        Synth._pulse_list[i].Update(Synth,i+1)
        
    plt.figure()
    E_tot = np.array([]) #total electric field
    I=np.array([]) #total intensity
    gradient=np.array([])
    E_individual = np.zeros((Synth.no_of_channels(),len(t))) #list of lists containing the E field values of each channel
    I_individual = np.zeros((Synth.no_of_channels(),len(t))) #list of lists containing the intensity values of each channel

    #creates final arrays for plotting   
    for i in range(len(t)):
        #create list of total electric field value at every t
        E_i= Synth.E_field_value(t[i])
        E_tot=np.append(E_tot,[E_i])
        I=np.append(I,[E_i**2])
        if i==0:
            gradient=np.append(gradient,[0])
        else:
            h=t[1]-t[0]
            gradient=np.append(gradient,[(E_i**2-Synth.E_field_value(t[i-1])**2)/h])
        for j in range(len(Synth._pulse_list)):
            #append individual channel electric fields
            E_individual[j][i]=Synth._pulse_list[j].E_field_value(t[i])
            I_individual[j][i]=(Synth._pulse_list[j].E_field_value(t[i]))**2

    """
    #shift goal field to align with max intensity
    if function==errorCorrectionAdvanced_int or function==errorCorrection_int:
        #shift the left electric field to match in time
        offset=np.argmax(I)-np.argmax(goal_field)

        if offset > 0: #E2 on the left of E1
            goal_field = goal_field[:len(I)-abs(offset)]
            goal_field=np.append(np.zeros(abs(offset)),goal_field)
        elif offset < 0: #E2 on the right of E1
            goal_field = goal_field[abs(offset):]
            goal_field=np.append(goal_field,np.zeros(abs(offset)))
    """
    #plot results
    energies=Synth.Energy_distr(t) #energies in each channel
    f = plt.figure(constrained_layout=True)
    gs = f.add_gridspec(Synth.no_of_channels(), 2)
    f_ax_sim = f.add_subplot(gs[:, 0])
    f_ax_sim.plot(t, E_tot, label="Electric field")
    f_ax_sim.plot(t, I, label="Intensity")
    f_ax_sim.plot(t, gradient, label="Intensity Gradient")
    if function==errorCorrectionAdvanced_int or function==errorCorrection_int:
        #need another curve which is the goal field
        #shift this to align with the max intensity?
        f_ax_sim.plot(t, goal_field, label="Goal Intensity")
    f_ax_sim.set_xlabel('Time, fs')
    f_ax_sim.set_ylabel('Electric field / Intensity')
    plt.legend()

    for i in range(Synth.no_of_channels()):
        #create the subplots for each channel
        f_ax = f.add_subplot(gs[i, 1])
        j=i+1
        f_ax.plot(t, E_individual[i], label="Electric field %s" %j)
        f_ax.plot(t, I_individual[i], label="Intensity %s" %j)
        f_ax.set_title("%s of energy"%(round(energies[i],3)))
        if i == Synth.no_of_channels()-1:
            f_ax.set_xlabel('Time, fs')
        plt.legend()
        if i != (Synth.no_of_channels()-1):
            f_ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    plt.show()

#testing

"""
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
BO(params, Synth, sharpestPeak_triang, 10,10)
"""
