import sys
from matplotlib.cbook import ls_mapper
import matplotlib.pyplot as plt
from scipy import integrate
import csv
import pandas as pd
import julia
import numpy as np
from scipy.optimize import curve_fit

#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.style.use('tableau-colorblind10')
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\')
#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building_datasets\\")
#from rms_width import *

#sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\input_spectra\\")
#sys.path.append("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\input_spectra\\")
#from find_I0 import *


# rebuild sim_transmissions
gas="Ar"
header = ['radius', 'Fibre Length', 'Transmission']
lines=[]
#filepath='C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\plots\\transmission\\grazing_reflection\\low_energy_transmission_' + gas+ '_mediumradii.csv'
filepath = 'C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\experiments\\plots\\transmission\\grazing_reflection\\low_energy_transmission_' + gas+ '_mediumradii.csv'

file=open(filepath)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

for row in csvreader:
        lines.append(row)

#lines=lines[1:]#remove header
radii=[float(lines[0][0])]
#radii=data.iloc[0][0]
L=[]
sims=[[]]
for i in range(len(lines)):
    if float(lines[i][0])!=radii[-1]:
        radii.append(float(lines[i][0]))
        sims.append([float(lines[i][2])])
    else:
        if float(lines[i][0])==radii[0]:
            L.append(float(lines[i][1]))
        sims[-1].append(float(lines[i][2]))


print(radii)
print(L)
print(len(sims[0]))
########################################################################################
#fit exponential decays
def func(x,a,b):
    return a*np.exp(-b*x)
fit_params=[]

fig = plt.figure()
#plt.suptitle("Argon Low Energy Transmission",fontsize=20)

ax1 = fig.add_subplot(121)
for i in range(len(sims)):
    popt,_=curve_fit(func,L,sims[i])
    fit_params.append(popt)
    ax1.plot(L, sims[i],label="%s$\mathrm{\mu}$m radius"%int(radii[i]*10**6))
plt.legend(fontsize=14,loc="lower right")
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax1.set_xlim(0,3)
#ax1.set_title("Argon Low Energy Transmission",fontsize=20)
ax1.set_xlabel("Fibre Length (m)",fontsize=16)
ax1.set_ylabel("Transmission Fraction",fontsize=16)
print(fit_params)
####################################################################################

#fig2=plt.figure()
ax2 = fig.add_subplot(122)
r_3=[]
for i in radii:
    r_3.append(i**(-3)*10**(-18))
decay_coeff=[]
for i in range(len(fit_params)):
    decay_coeff.append(fit_params[i][1])

r_3=np.array(r_3)
decay_coeff=np.array(decay_coeff)
def line(x,a):
    return a*x

popt,_=curve_fit(line,r_3,decay_coeff)

ax2.plot(r_3, decay_coeff,ls="None",marker="+", markersize=20)
ax2.plot(r_3,line(r_3,*popt),label=r"$\mathrm{\alpha}$=%s$\mathrm{\pm}$23$\mathrm{\mu m^{-3}}$"%(int(popt[0])))
plt.ylabel("Decay Coefficient ($\mathrm{m^{-1}}$)",fontsize=16)
plt.xlabel("Inverse of Fibre Radius Cubed ($\mathrm{\mu m^{-3}}$)",fontsize=16)
#plt.title("Argon Low Energy Transmission Decay Coefficient",fontsize=20)
print(np.sqrt(_[0][0]))
plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)




plt.show()



