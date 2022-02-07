import sys
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
import numpy as np
import matplotlib.pyplot as plt

from theoretical_width import theoretical_width

radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of 3.5 atm
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energies = np.linspace(0.1e-3,4.1e-3,100) # array of energies in the pump pulse

widths = []
for i in range(len(energies)):
    widths.append(theoretical_width(flength, pressure, λ0, τfwhm, energies[i]))

plt.scatter(energies*10**(3),widths,marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel("Pulse energy, mJ")
plt.show()
