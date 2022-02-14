#imports
import julia
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\")
from GDD_range import *

max_duration=100e-15#100fs
starting_value=4 #guess is GDD of 10
t=np.linspace(0,100,1000)
t0=50
wavel=800e-9
domega=2e15
CEP=0
print(GDD_range(max_duration, starting_value,t,t0,wavel,domega, CEP))
#returns width function error:invalid value encountered in double_scalars