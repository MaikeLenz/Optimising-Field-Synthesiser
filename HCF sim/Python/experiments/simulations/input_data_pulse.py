import matplotlib.pyplot as plt
import numpy as np

#path to txt file
lines=[]
columns=[[],[],[],[],[],[],[],[],[],[],[]]

import sys
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *

with open ('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\data\\HCF_scans\\power in\\Input_Power_Scan.txt', 'rt') as myfile:  # Open lorem.txt for reading
    for myline in myfile:
        lines.append(myline)

c = 299792458 # m/s

data=lines[22:] #gets rid of all the stuff at the top
for i in data:
    split=i.split("\t") #delimiter is \t
    for j ,value in enumerate(split):
        columns[j].append(float(value))

wavel_nm=np.array(columns[0])
intens1_2=np.array(columns[1])
intens1_1=np.array(columns[2])
intens1_0=np.array(columns[3])
intens0_9=np.array(columns[4])
intens0_8=np.array(columns[5])
intens0_7=np.array(columns[6])
intens0_6=np.array(columns[7])
intens0_5=np.array(columns[8])
intens0_4=np.array(columns[9])
intens0_3=np.array(columns[10])
print(type(wavel_nm))
omega=2*np.pi*c/(wavel_nm*10**-9)

plt.plot(omega,intens1_2, label="I(omega), 1200mW")
plt.xlabel("Angular frequency")
plt.ylabel("Intensity")
plt.legend()
plt.figure()
plt.plot(wavel_nm,intens1_2,label="I(lambda), 1200mW")
plt.xlabel("Wavelength, nm")
plt.ylabel("Intensity")
plt.legend()
plt.show()

"""
import julia
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")
from julia import Main
Main.using("Luna")

# Define custom pulse in frequency domain
energy = 1.2e-3 # energy in the pump pulse, 0.5mJ
wavel = moment(wavel_nm,1)
domega = 2e15
omega = np.linspace(2*np.pi*c/wavel - domega/2, 2*np.pi*c/wavel + domega/2, 100)
Iω = 
ϕω=np.zeros(len(intens1_2))
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

#plotting
plt.figure()
plt.plot(λ,Iλ)
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")

plt.figure()
plt.plot(omega,Iomega)
#plt.plot(width_plot,bar_height, label="rms width")
plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.figure()
plt.plot(t,Et,label="z=1m")
plt.plot(t,Et0,label="z=0")
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()
plt.show()
plt.plot(wavel_nm,intens1_2,label="1200mW")
"""
