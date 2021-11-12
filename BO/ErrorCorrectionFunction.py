
import numpy as np
import matplotlib.pyplot as plt

def errorCorrection(t, E1, E2):
    """
    returns the negative of the rms error between E1 and E2
    without any adjustment in amplitudes or position in time
    """
    diff = []
    if len(E1) != len(E2):
        print('Error- E1 is a different length to E2')
    for i in range(len(E1)):
        diff.append((E1[i] - E2[i])**2)
    h = t[1] - t[0]
    return -1*((0.5*h*((diff[0]+diff[-1]) + 2*np.sum(diff[1:-1])))**0.5)

def errorCorrectionAdvanced(t, E1, E2):
    """
    finds rms error between two functions, first scales them and matches up maxima in time.
    """
    diff = []
    if len(E1) != len(E2):
        print('Error- E1 is a different length to E2')
        
    plt.figure()
    plt.plot(t, E1, label='curve 1')
    plt.plot(t, E2, label='curve 2')
    plt.title('Raw data')
    plt.legend()
        
    # First scale both functions to amplitude of 1
    for i in range(len(E1)):
        #E1[i] = E1[i]/max(E1)
        #E2[i] = E2[i]/max(E2)
        #norm = np.linalg.norm(an_array)
        #normal_array = an_array/norm
        E1=list(np.array(E1)/(np.linalg.norm(np.array(E1)))) #normalise arrays
        E2=list(np.array(E2)/(np.linalg.norm(np.array(E2))))

    plt.figure()
    plt.plot(t, E1, label='curve 1, scaled')
    plt.plot(t, E2, label='curve 2, scaled')
    plt.title('Amplitude Scaled')
    plt.legend()
        
    # Next shift the maximums to the same time values- consider only the first maximum for simplicity
    E1_max_index = [] #lists that will contain the index of the max value
    E2_max_index = []
    for i in range(len(E1)):
        if E1[i] == max(E1):
            E1_max_index.append(i)
        if E2[i] == max(E2):
            E2_max_index.append(i)
    h = t[1] - t[0] #time interval 

    #shift the left electric field to match in time
    offset=E1_max_index[0]-E2_max_index[0]
    if offset > 0: #E2 on the left of E1
        E1 = E1[offset:]
        E2 = E2[:len(E2)-offset]
        t=t[:len(t)-offset]
    elif offset < 0: #E2 on the right of E1
        E2 = E2[offset:]
        E1 = E1[:len(E2)-offset]
        t=t[:len(t)-offset]
    """
    E2_shifted = np.zeros(len(E2))
    for i in range(len(E2)):
        if (i+E1_max_index[0]-E2_max_index[0]) < len(E2):
            E2_shifted[i] = E2[i+E1_max_index[0]-E2_max_index[0]]
    """
    plt.figure()
    plt.plot(t, E1, label='curve 1')
    plt.plot(t, E2, label ='curve 2, shifted in time')
    plt.title('E2 shifted in time')
    plt.legend()
        
    for i in range(len(E1)):
        diff.append((E1[i] - E2[i])**2)
    plt.show()
    print(errorCorrection(t,E1,E2))
    return errorCorrection(t,E1,E2)


def Gauss(x, A, u, o):
    return A*np.exp(-((x-u)**2)/(2*(o**2)))


"""
#%%
# Testing errorCorrection
t = np.arange(0, 50, 0.1)
E1 = Gauss(t, 1, 25, 5)


# Test function against itself
plt.figure()
plt.plot(t, E1, label='original')
plt.legend()
print(errorCorrection(t, E1, E1)) # Should be zero


# Test against function shifted in time (delayed)
E2 = Gauss(t+5, 1, 25, 5)
plt.figure()
plt.plot(t, E1, label='original')
plt.plot(t, E2, label='shifted')
plt.legend()
print(errorCorrection(t, E1, E2))

# Shift more in time- should be a larger error
E2 = Gauss(t+10, 1, 25, 5)
plt.figure()
plt.plot(t, E1, label='original')
plt.plot(t, E2, label='shifted')
plt.legend()
print(errorCorrection(t, E1, E2))

# Change amplitude and width
E2 = Gauss(t, 5, 25, 5)
plt.figure()
plt.plot(t, E1, label='original')
plt.plot(t, E2, label='shifted')
print(errorCorrection(t, E1, E2))
E3 = Gauss(t, 1, 25, 10)
plt.plot(t, E3, label='broader')
plt.legend()
print(errorCorrection(t, E1, E3))
"""
#%%
# Test advanced error correction function
t = np.arange(0, 50, 0.1)
E1 = Gauss(t, 1, 25, 5)
E2 = Gauss(t+5, 5, 25, 5)
errorCorrectionAdvanced(t, E1, E2)

