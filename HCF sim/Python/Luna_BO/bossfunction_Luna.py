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
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from pulse_with_GDD import *
from Luna_subtarget import *
from compressor_grating_to_values import *

filepath = 'C:\\Users\\iammo\\Documents\\'

#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length
c = 299792458 # m/s


def Luna_BO(params, initial_values_HCF, function, Gaussian = False, ImperialLab = False, init_points=50, n_iter=50, t=np.linspace(-20,100,20000), plotting=True, wavel_bounds=None):     
    """
    performs BO with params as specified as strings in params input (params is list of strings) on the HCF.
    init_points: number of initial BO points
    n_iter: number of iterations
    plots input&output spectrum
    initial_values_HCF = [radius, flength, gas, pressure, λ0, τfwhm, energy] # array of initial values for Luna simulation, could change this to input actual Luna simulation
    """ 
    #Load Luna simulation
    Main.using("Luna")

    #assign initial values to simulation
    Main.radius = initial_values_HCF[0] #fibre core radius, m
    Main.flength = initial_values_HCF[1] #fibre length, m
    Main.gas_str = initial_values_HCF[2] #gas in fibre
    Main.eval("gas = Symbol(gas_str)")
    Main.pressure=initial_values_HCF[3]
    Main.λ0 = initial_values_HCF[4] #central wavelength, m
    Main.energy = initial_values_HCF[5] #input energy, J
    Main.τfwhm = initial_values_HCF[6] #FWHM duration of input pulse, s
    grating_pair_displacement = initial_values_HCF[7] #displacement of compressor grating, m

    args_BO = {} #this dictionary will contain only the parameters we want to vary here
    params_dict={} #this dictionary contains all the parameter values associated with the system
    #load in initial values
    params_dict['radius'] = initial_values_HCF[0]
    params_dict['flength'] = initial_values_HCF[1]
    params_dict['gas_str'] = initial_values_HCF[2]
    params_dict['pressure'] = initial_values_HCF[3]
    params_dict['λ0'] = initial_values_HCF[4]
    params_dict['energy'] = initial_values_HCF[5]
    params_dict['FWHM'] = initial_values_HCF[6]
    params_dict['grating_pair_displacement'] = initial_values_HCF[7]

    #now filter out parameters we are varying
    for i in params:
        if i in params_dict:
            args_BO[i] = params_dict[i] #append parameters to be varied to dictionary
    print(args_BO)

    def target_func(**args):
        """
        this is the target function of the optimiser. It is created as a nested function to take only the desired variables as inputs.
        """
        #first update both args_BO and params_dict with variables to be probed next
        for i in range(len(params)):
            params_dict[params[i]] = args[params[i]]
            
        # Update the simulation's variables with new parameters
        #we use args_BO for this to prevent reloading unchanged parameters into Luna since this takes a lot of time.
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
            elif 'grating_pair_displacement' in key:
                grating_pair_displacement = value
        
        # Check if the point to be probed is under the critical power condition to avoid unphysical outputs.
        # Critical power condition
        Main.eval('ω = PhysData.wlfreq(λ0)')
        Main.eval('_, n0, n2  = Tools.getN0n0n2(ω, gas; P=pressure)')
        Main.eval('Pcrit = Tools.Pcr(ω, n0, n2)')
        Pcrit = Main.Pcrit #cant be above this
        Pmin = 0 #cant be below zero
        τfwhm = Main.τfwhm
        tau = τfwhm/(2*np.sqrt(np.log(2)))
        P = Main.energy/(np.sqrt(np.pi)*tau)
        #power condition is 1 if we are in range and 0 if we are out of the physical range
        power_condition = int(Pmin <= P <= Pcrit)

        try:
            if Gaussian == False:
                if ImperialLab == False:
                    #Custom data pulse is defined and passed to prop capillary
                    domega = 2*np.pi*0.44/τfwhm
                    omega = np.linspace(2*np.pi*c/params_dict["λ0"] - 5*domega/2, 2*np.pi*c/params_dict["λ0"] + 5*domega/2, 100)

                    GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=params_dict["grating_pair_displacement"]*1000)

                    E, ϕω = E_field_freq(omega, GD=0.0, wavel=params_dict["λ0"], domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
                    Iω = np.abs(E)**2


                    Main.ω = omega
                    Main.Iω = Iω  
                    Main.phase = ϕω 
                    # Pass data to Luna
                    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
                else:
                    # Get experimental input spectrum, scale energy and apply phase
                    lines=[]
                    columns=[[],[],[],[],[],[],[],[],[],[],[]]
                    with open (filepath+'Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
                        for myline in myfile:
                            lines.append(myline)

                    c = 299792458 # m/s
                    #print(lines[:22])
                    data=lines[22:] #gets rid of all the stuff at the top
                    data=data[int(len(data)/2):]
                    for i in data:
                        cut=i.split("\t") #delimiter is \t
                        for j ,value in enumerate(cut):
                            columns[j].append(float(value))

                    wavel_nm = np.array(columns[0])
                    intens = np.array(columns[3])
                    omega_list=2*np.pi*c/(wavel_nm*10**-9)
                    Main.ω = omega_list[::-1]
                    Main.Iω = intens[::-1]

                    GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=params_dict["grating_pair_displacement"]*1000)
                    phase = []
                    for j in range(len(omega_list)):
                        phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/params_dict["λ0"], CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
                    Main.phase = phase

                    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
                
            else:
                #default gaussian pulse passed to prop capillary
                Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

            Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
            if function == peak_power_window:
                Main.wavel_bounds=wavel_bounds
                #can also have Processing.peakpower
                Main.eval("peak_power=Stats.peakpower(duv['grid'], duv['Eω'], λlims=wavel_bounds; label=nothing)")
                peak_power=Main.peak_power
                return peak_power*power_condition
            # Get values
            
            λ = Main.λ
            Iλ = Main.Iλ    
                
            return function(λ, Iλ)*power_condition #pass t and E to sub-target function
        except:
            return 0
        
    # Make pbounds dictionary
    pbounds = {}
    for i in params:
        #assume standard bounds
        if 'energy' in i:
            #pbounds[i] = (0,1e-3)
            #pbounds[i] = (0.1e-3,2.0e-3)
            pbounds[i] = (0.5e-3, 1.5e-3)
        elif 'τfwhm' in i:
            #pbounds[i] = (20e-15,50e-15)
            pbounds[i] = (4e-15, 30e-15)
        elif 'λ0' in i:
            pbounds[i] = (700e-9,900e-9)
        elif 'pressure' in i:
            #pbounds[i] = (0,3)
            #pbounds[i] = (1,15)
            #pbounds[i] = (1, 10)
            pbounds[i] = (0.5, 3.5)
        elif 'radius' in i:                
            #pbounds[i] = (125e-6,300e-6)
            pbounds[i] = (50e-6, 500e-6)
        elif 'flength' in i:
            #pbounds[i] = (1,2)
            pbounds[i] = (0.1, 6)
        elif 'grating_pair_displacement' in i:
            pbounds[i] = (-0.5e-3, 0.5e-3)
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

    #now load the final BO result parameters into Luna to plot them
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
        elif 'grating_pair_separation' in key:
            grating_pair_displacement = results[key]

    if plotting == True:
        try:
            if Gaussian == False:
                if ImperialLab == False:
                    λ0 = Main.λ0
                    τfwhm = Main.τfwhm
                    domega = 2*np.pi*0.44/τfwhm
                    omega = np.linspace(2*np.pi*c/λ0 - 5*domega/2, 2*np.pi*c/λ0 + 5*domega/2, 100)

                    GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)

                    E, ϕω = E_field_freq(omega, GD=0.0, wavel=λ0, domega=domega, amp=1, CEP=0, GDD=GDD, TOD=TOD)
                    Iω = np.abs(E)**2

                    Main.ω = omega
                    Main.Iω = Iω  
                    Main.phase = ϕω 
                    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
                else:
                    # Get experimental input spectrum, scale energy and apply phase
                    lines=[]
                    columns=[[],[],[],[],[],[],[],[],[],[],[]]
                    with open (filepath+'Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
                        for myline in myfile:
                            lines.append(myline)

                    c = 299792458 # m/s
                    #print(lines[:22])
                    data=lines[22:] #gets rid of all the stuff at the top
                    data=data[int(len(data)/2):]
                    for i in data:
                        cut=i.split("\t") #delimiter is \t
                        for j ,value in enumerate(cut):
                            columns[j].append(float(value))

                    wavel_nm = np.array(columns[0])
                    intens = np.array(columns[3])
                    omega_list=2*np.pi*c/(wavel_nm*10**-9)
                    Main.ω = omega_list[::-1]
                    Main.Iω = intens[::-1]

                    GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=grating_pair_displacement*1000)
                    phase = []
                    for j in range(len(omega_list)):
                        phase.append(get_phi(omega=omega_list[j], omega0=2*np.pi*c/params_dict["λ0"], CEP=0, GD=0, GDD=GDD, TOD=TOD, FoOD=0, FiOD=0))
                    Main.phase = phase

                    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
                    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
                
            else:
                Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

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
        except:
            print('No optimal parameters found below the critical power threshold')

    return optimizer.max, optimizer.res
