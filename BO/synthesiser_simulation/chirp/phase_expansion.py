import numpy as np
import matplotlib.pyplot as plt

# set up frequency axis
c = 300 # nm/fs
lambda0 = 800 # centre wavelenght, nm
omega0 = 2 * np. pi * c/lambda0 # rad/fs
domega = 2 # for example, rad/fs
omega = np.linspace(omega0-domega/2, omega0+domega/2, 1000) # omega axis rad/fs

# set up field (Gaussian)
E0 = 1 # arb. units
E_transform_limited = E0 * np.exp(-2 * np.log(2) * (omega-omega0)**2/domega**2)

# spectral intensity
plt.plot(omega, np.abs(E_transform_limited)**2)
plt.show()

CEP  = np.pi/2 # for example, rad
GD = 0 # GD relates to absolute arrival times, so not physically important
GDD = 100 # for example, fs**2
TOD = 0 # maybe later, fs**3

def get_phi(omega, omega0, CEP, GDD, TOD):
    return CEP + GD * (omega-omega) + (1/2) * GDD * (omega-omega0)**2 + (1/6) * TOD * (omega-omega0)**3 

phi = get_phi(omega, omega0, CEP, GDD, TOD)

plt.plot(omega, phi)
plt.show()

E_with_phase_included = E_transform_limited * np.exp(phi * 1J) 

# intensity
plt.plot(omega, np.abs(E_with_phase_included)**2)
plt.show()

phase = np.angle(E_with_phase_included)

plt.plot(omega, phase)
plt.show()

phase = np.unwrap(phase)

plt.plot(omega, phase)
plt.show()