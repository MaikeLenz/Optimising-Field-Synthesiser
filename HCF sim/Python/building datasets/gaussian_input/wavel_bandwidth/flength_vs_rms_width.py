import julia
import matplotlib.pyplot as plt
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
radius = 125e-6 # HCF core radius
flengths = np.linspace(0.05,20,100) # HCF length
gas = "Ne"
pressure =  2.340607 # gas pressure in bar, corresponds to 66% of final pressure in atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy=0.5e-3

# Assign arguments to Main namespace
Main.radius = radius
Main.pressure = pressure

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")
Main.τfwhm = τfwhm
Main.λ0 = λ0
Main.energy = energy
widths=np.array([])

for i in flengths:
    print(i)
    Main.flength = i
    # Calculations
    # setting pressure to (0,pressure) means a gradient from zero up until given value
    Main.duv = Main.eval('duv = prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, trange=400e-15, λlims=(150e-9, 4e-6))')

    #now extract datasets
    Main.eval("λ, Iλ = Processing.getIω(duv, :λ, flength)")
    #Main.eval('t, Et = Processing.getEt(duv)')

    ## These next lines show how t, Et and zactual could be accessed in the Python namespace for analysis
    # Once defined, the same method as in time_1d can be used to get the y data needed for analysis of the curve (max heigh, FWHM, etc.), which
    # subsequently would be the inputs the the BO 
    #assign python variables
    λ = Main.λ
    Iλ = Main.Iλ
    width=rms_width(λ,Iλ)*10**9 #in nm
    widths=np.append(widths,width)

"""
plt.scatter(pressures,widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel("Pressure, bar")
plt.show()
"""

plt.scatter(flengths,widths, marker="+", label='Luna')

theor_widths = []
for i in range(len(flengths)):
    theor_widths.append(theoretical_width(radius, flengths[i], pressure, λ0, τfwhm, energy))
plt.scatter(flengths,theor_widths, marker="+", label='Theoretical')
plt.ylabel("Bandwidth, nm")
plt.xlabel('Fibre Length, m')
plt.legend()
plt.show()