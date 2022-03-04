# test new min/max intensity condition
import numpy as np

max_intensity = 1
min_intensity = 0

E = 1e-3 # energy, J
tau = 30e-15 # duration, fs
a = 175e-6 # fibre radius, m

I = E/((np.pi**(3/2))*tau*((0.64*a)**2))

print(I)