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

def superGauss(x, A, x0, sigma):
    """
    Fit as super Gaussian to the data and extract the parameter sigma to show the width
    """
    return A*np.exp(-2*((x-x0)/sigma)**4)

def threshold(x,y):
    """
    Find points where signal reaches certain level above noise and find the distance between them
    """
    thresh=0.1
    rows = np.where(y > max(y)*thresh)
    if len(rows) > 0:
        min_index = rows[0]
        max_index = min_index
    else:
        min_index = rows[0]
        max_index = rows[-1]
    return x[max_index]-x[min_index]
    