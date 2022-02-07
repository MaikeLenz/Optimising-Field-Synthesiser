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
τfwhms = np.linspace(5e-15,60e-15,100) # array of FWHM durations of the pump pulse
energy=0.5e-3

widths = []
for i in range(len(τfwhms)):
    widths.append(theoretical_width(flength, pressure, λ0, τfwhms[i], energy))

plt.scatter(τfwhms/10**(-15),widths, marker="+")
plt.grid()
plt.ylabel("angular frequency width, /s")
plt.xlabel("Pulse duration, fs")
plt.show()
