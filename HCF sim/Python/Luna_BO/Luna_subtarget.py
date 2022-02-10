import julia
#from julia.api import Julia
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\\ML\\OneDrive - Imperial College London\\MSci_Project\\code\\Synth\\Optimising-Field-Synthesiser\\HCF sim\\Python\\building datasets\\')
#Molly's path here
from rms_width import *


julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin\\julia.exe")
#julia.Julia(runtime="C:\\Users\\ML\\AppData\\Local\\Programs\\Julia-1.7.0\\bin")

from julia import Main

def max_bandwidth(t,Et,λ,Iλ):
    return rms_width(λ,Iλ)
