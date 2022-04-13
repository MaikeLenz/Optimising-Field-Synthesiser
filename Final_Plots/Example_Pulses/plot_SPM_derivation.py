import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set2.colors)
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.labelsize'] = 16

def I(t, I0, tau):
    return I0*np.exp(-(t/tau)**2)
def omega(t, omega0, L, n2, I0, tau):
    c = 3e8
    return ((2*omega0*L*n2*I0*t)/(c*(tau**2)))*np.exp(-(t/tau)**2)

t = np.linspace(-100e-15, 100e-15, 1000)
c = 3e8
tau = 30e-15
energy = 1e-3
radius = 175e-6
wavel0 = 800e-9
omega0 = 2*np.pi*c/wavel0
L = 1.05
pressure = 0.66*3
n2 = (9.3e-21*pressure/10000)

power = energy/(np.sqrt(np.pi)*tau) # energy in J, power in J/s
W0 = 0.64*radius # W0 in m, radius in m
I0 = (power/(np.pi*(W0**2))) # I0 in J/s/m^2 

Intensity = I(t, I0, tau)
Frequencies = omega(t, omega0, L, n2, I0, tau)

fig, ax1 = plt.subplots()

ax1.set_xlabel('Time (fs)')
ax1.set_ylabel('Intensity ($W/m^{2}$)')
ax1.plot(t, Intensity, color='black', label='I(t)')
ax2 = ax1.twinx()
ax2.set_ylabel('$\omega(t) - \omega_{0}$ (rad/s)')
ax2.plot(t, Frequencies, '--', color='black', label='$\omega(t) - \omega_{0}$')

ax1.legend(loc='upper left', fontsize=16)
ax2.legend(loc='upper right', fontsize=16)

plt.show()