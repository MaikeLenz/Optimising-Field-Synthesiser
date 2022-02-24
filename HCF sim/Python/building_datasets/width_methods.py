"""
Different techniques used to measure pulse width
"""
from scipy.integrate import simps
import numpy as np

def norm_and_int(x, y):
    """
    Normalises the pulse so that the maximum is 1, and then integrates
    """
    maximum = max(y)
    norm = []
    for i in y:
        norm.append(i/maximum)
    return simps(norm, x)

def superGauss(x, A, x0, sigma, P):
    """
    Fit as super Gaussian to the data and extract the parameter sigma to show the width
    """
    return A*np.exp(-2*((x-x0)/sigma)**P)