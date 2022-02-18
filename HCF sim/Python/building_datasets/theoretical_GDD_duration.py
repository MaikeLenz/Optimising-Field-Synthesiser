import numpy as np

def GDD_duration(GDD, tp):
    """
    Returns theoretical duration broadening due to GDD
    tp: transform limited pulse duration
    """
    return tp*np.sqrt(1 + (4*((2*np.log(2))**2)*(GDD**2))/(tp**4))

#print(GDD_duration(1,5))
#print(GDD_duration(100, 5))