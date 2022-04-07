import julia
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import csv
from scipy.signal import detrend
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
#sys.path.append('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\BO\\synthesiser_simulation\\')
from angfreq_to_time import *

filepath="C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\"
#filepath="C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Luna_BO\\tests\\optimise_Luna\\data\\optimise_lab\\"

# Read optimal params
df_0 = pd.read_csv(filepath+"Test_Data2.csv",skipinitialspace=True)
omega_df=df_0.iloc[210:250,0]

Eomega_real_df=df_0.iloc[210:250,1]
Eomega_imag_df=df_0.iloc[210:250,2]
omega=np.array([])
Eomega=np.array([])


for i in range(len(omega_df)):
    omega=np.append(omega,omega_df[210+i])
    Eomega=np.append(Eomega,Eomega_real_df[210+i]+1j*Eomega_imag_df[210+i])

c=3e8
lambda0=800e-9
om0 = 2*np.pi*c/lambda0
om0_idx = np.argmin(np.abs(omega-om0))
 
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.set_xlabel('Angular Frequency')
ax2.set_ylabel('Phase')
ax1.set_ylabel('Intensity')

domega = omega[2] - omega[1]
tau = np.pi/domega
phase_raw = np.angle(Eomega)
phase = np.unwrap(phase_raw - omega*tau)
phase -= phase[np.argmin(np.abs(omega - 2.4e-15))]
phase=phase*(-1)
phase -= phase[om0_idx]

ax2.plot(omega, phase, '--', label='Phase after')
ax1.plot(omega, np.abs(Eomega)**2, label='Intensity after')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.suptitle('Ne, 1.2mJ, 0.66*3bar')

"""
# Save data
header = ['Angular frequency (rad/s)', 'Real Electric Field (a.u.)', 'Imaginary Electric Field (a.u.)']
#with open('C:\\Users\\iammo\\Documents\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Test_Data_grid.csv', 'w', encoding='UTF8', newline='') as f:
with open('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\Test_Data_grid_zoom.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(omega)):
        writer.writerow([omega[i], Eomega[i].real, Eomega[i].imag])
"""
plt.show()
t,Et=f_to_t_irfft(omega/(2*np.pi),Eomega)
plt.plot(t,np.abs(Et)**2)
plt.show()