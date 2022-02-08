import sys
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\")
import numpy as np
import matplotlib.pyplot as plt

from theoretical_width import theoretical_width

radius = 125e-6 # HCF core radius
flength = 1 # HCF length
gas = "Ne"
pressure = 2.340607 # gas pressure in bar, corresponds to 66% of final pressure in atm
λ0s = np.linspace(500e-9,1000e-9,100) # central wavelength of the pump pulse
τfwhm = 30e-15 # FWHM duration of the pump pulse
energy=0.5e-3

widths = []
for i in range(len(λ0s)):
    widths.append(theoretical_width(flength, pressure, λ0s[i], τfwhm, energy))

width_squared = []
for i in widths:
    width_squared.append(i**2)

#plt.scatter(λ0s*10**9, width_squared, marker="+")
plt.scatter(λ0s*10**9, widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel('Wavelength, nm')
plt.show()
