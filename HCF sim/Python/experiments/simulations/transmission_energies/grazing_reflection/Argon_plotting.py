import sys
from matplotlib.cbook import ls_mapper
import matplotlib.pyplot as plt
from scipy import integrate
import csv
import pandas as pd
import julia
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.transforms as mtransforms


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

<<<<<<< HEAD
#fig = plt.figure()
#plt.suptitle("Argon Low Energy Transmission",fontsize=20)
fig, axs = plt.subplot_mosaic([['a)', 'b)']],constrained_layout=True)
#ax1 = fig.add_subplot(121)
||||||| 1f91667
fig = plt.figure()
<<<<<<< HEAD
plt.suptitle("Argon Low Energy Transmission",fontsize=20)
=======
fig = plt.figure()
#plt.suptitle("Argon Low Energy Transmission",fontsize=20)
>>>>>>> f3f1bc3a8fc39a7244c3ccfe38ae8de2eccb0254
||||||| 1f91667
plt.suptitle("Argon Low Energy Transmission",fontsize=20)
=======
#plt.suptitle("Argon Low Energy Transmission",fontsize=20)
>>>>>>> f3f1bc3a8fc39a7244c3ccfe38ae8de2eccb0254

ax1=axs["a)"]
ax2=axs["b)"]
for i in range(len(sims)):
    popt,_=curve_fit(func,L,sims[i])
    fit_params.append(popt)
<<<<<<< HEAD
<<<<<<< HEAD
    ax1.plot(L, sims[i],label="%s$\mathrm{\mu}$m"%int(radii[i]*10**6))
||||||| 1f91667
    ax1.plot(L, sims[i],label="radius=%s$\mathrm{\mu}$m"%int(radii[i]*10**6))
=======
    ax1.plot(L, sims[i],label="%s$\mathrm{\mu}$m radius"%int(radii[i]*10**6))
>>>>>>> f3f1bc3a8fc39a7244c3ccfe38ae8de2eccb0254
||||||| 1f91667
    ax1.plot(L, sims[i],label="radius=%s$\mathrm{\mu}$m"%int(radii[i]*10**6))
=======
    ax1.plot(L, sims[i],label="%s$\mathrm{\mu}$m radius"%int(radii[i]*10**6))
>>>>>>> f3f1bc3a8fc39a7244c3ccfe38ae8de2eccb0254
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
#ax2 = fig.add_subplot(122)

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

ax2.plot(r_3, decay_coeff,ls="None",marker="+", markersize=10)
ax2.plot(r_3,line(r_3,*popt),label=r"$\mathrm{\alpha}$=%s$\mathrm{\pm}$23$\mathrm{\mu m^{-3}}$"%(int(popt[0])))
<<<<<<< HEAD
<<<<<<< HEAD
ax2.set_ylabel("Decay Coefficient, $\mathrm{m^{-1}}$",fontsize=16)
ax2.set_xlabel("Inverse of Core Radius Cubed, $\mathrm{\mu m^{-3}}$",fontsize=16)
||||||| 1f91667
plt.ylabel("Decay Coefficient, $\mathrm{m^{-1}}$",fontsize=16)
plt.xlabel("Inverse of Fibre Radius Cubed, $\mathrm{\mu m^{-3}}$",fontsize=16)
=======
plt.ylabel("Decay Coefficient ($\mathrm{m^{-1}}$)",fontsize=16)
plt.xlabel("Inverse of Fibre Radius Cubed ($\mathrm{\mu m^{-3}}$)",fontsize=16)
>>>>>>> f3f1bc3a8fc39a7244c3ccfe38ae8de2eccb0254
||||||| 1f91667
plt.ylabel("Decay Coefficient, $\mathrm{m^{-1}}$",fontsize=16)
plt.xlabel("Inverse of Fibre Radius Cubed, $\mathrm{\mu m^{-3}}$",fontsize=16)
=======
plt.ylabel("Decay Coefficient ($\mathrm{m^{-1}}$)",fontsize=16)
plt.xlabel("Inverse of Fibre Radius Cubed ($\mathrm{\mu m^{-3}}$)",fontsize=16)
>>>>>>> f3f1bc3a8fc39a7244c3ccfe38ae8de2eccb0254
#plt.title("Argon Low Energy Transmission Decay Coefficient",fontsize=20)
print(np.sqrt(_[0][0]))
ax1.legend(fontsize=14,loc="lower right")
ax2.legend(fontsize=14,loc="lower right")

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

"""
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='large', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))

"""
plt.show()



