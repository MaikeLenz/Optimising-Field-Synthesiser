import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

plt.figure()
ax1 = plt.subplot(3,2,2)
ax2 = plt.subplot(3,2,4)
ax3 = plt.subplot(3,2,6)
ax4 = plt.subplot(1,2,1)
axes = [ax1, ax2, ax3, ax4]

df_iter = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\Optimal_Params_points_probed.csv")
iteration = df_iter.iloc[:,0]
target_width_iter = df_iter.iloc[:,1] # \m
energy = df_iter.iloc[:,2] # J
pressure = df_iter.iloc[:,3] # bar
grating_pos = df_iter.iloc[:,4] # m

ax4.set_ylim(0, 5.5e14)
ax4.plot(iteration, target_width_iter, 'x', label='Points Probed', color='tab:blue')
ax4.set_xlabel('Number of Iterations')
ax4.set_ylabel('RMS Width, \s')
ax1.plot(iteration, energy*(10**3), 'x', color='tab:blue')
ax1.set_ylabel('Energy (mJ)')
ax2.plot(iteration, pressure, 'x', color='tab:blue')
ax2.set_ylabel('Pressure (bar)')
ax3.plot(iteration, grating_pos*(10**3), 'x', color='tab:blue')
ax3.set_ylabel('Grating Position (mm)')
ax3.set_xlabel('Number of Iterations')

df_optimum = pd.read_csv("C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\Ar_optimisation\\Optimal_Params_optimums.csv")
optimum = df_optimum.iloc[:,0]
target_width_opt = df_optimum.iloc[:,1] # \m
energy = df_optimum.iloc[:,2] # J
pressure = df_optimum.iloc[:,3] # bar
grating_pos = df_optimum.iloc[:,4] # m

ax4.plot(iteration[50:], target_width_opt, linewidth=4, label='Optimum', color='tab:red')
ax1.plot(iteration[50:], energy*(10**3), linewidth=4, color='tab:red')
ax2.plot(iteration[50:], pressure, linewidth=4, color='tab:red')
ax3.plot(iteration[50:], grating_pos*(10**3), linewidth=4, color='tab:red')
ax4.legend(fontsize=16)

plt.show()