import julia
import matplotlib.pyplot as plt
import csv
#plt.rcParams['text.usetex'] = True
import sys
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
from theoretical_width import theoretical_width

#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
julia.Julia(runtime="C:\\Users\\iammo\\AppData\\Local\\Programs\\Julia-1.7.1\\bin\\julia.exe")

from julia import Main

Main.using("Luna")

from rms_width import *
# Arguments
radius = np.linspace(50e-6,500e-6,100) # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of final pressure in atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy=0.5e-3

# Assign arguments to Main namespace
Main.flength = flength
Main.pressure = pressure

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.τfwhm = τfwhm
Main.λ0 = λ0
Main.energy = energy
widths=np.array([])

for i in radius:
    print(i)
    Main.radius = i
    # Calculations
    # setting pressure to (0,pressure) means a gradient from zero up until given value
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

    #now extract datasets
    Main.eval("ω, Iω = Processing.getIω(duv, :ω, flength)")
    Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    ω = Main.ω
    Iω = Main.Iω
    width=rms_width(ω,Iω)
    widths=np.append(widths,width)

"""
plt.scatter(radius*10**6,widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel('Core radius, um')
plt.show()
"""

plt.scatter(radius*10**6,widths, marker="+", label='Luna')

theor_widths = []
for i in range(len(radius)):
    theor_widths.append(theoretical_width(radius[i], flength, pressure, λ0, τfwhm, energy))
plt.scatter(radius*10**6,theor_widths, marker="+", label='Theoretical')
plt.ylabel("angular frequency width, /s")
plt.xlabel('Core radius, um')
plt.legend()
plt.show()

# Save the data
header = ['Core radius, um', 'Simulated Angular Frequency Width, /s', 'Theoretical Angular Frequency Width, /s']
with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\angfreq_bandwidth\\data\\radius_vs_rms_width.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    # write the data
    for i in range(len(radius)):
        writer.writerow([radius[i]*10**6, widths[i], theor_widths[i]])