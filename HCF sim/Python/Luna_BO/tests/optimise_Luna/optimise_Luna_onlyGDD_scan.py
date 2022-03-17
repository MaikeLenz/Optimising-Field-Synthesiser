import numpy as np
from bayes_opt import BayesianOptimization
import matplotlib.pyplot as plt
import julia
import csv
import sys
from numpy.random import *
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\')
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')

sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\')
from bossfunction_Luna_debugging import *
from compressor_grating_to_values import *

#################################################################################################################
#this function carries out BO for hollow core fibre
#params to be varied: 
    # Pulse: input energy, τfwhm, central wavelength
    # Fibre: pressure, fibre core radius, fibre length
displacements=np.linspace(-0.05e-3,0.05e-3,10)
wavel = 800e-9
gas = 'Ne'

FWHM = 22e-15
radius = 175e-6
flength = 1.05
pressure = 0.8*0.66
energy = 1.5e-3
#radius_init = randint(50, 500)*(10**-6)
#flength_init = randint(1, 30)*0.1
#pressure_init = randint(1, 10)
#energy_init= randint(1, 10)*(10**-4)

c = 299792458 # m/s
domega = 2*np.pi*c/FWHM
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 1000)

Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = wavel
Main.τfwhm = FWHM
Main.energy = energy

Main.ω = omega
# This part is optional - run first with just initial points for comparison
#values:  radius, flength, gas, pressure, wavelength, GDD, energy
#initial_values_HCF=[radius, flength, gas, pressure, wavel, energy,FWHM, 0]

widths_rms=[]
widths_thresh=[]

for i in range(len(displacements)):
    GDD, TOD = compressor_grating_values(grating_pair_displacement_mm=displacements[i]*1000)

    E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
    Iω = np.abs(E)**2

    Main.Iω = Iω  
    Main.phase = ϕω

    # Calculations
    # setting pressure to (0,pressure) means a gradient from zero up until given value
    Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')

    #now extract datasets
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    λ = Main.λ
    Iλ = Main.Iλ
    t = Main.t
    omega=Main.ω
    Iomega=Main.Iω
    Iomega=Iomega.reshape((-1,))[0:500]
    omega=omega[0:500]

    Et_allz=Main.Et #array of Et at all z 
    Et=Et_allz[:,-1] #last item in each element is pulse shape at the end
    Et0=Et_allz[:,0] #first item in each element is pulse shape at the start
    #note Et is complex

    #creating indicative bar to show rms width
    widths_rms.append(rms_width(omega,Iomega))
    widths_thresh.append(threshold(omega,Iomega,omega,Iomega))

print(displacements)   
print(widths_rms)
print(widths_thresh)
