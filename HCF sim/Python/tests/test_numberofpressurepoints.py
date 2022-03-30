
import julia
import matplotlib.pyplot as plt
import numpy as np
import random
import csv
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
from rms_width import *
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\test_pressure_gradients\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\tests\\test_pressure_gradients\\')
from compare_pressures import *
julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")


# Arguments
radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy = 0.5e-3 # energy in the pump pulse, 0.5mJ
pressures=[]
positions=[]
for i in range(1000):
      pressures.append(random.uniform(1.5, 3))
      positions.append(i*flength/100)
pressure_list=[positions,pressures]
pressure=tuple(tuple(sub) for sub in pressure_list)
# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

# Calculations
# setting pressure to (0,pressure) means a gradient from zero up until given value
Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

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
width=rms_width(omega,Iomega)
print(width)
centre=moment(omega,Iomega,1)/moment(omega,Iomega,0)
height=moment(Iomega,omega,1)/moment(Iomega,omega,0)
width_plot=np.array([centre-0.5*width,centre+0.5*width])
bar_height=np.array([height,height])

"""
#save I vs omega to csv
file = open("HCF_I_omega.csv", "w",newline="")
writer = csv.writer(file)
header=[ "angular frequency","Intensity"]
writer.writerow(header)
for w in range(len(Iomega)):
  writer.writerow([omega[w], Iomega[w][0]])

file.close()
"""
#plotting
plt.figure()
plt.plot(λ,Iλ)
plt.xlabel("Wavelength (m)")
plt.ylabel("Spectral energy density (J/m)")

plt.figure()
plt.plot(omega,Iomega)
plt.plot(width_plot,bar_height, label="rms width")
plt.legend()
plt.xlabel("Angular frequency,/s")
plt.ylabel("Intensity, a.u.")

plt.figure()
plt.plot(t,Et,label="z=1m")
plt.plot(t,Et0,label="z=0")
plt.xlabel("time,s")
plt.ylabel("Electric field, a.u.")
plt.legend()
plt.figure()
Z,P=P_distribution(pressure[0],pressure[1])
plt.scatter(Z,P)
plt.show()