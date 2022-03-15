import numpy as np

def phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD, t0=0, cep=0, transmission_fraction=1):
    c = 299792458
    tau = τfwhm/(2*np.sqrt(2*np.log(2)))
    dom = 0.44*2*np.pi/τfwhm
    om0 = 2*np.pi*c/λ0
    power = energy/(np.sqrt(np.pi)*tau) # energy in J, power in J/s
    W0 = 0.64*radius # W0 in m, radius in m
    I0 = (power/(np.pi*(W0**2)))*transmission_fraction # I0 in J/s/m^2 

    # Values of n2 from https://link.springer.com/article/10.1007/s00340-013-5354-0
    # Values of n0 assumed to be 1
    if gas == 'Ne':
        n0 = 1
        n2=(9.3e-21*pressure/10000)
    elif gas == 'Ar':
        n0 = 1
        n2=(1.11e-19*pressure/10000)

    q = ( np.log(4)/dom **2 + 0.5 * 1j * GDD )**0.5
    E_GDD = np.log(4)**0.5 * np.exp(-0.25*(t-t0)**2/q**2) * np.exp(1j*om0*(t-t0) + 1j*cep)/(dom*q)

    phase_GDD_wrapped = np.angle(E_GDD)
    phase_GDD = np.unwrap(phase_GDD_wrapped) - om0*t

    # get tau from dom
    phase_SPM = (om0*flength/c)*(n2*I0*np.exp(-(t/tau)**2))

    total_phase = phase_GDD + phase_SPM
    return total_phase, phase_GDD, phase_SPM

def dydx(x, y):
    """ returns derivative with same shape as y, as opposed to np.diff which returns a shorter array """
    assert len(x) == len(y)
    x = np.array(x)
    y = np.array(y)
    dx = x[1] - x[0]
    return np.gradient(y, dx)

def omega_SPM_plus_GDD(t, total_phase):
    omega = dydx(t, total_phase)
    return omega

def width_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD, t0=0, cep=0, transmission_fraction=1):
    total_phase, _, _ = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD, t0, cep, transmission_fraction)
    omega = omega_SPM_plus_GDD(t, total_phase)
    domega = max(omega) - min(omega)
    return domega

"""
import matplotlib.pyplot as plt
t = np.linspace(-50e-15, 50e-15, 1000)
radius = 175e-6
flength = 1.05
pressure = 2
λ0 = 800e-9
τfwhm = 30e-15
energy = 1e-3
gas = 'Ne'
GDD = 400e-30

total_phase_pos, phase_GDD_pos, phase_SPM_pos = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD, t0=0, cep=0, transmission_fraction=1)
total_phase_neg, phase_GDD_neg, phase_SPM_neg = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, -GDD, t0=0, cep=0, transmission_fraction=1)
total_phase_zero, phase_GDD_zero, phase_SPM_zero = phase_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, 0, t0=0, cep=0, transmission_fraction=1)

omega_pos = omega_SPM_plus_GDD(t, total_phase_pos)
omega_neg = omega_SPM_plus_GDD(t, total_phase_neg)
omega_zero = omega_SPM_plus_GDD(t, total_phase_zero)

domega_pos = max(omega_pos) - min(omega_pos)
domega_neg = max(omega_neg) - min(omega_neg)
domega_zero = max(omega_zero) - min(omega_zero)

print('Positive GDD = {}'.format(domega_pos))
print('Negative GDD = {}'.format(domega_neg))
print('Zero GDD = {}'.format(domega_zero))

plt.figure()
plt.plot(t, total_phase_pos, label='Positive GDD')
plt.plot(t, total_phase_neg, label='Negative GDD')
plt.plot(t, total_phase_zero, label='Zero GDD')
plt.legend()
plt.show()

plt.figure()
plt.plot(t, omega_pos, label='Positive GDD')
plt.plot(t, omega_neg, label='Negative GDD')
plt.plot(t, omega_zero, label='Zero GDD')
plt.legend()
plt.show()


GDD_range = np.linspace(-1000e-30, 1000e-30, 10000)
domegas = []
domega_for_zero_GDD = width_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, 0, t0=0, cep=0, transmission_fraction=1)
for i in range(len(GDD_range)):
    domegas.append(width_SPM_plus_GDD(t, radius, flength, pressure, λ0, τfwhm, energy, gas, GDD_range[i], t0=0, cep=0, transmission_fraction=1) - domega_for_zero_GDD)
print(domega_for_zero_GDD)
print(domegas[0])

plt.plot(GDD_range*(10**30), domegas)
plt.xlabel('GDD, fs^2')
plt.ylabel('Width, /s')
plt.show()
"""