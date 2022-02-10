
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\chirp\\')
from pulse_with_GDD import *

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

# Define custom pulse in frequency domain
energy = 0.5e-3 # energy in the pump pulse, 0.5mJ
c = 299792458 # m/s
wavel = 800e-9
domega = 2e15
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)

E, ϕω = E_field_freq(omega, GD=0.0, wavel=wavel, domega=domega, amp=1, CEP=0, GDD=0, TOD=0)
Iω = np.abs(E**2)

Main.energy = energy
Main.ω = omega
Main.Iω = Iω  
Main.phase = ϕω
Main.λ0 = wavel

# Define experimental params
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
Main.radius = radius
Main.flength = flength
Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.pressure = pressure

# Pass data to Luna
Main.eval('pulse = Pulses.DataPulse(ω, Iω, phase; energy, λ0=NaN, mode=:lowest, polarisation=:linear, propagator=nothing)')
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, pulses=pulse, trange=400e-15, λlims=(150e-9, 4e-6))')
