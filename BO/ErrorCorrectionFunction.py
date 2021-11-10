
import numpy as np
import matplotlib.pyplot as plt

def errorCorrection(t, E1, E2):
    diff = []
    if len(E1) != len(E2):
        print('Error- E1 is a different length to E2')
    for i in range(len(E1)):
        diff.append((E1[i] - E2[i])**2)
    h = t[1] - t[0]
    return (0.5*h*((diff[0]+diff[-1]) + 2*np.sum(diff[1:-1])))**0.5

def errorCorrectionAdvanced(t, E1, E2):
    diff = []
    if len(E1) != len(E2):
        print('Error- E1 is a different length to E2')
        
    plt.figure()
    plt.plot(t, E1)
    plt.plot(t, E2)
    plt.title('Raw data')
        
    # First scale both functions to amplitude of 1
    for i in range(len(E1)):
        E1[i] = E1[i]/max(E1)
        E2[i] = E2[i]/max(E2)
    plt.figure()
    plt.plot(t, E1)
    plt.plot(t, E2)
    plt.title('Amplitude Scaled')
        
    # Next shift the maximums to the same time values- consider only the first maximum for simplicity
    E1_max_index = []
    E2_max_index = []
    for i in range(len(E1)):
        if E1[i] == max(E1):
            E1_max_index.append(i)
        if E2[i] == max(E2):
            E2_max_index.append(i)
    h = t[1] - t[0]
    E2_shifted = np.zeros(len(E2))
    for i in range(len(E2)):
        if (i+E1_max_index[0]-E2_max_index[0]) < len(E2):
            E2_shifted[i] = E2[i+E1_max_index[0]-E2_max_index[0]]
    plt.figure()
    plt.plot(t, E1)
    plt.plot(t, E2_shifted)
    plt.title('E2 shifted in time')
        
    for i in range(len(E1)):
        diff.append((E1[i] - E2_shifted[i])**2)
    return (0.5*h*((diff[0]+diff[-1]) + 2*np.sum(diff[1:-1])))**0.5

def Gauss(x, A, u, o):
    return A*np.exp(-((x-u)**2)/(2*(o**2)))
#%%
# Testing errorCorrection
t = np.arange(0, 50, 0.1)
E1 = Gauss(t, 1, 25, 5)

# Test function against itself
plt.figure()
plt.plot(t, E1)
print(errorCorrection(t, E1, E1)) # Should be zero

# Test against function shifted in time (delayed)
E2 = Gauss(t+5, 1, 25, 5)
plt.figure()
plt.plot(t, E1)
plt.plot(t, E2)
print(errorCorrection(t, E1, E2))

# Shift more in time- should be a larger error
E2 = Gauss(t+10, 1, 25, 5)
plt.figure()
plt.plot(t, E1)
plt.plot(t, E2)
print(errorCorrection(t, E1, E2))

# Change amplitude and width
E2 = Gauss(t, 5, 25, 5)
plt.figure()
plt.plot(t, E1)
plt.plot(t, E2)
print(errorCorrection(t, E1, E2))
E3 = Gauss(t, 1, 25, 10)
plt.plot(t, E3)
print(errorCorrection(t, E1, E3))

#%%
# Test advanced error correction function
t = np.arange(0, 50, 0.1)
E1 = Gauss(t, 1, 25, 5)
E2 = Gauss(t+5, 5, 25, 5)
errorCorrectionAdvanced(t, E1, E2)
