import sys
from matplotlib.cbook import ls_mapper
import matplotlib.pyplot as plt
from scipy import integrate
import csv
import julia
import numpy as np
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from rms_width import *

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\input_spectra\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\input_spectra\\")
from find_I0 import *

julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

##################################################################################
#simulate output spectra

radii=np.linspace(30e-6,40e-6,50e-6,60e-6,70e-6)
L=np.linspace(0.1,3,30)

sim_transmission=np.ones((len(radii),len(L)))

for i in range(len(radii)):
    for j in range(len(L)):
        radius=radii[i]
        flength = L[j] # HCF length
        print(radius,flength)
        gas = "Ar"
        pressure = 0.1 # gas pressure in bar
        λ0 = 800e-9 # central wavelength of the pump pulse
        τfwhm = 30e-15 # FWHM duration of the pump pulse
        energy = 1e-5 # energy in the pump pulse

        # Assign arguments to Main namespace
        Main.radius = radius
        Main.flength = flength

        Main.gas_str = gas
        Main.eval("gas = Symbol(gas_str)")

        Main.pressure = pressure
        Main.λ0 = λ0
        Main.τfwhm = τfwhm
        Main.energy = energy

        #Pass data to Luna
        Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

        #########################################################################################
        #find simulated output 
        Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
        Main.eval("λ2, Iλ2 = Processing.getIω(duv, :λ, 0)")

        #energy(grid, Eω; bandpass=nothing)
        #Main.eval("ω, Eω = Processing.getEω(pulse)")
        #Main.eval('energy=energy(duv,duv["Eω"])')
        #Main.eval("transm=transmission(radius, λ0, flength; kind=:HE, n=1, m=1)")
        λ = Main.λ
        Iλ = Main.Iλ
        λ2 = Main.λ2
        Iλ2 = Main.Iλ2
        
        #energy_i=Main.energy
        #energy_i=energies_in[i]*Main.transm
        sim_transmission[i][j]=integrate.simps(Iλ[:,0],λ)/integrate.simps(Iλ2[:,0],λ2)


fig = plt.figure()
ax1 = fig.add_subplot(111)

#a = np.cos(2*np.pi*np.linspace(0, 1, 60.))
for i in range(len(sim_transmission)):
    ax1.plot(L, sim_transmission[i],label="radius=%s$\mathrm{\mu}$m"%int(radii[i]*10**6))
plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax1.set_xlim(0.2,1.3)
ax1.set_title("Argon Low Energy Transmission",fontsize=20)
ax1.set_xlabel("Fibre Length, m",fontsize=16)
ax1.set_ylabel("Transmission",fontsize=16)

# Save the data
header = ['radius', 'Fibre Length', 'Transmission']
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\plots\\transmission\\grazing_reflection\\low_energy_transmission_' + gas+ '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(radii)):
        for j in range(len(L)):
            writer.writerow([radii[i],L[j],sim_transmission[i][j]])

plt.show()


