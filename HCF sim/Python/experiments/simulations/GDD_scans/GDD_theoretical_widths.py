import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
from theoretical_width import *
from theoretical_GDD_duration import *

filepath = "C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\"
# Define parameters
df = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\HCF_scans\\power in\\extracted_params.csv")
powers = df.iloc[:,0]
energies = powers/1000
λ0s = df.iloc[:,1]
domegas = df.iloc[:,2]

c = 299792458 # m/s
radius = 175e-6 # HCF core radius
flength = 1.05 # HCF length
pressure = 3*0.66
gas = 'Ne'
λ0 = λ0s[1]
domega = domegas[1]
τfwhm = 0.441/domega # Assuming transform limited
dλ = ((λ0**2)/(2*np.pi*c))*domega
energy = energies[1]

# First find theoretical broadening without GGD
#d_omega = theoretical_width(radius, flength, pressure, λ0, τfwhm, energy)
d_omega = theoretical_width_exp(radius, flength, energy, pressure, gas, dλ, λ0)
d_tp = 0.441/d_omega

# Now find GGD broadening
GDDs = np.linspace(-10000*(10**-30), 10000*(10**-30), 100)
width_time = []
for i in range(len(GDDs)):
    width_time.append(GDD_duration(GDDs[i], d_tp)) # Will give width in time-domain
# Convert widths from time to wavelength domain
width_wavelength = [] # Width in nm
for i in range(len(width_time)):
    width_omega = 0.441/width_time[i]
    width_wavelength.append((((λ0**2)/(2*np.pi*c))*width_omega)*(10**9))

# Plot against simulated widths
df = pd.read_csv(filepath+"simulations\\data\\GDD_Scan_huge_range.csv")
GDDs_sim = df.iloc[:,0]
widths_sim = df.iloc[:,1]

f , axs = plt.subplots(2)
axs[0].plot(GDDs_sim, widths_sim, label='Simulated')
axs[1].plot(GDDs*(10**30), width_wavelength, label='Theoretical')
axs[0].set_xlabel('GDD')
axs[0].set_ylabel('Width, nm')
axs[0].legend()
axs[1].set_xlabel('GDD')
axs[1].set_ylabel('Width, nm')
axs[1].legend()
plt.show()